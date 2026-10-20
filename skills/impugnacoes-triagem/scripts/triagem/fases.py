"""Portões e fase derivada: fila de minutas, minuta em revisão, aprovadas, próxima ação, alertas e status."""
import json

from .arquivos import draft_path, matches
from .comum import DONE, KIND_LABEL, KINDS, Refusal, ordered, parse_date, study_hash, today


def gate_open(state):
    docs = state['documentos']
    return docs is not None and (not docs['faltas'] or bool(docs.get('prosseguir')))


def require_gate(state):
    if not gate_open(state):
        raise Refusal('o portão documental não foi resolvido: registre "documentos" (e "prosseguir", se houver '
                      'faltas, com a frase do analista) antes disso.')


def queue(state):
    return [item for item in ordered(state['itens'])
            if item['decisao'] == 'incluir' and item['minuta']['status'] not in DONE]


def in_review(state):
    return [item for item in state['itens'] if item['minuta']['status'] == 'em_revisao']


def approved(state, kind=None):
    return [item for item in ordered(state['itens'])
            if item['minuta']['status'] == 'aprovada' and kind in (None, item['classe'])]


def approval(item):
    return {'id': item['id'], 'versao': item['minuta']['versao'], 'sha256': item['minuta']['sha256']}


def ids_with(state, decision):
    return [item['id'] for item in ordered(state['itens']) if item['decisao'] == decision]


def phase(state):
    if not gate_open(state):
        return 'documentos'
    if state['itens_registrados_em'] is None:
        return 'levantamento'
    if ids_with(state, 'pendente'):
        return 'selecao'
    if queue(state):
        return 'minutas'
    if any(approved(state, kind) and not state['peca'].get(kind) for kind in KINDS.values()):
        return 'peca_final'
    return 'concluido'


def next_action(state, folder, current):
    docs, review = state['documentos'], in_review(state)
    if current == 'documentos':
        if docs is None:
            return ('Verifique pelo conteúdo Edital, TR, ETP, Planilha, Pesquisa de preços e Minuta e registre '
                    'com "documentos". Não faça levantamento nem minuta antes disso.')
        return (f'Apresente o relatório do portão (faltam {", ".join(docs["faltas"])}, com o efeito de cada falta) e '
                'pergunte se o analista envia os documentos ou prossegue. Espere a resposta e registre com '
                '"documentos" ou "prosseguir". Não faça levantamento.')
    if current == 'levantamento':
        return ('Faça o levantamento, um documento por vez, calcule o prazo e registre os itens com "itens". '
                'Não gere minuta nem peça.')
    if current == 'selecao':
        note = f' A minuta {review[0]["id"]} continua em revisão, aguardando decisão.' if review else ''
        return (f'Peça ao analista a decisão sobre cada item pendente ({", ".join(ids_with(state, "pendente"))}): '
                'incluir, descartar ou avaliar depois. Registre a frase literal com "decidir". Silêncio ou escolha '
                'parcial não incluem nada. Não abra minuta nova.' + note)
    if current == 'minutas':
        if not review:
            return (f'Abra a próxima minuta ({queue(state)[0]["id"]}) com "minuta --acao abrir" e escreva só ela. '
                    'Não escreva outras minutas nem a peça.')
        item = review[0]
        draft, path = item['minuta'], draft_path(folder, item['id'])
        if not draft['sha256']:
            return (f'Escreva a minuta {item["id"]} v{draft["versao"]} em {path} e registre com "minuta --id '
                    f'{item["id"]} --acao registrar". Não abra outra minuta.')
        if not matches(folder, item):
            return (f'A minuta {item["id"]} mudou depois do registro: registre de novo e apresente a versão atual '
                    'antes de pedir a decisão.')
        return (f'Apresente a minuta {item["id"]} v{draft["versao"]} com o checklist de auditoria e peça a decisão '
                'explícita sobre ela (aprovo / ajuste: ... / descarto). "ok", "segue" ou "aprova todas" não valem. '
                'Não abra outra minuta nem gere a peça.')
    if current == 'peca_final':
        kinds = [KIND_LABEL[kind] for kind in KINDS.values() if approved(state, kind) and not state['peca'].get(kind)]
        return (f'Todas as minutas foram decididas. Pergunte o formato (único ou por ponto) da peça de '
                f'{" e de ".join(kinds)}, rode "peca --acao verificar", liste as versões aprovadas e peça confirmação '
                'explícita. Sem modelo em assets/, pare e informe. Não assine, não protocole, não envie.')
    text = 'Nada pendente nesta triagem.' if approved(state) else 'Nenhuma minuta aprovada: não há peça a gerar.'
    later = ids_with(state, 'avaliar_depois')
    if later:
        text += f' Para avaliar depois: {", ".join(later)} (retome com "decidir").'
    return text + ' Este script não gera PDF.'


def deadline_alerts(prazo):
    if not prazo:
        return []
    found = [f'prazo: {a if isinstance(a, str) else json.dumps(a, ensure_ascii=False)}'
             for a in prazo.get('alertas') or []]
    limit, current = parse_date(prazo.get('data_limite')), today()
    if limit and current > limit:
        found.append(f'prazo de impugnação vencido em {limit:%d/%m/%Y}, segundo o prazo registrado: avise o analista.')
    elif limit == current:
        found.append('hoje é o último dia do prazo de impugnação, segundo o prazo registrado.')
    return found


def alerts(state, folder, manifest):
    found, current = [], study_hash(manifest)
    if state['estudo_sha256'] is None:
        found.append('o hash do estudo não foi registrado no início (MANIFEST.json ausente): não dá para saber que '
                     'versão do estudo foi usada.')
    elif current is None:
        found.append(f'MANIFEST.json do estudo não encontrado em {manifest}: não dá para conferir se o estudo mudou.')
    elif current != state['estudo_sha256']:
        found.append('o estudo mudou desde o início da triagem: confira se os itens levantados continuam válidos.')
    for item in approved(state):
        if not matches(folder, item):
            found.append(f'minuta {item["id"]} alterada ou removida depois de aprovada: restaure a versão aprovada '
                         'ou use "reabrir".')
    for item in in_review(state):
        if item['minuta']['sha256'] and not matches(folder, item):
            found.append(f'minuta {item["id"]} alterada depois do registro: registre de novo antes de pedir decisão.')
    return found + deadline_alerts(state['prazo'])


def status(state, folder, manifest):
    current, review = phase(state), in_review(state)
    revision = None
    if review:
        item = review[0]
        revision = {'id': item['id'], 'versao': item['minuta']['versao'],
                    'arquivo': str(draft_path(folder, item['id'])), 'registrada': bool(item['minuta']['sha256'])}
    return {
        'pasta': str(folder), 'certame': state['certame'], 'fase': current,
        'proxima_acao': next_action(state, folder, current),
        'documentos': state['documentos'], 'prazo': state['prazo'],
        'itens': {'total': len(state['itens']), 'pendentes': ids_with(state, 'pendente'),
                  'incluidos': ids_with(state, 'incluir'), 'descartados': ids_with(state, 'descartar'),
                  'avaliar_depois': ids_with(state, 'avaliar_depois')},
        'fila_minutas': [item['id'] for item in queue(state)],
        'minuta_em_revisao': revision,
        'aprovadas': [approval(item) for item in approved(state)],
        'peca': state['peca'], 'estudo_sha256': state['estudo_sha256'],
        'alertas': alerts(state, folder, manifest),
    }
