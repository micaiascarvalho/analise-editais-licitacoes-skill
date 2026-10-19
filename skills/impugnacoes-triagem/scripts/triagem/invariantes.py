"""Invariantes do "validar": o que o estado.json e a pasta precisam cumprir mesmo depois de edição à mão."""
import json
import sys

from .arquivos import matches
from .comum import DONE, KIND_LABEL, KINDS, Refusal, id_number, ordered
from .evidencia import check_evidence
from .fases import approval, approved
from .persistencia import STATE_FILE, decode, located, shape_problems

FINAL_ACTION = {'aprovada': 'aprovar', 'descartada': 'descartar'}


def stray_files(folder, state):
    found, known = [], {item['id']: item for item in state['itens']}
    minutas = folder / 'minutas'
    for path in sorted(minutas.iterdir()) if minutas.is_dir() else []:
        if not path.is_file() or path.name.startswith('.'):
            continue
        item = known.get(path.stem) if path.suffix == '.md' else None
        if item is None:
            found.append(f'arquivo inesperado em minutas/: {path.name}')
        elif item['decisao'] != 'incluir':
            found.append(f'minutas/{path.name}: o item {item["id"]} não está incluído')
        elif item['minuta']['status'] not in ('em_revisao', 'aprovada'):
            found.append(f'minutas/{path.name}: minuta não aberta ou já descartada (abra uma por vez com '
                         '"minuta --acao abrir")')
    return found


def piece_problems(folder, state):
    found = []
    for kind, confirmed in state['peca'].items():
        if not confirmed:
            continue
        label = KIND_LABEL.get(kind, kind)
        found += evidence_violations(f'peça de {label} confirmada', confirmed.get('evidencia'), 'confirmar')
        undecided = [item['id'] for item in ordered(state['itens']) if item['classe'] == kind and (
            item['decisao'] == 'pendente' or (item['decisao'] == 'incluir' and item['minuta']['status'] not in DONE))]
        if undecided:
            found.append(f'peça de {label} confirmada com itens não decididos: {", ".join(undecided)}')
        if confirmed.get('aprovadas') != [approval(item) for item in approved(state, kind)]:
            found.append(f'peça de {label} confirmada com versões que não batem com as minutas aprovadas')
    return found


def evidence_violations(subject, text, *args, **kwargs):
    """Evidência gravada que falta ou que o comando recusaria (estado editado à mão, fora da CLI)."""
    if not text:
        return [f'{subject} sem evidência']
    try:
        check_evidence(text, *args, **kwargs)
    except Refusal as exc:
        return [f'{subject} com evidência que não vale ({exc})']
    return []


def final_problems(state, item):
    """Minuta aprovada ou descartada só pela CLI: decisão no histórico, registro da versão e evidência válida."""
    item_id, draft = item['id'], item['minuta']
    status_name, action = draft['status'], FINAL_ACTION[draft['status']]
    found = evidence_violations(f'{item_id}: minuta {status_name}', draft['evidencia'], action, item_id)
    last = draft['historico'][-1] if draft['historico'] else {}
    expected = {'acao': action, 'versao': draft['versao'], 'sha256': draft['sha256'], 'evidencia': draft['evidencia']}
    if any(last.get(key) != value for key, value in expected.items()):
        found.append(f'{item_id}: minuta {status_name} sem a decisão correspondente no histórico '
                     '(ação, versão, sha256 e evidência)')
    registered = f'{item_id} v{draft["versao"]} ({(draft["sha256"] or "")[:12]})'
    if not any(event['acao'] == 'minuta_registrar' and event['detalhe'] == registered for event in state['eventos']):
        found.append(f'{item_id}: minuta {status_name} v{draft["versao"]} sem o evento de registro dessa versão')
    return found


def item_violations(folder, state, item, seen):
    item_id, draft = item['id'], item['minuta']
    number = id_number(item_id)
    if not number:
        return [f'ID fora do formato IMP-NN/ESC-NN: {item_id!r}']
    found = []
    if number in seen:
        found.append(f'ID repetido: {item_id}' if seen[number] == item_id else
                     f'ID repetido: {item_id} tem o mesmo número de {seen[number]}')
    seen.setdefault(number, item_id)
    if item['classe'] != KINDS[number[0]]:
        found.append(f'{item_id}: classe "{item["classe"]}" incoerente com o ID')
    if item['decisao'] != 'pendente':
        found += evidence_violations(f'{item_id}: decisão', item['evidencia'], 'decidir', decision=item['decisao'])
    if draft['status'] and item['decisao'] != 'incluir':
        found.append(f'{item_id}: minuta {draft["status"]} em item não incluído')
    if draft['status'] in DONE:
        found += final_problems(state, item)
    if draft['status'] == 'aprovada' and not matches(folder, item):
        found.append(f'{item_id}: minuta aprovada alterada ou removida (sha256 não confere)')
    return found


def invariant_problems(folder, state):
    found, seen = [], {}
    for item in state['itens']:
        found += item_violations(folder, state, item, seen)
    review = [item['id'] for item in state['itens'] if item['minuta']['status'] == 'em_revisao']
    if len(review) > 1:
        found.append(f'mais de uma minuta em revisão: {", ".join(review)}')
    proceed = (state['documentos'] or {}).get('prosseguir')
    if proceed is not None:
        found += evidence_violations('decisão de prosseguir', proceed['evidencia'], 'prosseguir')
    return found + stray_files(folder, state) + piece_problems(folder, state)


def violations(folder):
    try:
        state = json.loads(decode((folder / STATE_FILE).read_bytes(), STATE_FILE))
    except OSError as exc:
        return [f'{STATE_FILE} ilegível: {exc}']
    except Refusal as exc:
        return [str(exc)]
    except ValueError as exc:
        return [f'{STATE_FILE} não é JSON válido: {exc}']
    found = shape_problems(state)
    if found:
        return found
    try:
        return invariant_problems(folder, state)
    except Exception as exc:  # o validar não pode cair: o que o esquema não previu vira violação, não traceback
        return [f'{STATE_FILE} fora do formato ({type(exc).__name__}: {exc}): corrija o arquivo']


def cmd_validate(args):
    found = violations(located(args.pasta))
    print(json.dumps({'valido': not found, 'violacoes': found}, ensure_ascii=False, indent=2))
    if found:
        print(f'erro: {len(found)} violação(ões) de invariante.', file=sys.stderr)
        return 1
    return 0
