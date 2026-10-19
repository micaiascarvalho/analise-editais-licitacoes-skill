"""Comandos da triagem: slug, iniciar, status, documentos, prosseguir, prazo, itens, decidir e reabrir."""
import sys

from .arquivos import archive
from .comum import (DOC_CODES, FORMAT_VERSION, ID_RE, KINDS, MAX_SLUG, SLUG_RE, Refusal, check_year, id_number, log,
                    make_slug, ordered, parse_date, plain, split_list, stamp, study_hash)
from .evidencia import check_evidence
from .fases import require_gate, status
from .peca import invalidate_piece
from .persistencia import STATE_FILE, leftovers, load, located, locked, read_json, save


def blank_draft(version=0, history=None):
    return {'status': None, 'versao': version, 'sha256': None, 'evidencia': None, 'quando': None,
            'historico': history or []}


def new_item(item_id, kind, title):
    return {'id': item_id, 'classe': kind, 'titulo': title, 'decisao': 'pendente', 'evidencia': None,
            'decidido_em': None, 'minuta': blank_draft()}


def pick(state, text):
    ids = list(dict.fromkeys(part.upper() for part in split_list(text)))
    if not ids:
        raise Refusal('informe os IDs separados por vírgula.')
    known = {item['id']: item for item in state['itens']}
    unknown = [item_id for item_id in ids if item_id not in known]
    if unknown:
        raise Refusal(f'IDs não registrados: {", ".join(unknown)}.')
    return [known[item_id] for item_id in ids]


def parse_codes(text):
    codes = []
    for code in (part.upper() for part in split_list(text)):
        if code == 'RERI':
            raise Refusal('RERI não entra nas listas: use --reri presente|ausente|desconhecido.')
        if code not in DOC_CODES:
            raise Refusal(f'código de documento desconhecido: {code} (aceitos: {", ".join(DOC_CODES)}).')
        if code not in codes:
            codes.append(code)
    return sorted(codes, key=DOC_CODES.index)


def cmd_documents(state, folder, args):
    present, missing = parse_codes(args.presentes), parse_codes(args.faltas)
    both = [code for code in present if code in missing]
    if both:
        raise Refusal(f'{", ".join(both)} não pode estar em --presentes e em --faltas ao mesmo tempo.')
    unclassified = [code for code in DOC_CODES if code not in present and code not in missing]
    if unclassified:
        raise Refusal(f'faltou classificar {", ".join(unclassified)}: cada um dos 6 códigos vai em --presentes ou '
                      '--faltas.')
    previous = state['documentos'] or {}
    authorized = previous.get('prosseguir')
    if authorized and not (missing and set(missing) <= set(authorized['faltas'])):
        authorized = None
    state['documentos'] = {'presentes': present, 'faltas': missing,
                           'reri': args.reri or previous.get('reri', 'desconhecido'),
                           'registrado_em': stamp(), 'prosseguir': authorized}
    if args.esfera:
        state['certame']['esfera'] = args.esfera
    log(state, 'documentos', f'presentes: {", ".join(present) or "nenhum"}; faltas: {", ".join(missing) or "nenhuma"}; '
                             f'RERI: {state["documentos"]["reri"]}')
    if not missing:
        return 'Portão resolvido: todos os documentos estão presentes.'
    if authorized:
        return 'Portão registrado: as faltas já tinham decisão de prosseguir do analista.'
    return ('Portão registrado com faltas: apresente o relatório (o que falta e o efeito de cada falta) e pergunte se '
            'o analista envia os documentos ou prossegue.')


def cmd_proceed(state, folder, args):
    docs = state['documentos']
    if docs is None:
        raise Refusal('o portão documental ainda não foi registrado: rode "documentos" primeiro.')
    if not docs['faltas']:
        raise Refusal('não há faltas no portão documental: não é preciso prosseguir.')
    evidence = check_evidence(args.evidencia, 'prosseguir')
    docs['prosseguir'] = {'evidencia': evidence, 'quando': stamp(), 'faltas': list(docs['faltas'])}
    log(state, 'prosseguir', f'sem {", ".join(docs["faltas"])}: "{evidence}"')
    return 'Decisão de prosseguir registrada: o portão está resolvido; siga para o levantamento.'


def cmd_deadline(state, folder, args):
    data = read_json(args.dados, 'os dados do prazo')
    if not isinstance(data, dict):
        raise Refusal('os dados do prazo precisam ser o objeto JSON de "prazo.py --json".')
    absent = [key for key in ('abertura', 'data_limite', 'alertas') if key not in data]
    if absent:
        raise Refusal(f'dados do prazo sem {", ".join(absent)}: use a saída de "prazo.py --json".')
    if not isinstance(data['alertas'], list):
        raise Refusal('"alertas" dos dados do prazo precisa ser uma lista.')
    if data['data_limite'] is not None and parse_date(data['data_limite']) is None:
        raise Refusal(f'data_limite inválida: "{data["data_limite"]}" (use AAAA-MM-DD).')
    state['prazo'] = {**data, 'registrado_em': stamp()}
    log(state, 'prazo', f'data-limite {data["data_limite"]}, abertura {data["abertura"]}')
    return 'Prazo registrado.'


def cmd_items(state, folder, args):
    require_gate(state)
    data = read_json(args.arquivo, 'o arquivo de itens')
    if not isinstance(data, list):
        raise Refusal('o arquivo de itens precisa ser uma lista de {id, classe, titulo}.')
    known, new = {id_number(item['id']): item['id'] for item in state['itens']}, []
    for n, entry in enumerate(data, 1):
        if not isinstance(entry, dict):
            raise Refusal(f'item {n}: precisa ser um objeto {{id, classe, titulo}}.')
        item_id = str(entry.get('id') or '').strip()
        match = ID_RE.fullmatch(item_id)
        if not match:
            raise Refusal(f'item {n}: ID "{item_id}" fora do formato IMP-NN ou ESC-NN (2 ou mais dígitos).')
        kind = plain(str(entry.get('classe') or ''))
        if kind != KINDS[match[1]]:
            raise Refusal(f'{item_id}: classe "{entry.get("classe")}" incoerente com o ID '
                          f'({match[1]} é sempre {KINDS[match[1]]}).')
        title = ' '.join(str(entry.get('titulo') or '').split())
        if not title:
            raise Refusal(f'{item_id}: título vazio.')
        key = id_number(item_id)
        if key in known:
            clash = 'já existe' if known[key] == item_id else f'repete o número de {known[key]}'
            raise Refusal(f'{item_id} {clash}: os IDs são estáveis; dê um número novo ao item novo.')
        known[key] = item_id
        new.append(new_item(item_id, kind, title))
    if not new and state['itens_registrados_em'] is not None:
        raise Refusal('nenhum item novo no arquivo.')
    state['itens'] += new
    state['itens_registrados_em'] = stamp()
    for kind in sorted({item['classe'] for item in new}):
        invalidate_piece(state, kind, 'itens novos registrados')
    ids = ', '.join(item['id'] for item in new)
    log(state, 'itens', f'registrados: {ids}' if new else 'levantamento concluído sem itens')
    if not new:
        return 'Levantamento registrado sem itens: não há o que selecionar.'
    return f'{len(new)} item(ns) registrado(s) como pendente(s): {ids}. Peça a seleção ao analista.'


def cmd_decide(state, folder, args):
    require_gate(state)
    if not state['itens']:
        raise Refusal('nenhum item registrado: registre o levantamento com "itens" antes de decidir.')
    evidence = check_evidence(args.evidencia, 'decidir', decision=args.decisao)
    if args.ids.strip().upper() == 'PENDENTES':
        targets = [item for item in ordered(state['itens']) if item['decisao'] == 'pendente']
        if not targets:
            raise Refusal('não há itens pendentes.')
    else:
        targets = pick(state, args.ids)
    blocked = [item['id'] for item in targets if item['minuta']['status']]
    if blocked:
        raise Refusal(f'{", ".join(blocked)} já tem minuta aberta ou decidida: para mudar a decisão use "reabrir" '
                      'com o motivo.')
    for item in targets:
        if args.decisao == 'incluir' and item['decisao'] != 'incluir':
            invalidate_piece(state, item['classe'], f'{item["id"]} incluído')
        item.update(decisao=args.decisao, evidencia=evidence, decidido_em=stamp())
    ids = ', '.join(item['id'] for item in targets)
    log(state, 'decidir', f'{ids} → {args.decisao}: "{evidence}"')
    return f'Decisão registrada para {ids}: {args.decisao.replace("_", " ")}.'


def cmd_reopen(state, folder, args):
    if not state['itens']:
        raise Refusal('nenhum item registrado.')
    motive = check_evidence(args.motivo, 'reabrir')
    targets = pick(state, args.ids)
    idle = [item['id'] for item in targets if item['decisao'] == 'pendente' and not item['minuta']['status']]
    if idle:
        raise Refusal(f'{", ".join(idle)} já está pendente: não há o que reabrir.')
    for item in targets:
        draft = item['minuta']
        archived = archive(folder, item['id'], draft['versao'])
        history = draft['historico'] + [{'versao': draft['versao'], 'acao': 'reabrir', 'motivo': motive,
                                         'arquivo': archived, 'quando': stamp()}]
        item['minuta'] = blank_draft(draft['versao'], history)
        item.update(decisao='pendente', evidencia=None, decidido_em=None)
        invalidate_piece(state, item['classe'], f'{item["id"]} reaberto')
    ids = ', '.join(item['id'] for item in targets)
    log(state, 'reabrir', f'{ids}: "{motive}"')
    return f'{ids} reaberto(s): voltam para a seleção; peça a nova decisão ao analista.'


def cmd_slug(args):
    print(make_slug(args.orgao, args.modalidade, args.numero, args.ano))
    return 0


def check_new_folder(folder):
    if (folder / STATE_FILE).exists():
        raise Refusal(f'{folder} já existe: retome com "status --pasta {folder}".')
    extra = leftovers(folder)
    if extra:
        raise Refusal(f'{folder} já existe sem {STATE_FILE} e tem {", ".join(extra)}: confira a pasta ou use outro '
                      '--slug.')


def cmd_init(args):
    check_year(args.ano)
    if args.slug and not SLUG_RE.fullmatch(args.slug):
        raise Refusal(f'slug inválido: "{args.slug}" (use minúsculas sem acento, números e hífens).')
    slug = args.slug or make_slug(args.orgao, args.modalidade, args.numero, args.ano)
    if len(slug) > MAX_SLUG:
        raise Refusal(f'o slug ficou com {len(slug)} caracteres (máximo {MAX_SLUG}): passe um --slug mais curto.')
    folder = (located(args.raiz) / slug).resolve()
    check_new_folder(folder)
    study = study_hash(args.manifesto)
    folder.mkdir(parents=True, exist_ok=True)
    with locked(folder):
        check_new_folder(folder)  # outro "iniciar" pode ter gravado enquanto este esperava a trava
        for sub in ('minutas/historico', 'texto'):
            (folder / sub).mkdir(parents=True, exist_ok=True)
        certame = {'slug': slug, 'orgao': args.orgao.strip(), 'modalidade': args.modalidade.strip(),
                   'numero': args.numero.strip(), 'ano': args.ano, 'esfera': args.esfera}
        state = {'formato': FORMAT_VERSION, 'certame': certame, 'criado_em': stamp(), 'estudo_sha256': study,
                 'documentos': None, 'prazo': None, 'itens_registrados_em': None, 'itens': [],
                 'peca': {kind: None for kind in KINDS.values()}, 'eventos': []}
        log(state, 'iniciar', f'pasta criada para {slug}')
        save(folder, state)
    if study is None:
        print(f'aviso: MANIFEST.json do estudo não encontrado em {args.manifesto}; estudo_sha256 fica null.',
              file=sys.stderr)
    return {'mensagem': f'Pasta do edital criada em {folder}.', **status(state, folder, args.manifesto)}


def cmd_status(args):
    folder = located(args.pasta)
    return status(load(folder), folder, args.manifesto)
