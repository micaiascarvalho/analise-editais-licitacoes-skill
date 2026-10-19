#!/usr/bin/env python3
"""Máquina de estados da triagem de um edital: impõe os portões da skill impugnacoes-triagem. Python 3.10+.

A fase é derivada dos dados, nesta ordem: documentos, levantamento, selecao, minutas, peca_final, concluido.
O estado fica em <pasta>/estado.json (fonte de verdade); <pasta>/registro.md é regenerado a cada mudança.
A cada turno, rode "status" e faça só a ação de "proxima_acao". Os comandos recusam transições fora de ordem.
Os comandos que gravam usam uma trava por pasta (.estado.lock): chamadas em paralelo esperam a vez.

Uso:
  estado.py slug --orgao TXT --modalidade TXT --numero TXT --ano AAAA
  estado.py iniciar --raiz DIR --orgao TXT --modalidade TXT --numero TXT --ano AAAA [--esfera ESFERA] [--slug SLUG]
  estado.py status --pasta DIR
  estado.py documentos --pasta DIR --presentes EDITAL,TR --faltas ETP,PLANILHA,PESQUISA,MINUTA [--reri presente]
  estado.py prosseguir --pasta DIR --evidencia "frase literal do analista"
  estado.py prazo --pasta DIR --dados prazo.json        (--dados - lê da entrada padrão)
  estado.py itens --pasta DIR --arquivo itens.json      (lista de {id, classe, titulo})
  estado.py decidir --pasta DIR --ids IMP-01,ESC-02|PENDENTES --decisao incluir|descartar|avaliar_depois --evidencia "..."
  estado.py minuta --pasta DIR --acao abrir
  estado.py minuta --pasta DIR --id IMP-01 --acao registrar
  estado.py minuta --pasta DIR --id IMP-01 --acao aprovar|ajustar|descartar --evidencia "..."
  estado.py reabrir --pasta DIR --ids IMP-01 --motivo "..."
  estado.py peca --pasta DIR --acao verificar
  estado.py peca --pasta DIR --acao confirmar --tipo impugnacao|esclarecimento --formato unico|por_ponto --evidencia "..."
  estado.py validar --pasta DIR                         sai com 1 se algum invariante for violado
"""
import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

try:
    import fcntl
except ImportError:  # Windows: sem fcntl, os comandos rodam sem trava
    fcntl = None

SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = SKILL_DIR / 'references' / 'estudo' / 'MANIFEST.json'
DEFAULT_ASSETS = SKILL_DIR / 'assets'
STATE_FILE = 'estado.json'
LOG_FILE = 'registro.md'
LOCK_FILE = '.estado.lock'
# O que o "iniciar" aceita numa pasta sem estado.json (texto/ do extrair_texto.py, iniciar interrompido).
REUSABLE = {'minutas', 'texto', LOCK_FILE}
FORMAT_VERSION = 1
LAST_EVENTS = 20
MAX_SLUG = 200

DOC_CODES = ('EDITAL', 'TR', 'ETP', 'PLANILHA', 'PESQUISA', 'MINUTA')
RERI_VALUES = ('presente', 'ausente', 'desconhecido')
SPHERES = ('federal', 'estadual', 'distrital', 'municipal')
KINDS = {'IMP': 'impugnacao', 'ESC': 'esclarecimento'}
KIND_LABEL = {'impugnacao': 'impugnação', 'esclarecimento': 'esclarecimento'}
DECISIONS = ('incluir', 'descartar', 'avaliar_depois')
DONE = ('aprovada', 'descartada')
DRAFT_LABEL = {'em_revisao': 'em revisão', 'aprovada': 'aprovada', 'descartada': 'descartada'}
FINAL_ACTION = {'aprovada': 'aprovar', 'descartada': 'descartar'}
ID_RE = re.compile(r'(IMP|ESC)-(\d{2,})', re.ASCII)  # sempre com fullmatch
SLUG_RE = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')

# Comparadas depois de plain(): sem caixa, sem acento, sem pontuação.
GENERIC = ('pode seguir', 'okay', 'ok', 'sim', 's', 'segue', 'continua', 'continue', 'certo',
           'beleza', 'blz', 'show', 'perfeito', 'top', 'valeu')
BATCH = re.compile(r'\b(?:todas|todos|tudo|ambas|ambos|demais|restantes?|essas|estas|em (?:bloco|lote)'
                   r'|(?:as|os) (?:outras|outros|proximas|proximos|seguintes|minutas|itens'
                   r'|duas|dois|tres|quatro|cinco))\b|\baprovad[ao]s\b|\baprov\w* geral\b')
NEGATED = re.compile(r'\bnao (?:\w+ )?aprov|desaprov')
NEGATIVE_ONLY = {'nao', 'nunca', 'jamais', 'nem', 'ainda', 'agora', 'por', 'enquanto'}
# Verbos que, negados na mesma oração ("não prossiga", "nunca aprovaria"), viram recusa da ação.
DENIABLE = {
    'prosseguir': r'prossig|prosseg|segu(?:e|em|ir|imos|indo)\b|sig[ao]m?\b|continu|avanc',
    'incluir': r'inclu',
    'descartar': r'descart|exclu(?:a|i|ir|o|sao)\b|retir|remov|tir(?:a|ar|e|em|o|ei)\b',
    'aprovar': r'aprov',
    'confirmar': r'confirm|ger(?:a|ar|e|em|ou)\b|emit|fech',
}
CONDITION = re.compile(r'\b(?:mas|porem|contudo|entretanto|desde que|contanto que)\b|\baprov(?:aria|arei|aremos|asse)')
CONDITION_NEAR = re.compile(r'\b(?:se|quando|antes de|depois de|apos)\b')
DISCARD = re.compile(r'\b(?:descart|exclu|retir|remov)|\btira(?:r|m|ndo)?\b|\bnao usar')
LOOSE_ID = re.compile(r'\b(impugnac\w*|esclarec\w*|imp|esc) ?(\d+)\b')
DRAFT_HINT = 'peça a decisão explícita sobre a minuta em revisão: aprovo / ajuste: ... / descarto'
HINTS = {
    'prosseguir': 'peça ao analista que diga explicitamente que prossegue sem os documentos que faltam '
                  '(por exemplo: "prossiga sem o ETP")',
    'decidir': 'peça ao analista a decisão explícita sobre os itens (por exemplo: "incluir IMP-01 e descartar ESC-02")',
    'aprovar': DRAFT_HINT, 'ajustar': DRAFT_HINT, 'descartar': DRAFT_HINT,
    'reabrir': 'peça ao analista o motivo da reabertura (por exemplo: a retificação que mudou o item)',
    'confirmar': 'liste as versões aprovadas e peça ao analista a confirmação explícita da peça',
}

NONE = type(None)
SHAPE = {'certame': dict, 'estudo_sha256': (str, NONE), 'documentos': (dict, NONE), 'prazo': (dict, NONE),
         'itens_registrados_em': (str, NONE), 'itens': list, 'peca': dict, 'eventos': list}
CERTAME_FIELDS = {'slug': str, 'orgao': str, 'modalidade': str, 'numero': str, 'ano': str}
DOCS_FIELDS = {'presentes': list, 'faltas': list, 'reri': str}
PROCEED_FIELDS = {'evidencia': str, 'faltas': list}
DEADLINE_FIELDS = {'abertura': object, 'data_limite': object, 'alertas': list}
EVENT_FIELDS = {'quando': str, 'acao': str, 'detalhe': str}
ITEM_FIELDS = {'id': str, 'classe': str, 'titulo': str, 'decisao': str, 'evidencia': (str, NONE), 'minuta': dict}
DRAFT_FIELDS = {'status': (str, NONE), 'versao': int, 'sha256': (str, NONE), 'evidencia': (str, NONE),
                'historico': list}


class Refusal(Exception):
    """Transição fora de ordem ou dado inválido; a mensagem diz o que fazer."""


def now():
    """Horário local com fuso; os testes substituem esta função."""
    return datetime.now().astimezone().replace(microsecond=0)


def stamp():
    return now().isoformat()


def plain(text):
    text = unicodedata.normalize('NFKD', text or '')
    text = ''.join(c for c in text if not unicodedata.combining(c)).lower()
    return ' '.join(re.sub(r'[^a-z0-9]+', ' ', text).split())


def nfc(text):
    return unicodedata.normalize('NFC', text)


def clauses(text):
    """Orações da frase em plain(), cada uma com a pontuação que a fecha ("aprovo? não" vira pergunta e negativa)."""
    parts = re.split(r'([.,;:!?\n]+)', text or '')
    return [(plain(part), end) for part, end in zip(parts[::2], parts[1::2] + [''])]


def split_list(text):
    return [part.strip() for part in (text or '').split(',') if part.strip()]


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_date(value):
    text = str(value or '').strip()[:10]
    for fmt in ('%Y-%m-%d', '%d/%m/%Y'):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    return None


def check_year(year):
    if not re.fullmatch(r'\d{4}', year or ''):
        raise Refusal(f'ano inválido: "{year}" (use AAAA).')


def make_slug(orgao, modalidade, numero, ano):
    check_year(ano)
    if not all(plain(part) for part in (orgao, modalidade, numero)):
        raise Refusal('órgão, modalidade e número precisam ter letras ou números.')
    return '-'.join(plain(' '.join((orgao, modalidade, numero, ano))).split())


def denies(text, action):
    """A frase é só uma negativa ("não", "ainda não") ou nega, na mesma oração, o verbo da ação."""
    words = set(plain(text).split())
    if words <= NEGATIVE_ONLY and words & {'nao', 'nunca', 'jamais'}:
        return True
    verbs = DENIABLE.get(action)
    return bool(verbs) and any(re.search(rf'\b(?:nao|nunca|jamais)(?: \w+){{0,2}} (?:{verbs})', clause)
                               for clause, _ in clauses(text))


def conditional(text):
    """Aprovação com ressalva, condição ou em forma de pergunta ("aprovo, mas...", "aprovaria se...", "aprovo?")."""
    if CONDITION.search(plain(text)):
        return True
    return any('aprov' in clause and ('?' in end or CONDITION_NEAR.search(clause)) for clause, end in clauses(text))


def canonical_id(prefix, number):
    return f'{prefix}-{int(number):02d}'


def cited_ids(norm):
    """IDs citados em qualquer grafia (IMP-2, imp 02, imp02, esclarecimento 1), na forma IMP-NN/ESC-NN."""
    return {canonical_id('IMP' if kind.startswith('imp') else 'ESC', number) for kind, number in LOOSE_ID.findall(norm)}


def check_approval(text, norm, item_id, hint):
    if 'aprov' not in norm:
        raise Refusal(f'para aprovar, a frase do analista precisa dizer "aprovo"; {hint}.')
    if NEGATED.search(norm) or denies(text, 'aprovar'):
        raise Refusal(f'a frase nega a aprovação; {hint}.')
    if BATCH.search(norm):
        raise Refusal('aprovação em lote não é aceita: apresente a minuta em revisão e peça a decisão sobre ela '
                      '(aprovo / ajuste: ... / descarto).')
    number = id_number(item_id)
    others = sorted(cited_ids(norm) - {canonical_id(*number) if number else item_id})
    if others:
        raise Refusal(f'a frase cita {", ".join(others)}, mas a minuta em revisão é {item_id}: '
                      f'peça a decisão sobre {item_id}.')
    if conditional(text):
        raise Refusal(f'a frase traz condição, ressalva ou pergunta ("{text}"): {DRAFT_HINT}; se o analista quer '
                      'mudar algo, é ajuste.')


def check_evidence(text, action=None, item_id=None, decision=None):
    """Recusa evidência vazia, genérica ou negativa e, por ação, o que pareça aprovação implícita ou em lote.

    Em "decidir", decision é a decisão registrada (incluir, descartar, avaliar_depois)."""
    text = ' '.join((text or '').split())
    norm = plain(text)
    hint = HINTS.get(action, 'peça ao analista uma resposta explícita')
    if not norm:
        raise Refusal(f'evidência vazia: registre a frase literal do analista; {hint}.')
    rest = norm
    for phrase in GENERIC:
        rest = re.sub(rf'\b{phrase}\b', ' ', rest)
    if not rest.strip():
        raise Refusal(f'"{text}" é genérico e não vale como decisão; {hint}.')
    if action == 'aprovar':
        check_approval(text, norm, item_id, hint)
    elif denies(text, decision if action == 'decidir' else action):
        raise Refusal(f'"{text}" nega ou recusa a ação e não vale como autorização; {hint}.')
    if action == 'ajustar' and len(text) < 10:
        raise Refusal('o ajuste precisa da instrução do analista (pelo menos 10 caracteres): pergunte o que mudar.')
    if action == 'descartar' and not DISCARD.search(norm):
        raise Refusal('para descartar, a frase do analista precisa dizer "descarto", "excluir", "retirar", '
                      f'"remover", "não usar" ou "tira"; {hint}.')
    return text


def study_hash(manifest):
    try:
        return json.loads(Path(manifest).read_text(encoding='utf-8')).get('estudo_sha256')
    except (OSError, ValueError, AttributeError):
        return None


def decode(data, label):
    try:
        return data.decode('utf-8-sig')
    except UnicodeDecodeError:
        raise Refusal(f'não foi possível ler {label} como UTF-8: salve o arquivo em UTF-8 e rode de novo.')


def read_input(source):
    if str(source) != '-':
        return Path(source).read_bytes()
    stream = getattr(sys.stdin, 'buffer', None)
    # Sem buffer (entrada trocada por texto), o surrogateescape devolve os bytes que não eram UTF-8.
    return stream.read() if stream else sys.stdin.read().encode('utf-8', 'surrogateescape')


def read_json(source, label):
    try:
        data = read_input(source)
    except OSError as exc:
        raise Refusal(f'não foi possível ler {source}: {exc}')
    text = decode(data, label)
    if not text.strip():
        raise Refusal(f'entrada vazia ({label}): se veio de um pipe, o comando anterior falhou '
                      '(veja o erro dele acima); nada foi registrado.')
    try:
        return json.loads(text)
    except ValueError as exc:
        raise Refusal(f'o conteúdo de {label} não é JSON válido: {exc}')


def write_atomic(path, text):
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f'.{path.name}.', suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            handle.write(text)
        mask = os.umask(0)
        os.umask(mask)
        os.chmod(tmp, 0o666 & ~mask)  # o mkstemp cria com 0600; o resto da pasta segue o umask
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def wrong_fields(value, fields, prefix):
    """Campos ausentes ou de tipo errado, com o caminho (ex.: documentos.faltas). bool não vale como número."""
    if not isinstance(value, dict):
        return [prefix or 'objeto']
    return [f'{prefix}.{name}' if prefix else name for name, kind in fields.items()
            if name not in value or not isinstance(value[name], kind) or isinstance(value[name], bool)]


def docs_problems(docs):
    if docs is None:
        return []
    found = wrong_fields(docs, DOCS_FIELDS, 'documentos')
    if found:
        return found
    if not all(code in DOC_CODES for code in docs['presentes'] + docs['faltas']):
        found.append('documentos.presentes/faltas (código desconhecido)')
    if docs['reri'] not in RERI_VALUES:
        found.append('documentos.reri')
    proceed = docs.get('prosseguir')
    if proceed is not None:
        found += wrong_fields(proceed, PROCEED_FIELDS, 'documentos.prosseguir')
    return found


def item_problems(item):
    found = wrong_fields(item, ITEM_FIELDS, '')
    if found:
        return found
    draft = item['minuta']
    found = wrong_fields(draft, DRAFT_FIELDS, 'minuta')
    if item['decisao'] not in ('pendente',) + DECISIONS:
        found.append(f'decisao ("{item["decisao"]}")')
    if found:
        return found
    if draft['status'] not in (None, 'em_revisao') + DONE:
        found.append(f'minuta.status ("{draft["status"]}")')
    if draft['versao'] < 0:
        found.append('minuta.versao')
    if not all(isinstance(entry, dict) for entry in draft['historico']):
        found.append('minuta.historico')
    return found


def shape_problems(state):
    """Esquema do estado.json: o que os comandos usam precisa existir com o tipo certo (edição à mão não derruba)."""
    if not isinstance(state, dict):
        return [f'{STATE_FILE} não é um objeto JSON']
    found = [f'campo ausente ou inválido em {STATE_FILE}: {key}'
             for key, kind in SHAPE.items() if not isinstance(state.get(key), kind)]
    if found:
        return found
    bad = wrong_fields(state['certame'], CERTAME_FIELDS, 'certame') + docs_problems(state['documentos'])
    if state['certame'].get('esfera') not in (None,) + SPHERES:
        bad.append('certame.esfera')
    if state['prazo'] is not None:
        bad += wrong_fields(state['prazo'], DEADLINE_FIELDS, 'prazo')
    bad += [f'peca.{kind}' for kind, value in state['peca'].items() if not isinstance(value, (dict, NONE))]
    bad += [f'eventos[{n}]' for n, event in enumerate(state['eventos'], 1) if wrong_fields(event, EVENT_FIELDS, '')]
    found = [f'campo ausente ou inválido em {STATE_FILE}: {name}' for name in bad]
    for n, item in enumerate(state['itens'], 1):
        problems = item_problems(item)
        if problems:
            found.append(f'item {n} fora do formato em {STATE_FILE}: {", ".join(problems)}')
    return found


def twin(folder, name):
    """Entrada de folder com o mesmo nome em NFC (pastas copiadas de outro sistema podem vir em NFD)."""
    try:
        return next((entry for entry in folder.iterdir() if nfc(entry.name) == nfc(name)), None)
    except OSError:
        return None


def located(path):
    """Caminho real no disco, aceitando partes digitadas em NFC quando a pasta está em NFD (ou o contrário)."""
    path = Path(os.path.abspath(path))
    found = Path(path.anchor)
    for part in path.parts[1:]:
        candidate = found / part
        if not candidate.exists() and found.is_dir():
            candidate = twin(found, part) or candidate
        found = candidate
    return found.resolve()


def leftovers(folder):
    """O que impede o "iniciar" de aproveitar uma pasta que já existe sem estado.json."""
    return sorted(entry.name for entry in folder.iterdir() if entry.name not in REUSABLE) if folder.is_dir() else []


def state_file(folder):
    path = folder / STATE_FILE
    if path.is_file():
        return path
    if folder.is_dir() and SLUG_RE.fullmatch(folder.name) and not leftovers(folder):
        raise Refusal(f'{folder} existe, mas não tem {STATE_FILE}: rode "iniciar --raiz {folder.parent} --slug '
                      f'{folder.name}" com os dados do certame (ele aproveita a pasta).')
    raise Refusal(f'{folder} não tem {STATE_FILE}: crie a pasta do edital com "iniciar".')


def load(folder):
    path = state_file(folder)
    text = decode(path.read_bytes(), str(path))
    try:
        state = json.loads(text)
    except ValueError as exc:
        raise Refusal(f'{path} não é JSON válido ({exc}): rode "validar" e corrija antes de seguir.')
    problems = shape_problems(state)
    if problems:
        raise Refusal('; '.join(problems) + ': rode "validar" e corrija antes de seguir.')
    return state


@contextmanager
def locked(folder):
    """Trava exclusiva da pasta: quem grava espera o outro terminar, em vez de sobrescrever o que ele gravou."""
    with open(folder / LOCK_FILE, 'a', encoding='utf-8') as handle:
        if fcntl:
            fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def save(folder, state):
    write_atomic(folder / STATE_FILE, json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    write_atomic(folder / LOG_FILE, render_log(state))


def log(state, action, detail):
    state['eventos'].append({'quando': stamp(), 'acao': action, 'detalhe': detail})


def blank_draft(version=0, history=None):
    return {'status': None, 'versao': version, 'sha256': None, 'evidencia': None, 'quando': None,
            'historico': history or []}


def new_item(item_id, kind, title):
    return {'id': item_id, 'classe': kind, 'titulo': title, 'decisao': 'pendente', 'evidencia': None,
            'decidido_em': None, 'minuta': blank_draft()}


def id_number(item_id):
    """(prefixo, número) de um ID válido, ou None. IMP-02 e IMP-002 têm o mesmo número: não podem coexistir."""
    match = ID_RE.fullmatch(str(item_id))
    return (match[1], int(match[2])) if match else None


def id_key(item_id):
    number = id_number(item_id)
    return (0 if number[0] == 'IMP' else 1, number[1], item_id) if number else (2, 0, str(item_id))


def ordered(items):
    return sorted(items, key=lambda item: id_key(item['id']))


def draft_path(folder, item_id):
    return folder / 'minutas' / f'{item_id}.md'


def matches(folder, item):
    path = draft_path(folder, item['id'])
    return path.is_file() and sha256_file(path) == item['minuta']['sha256']


def archive(folder, item_id, version):
    """Move minutas/<ID>.md para o histórico sem sobrescrever uma versão já arquivada."""
    source = draft_path(folder, item_id)
    if not source.is_file():
        return None
    history = folder / 'minutas' / 'historico'
    target, n = history / f'{item_id}.v{version}.md', 2
    while target.exists():
        target, n = history / f'{item_id}.v{version}-{n}.md', n + 1
    history.mkdir(parents=True, exist_ok=True)
    os.replace(source, target)
    return target.relative_to(folder).as_posix()


def archived_copies(folder, item_id, version):
    history = folder / 'minutas' / 'historico'
    name = re.compile(rf'{re.escape(item_id)}\.v{version}(?:-\d+)?\.md')
    return sorted(path for path in history.iterdir() if name.fullmatch(path.name)) if history.is_dir() else []


def restore(folder, state):
    """Desfaz um arquivamento interrompido (o arquivo foi para o histórico, mas o estado não chegou a ser gravado):
    a minuta registrada sumiu de minutas/ e a cópia com o mesmo sha256 está no histórico."""
    for item in state['itens']:
        draft, path = item['minuta'], draft_path(folder, item['id'])
        if draft['status'] not in ('em_revisao', 'aprovada') or not draft['sha256'] or path.exists():
            continue
        for copy in archived_copies(folder, item['id'], draft['versao']):
            if sha256_file(copy) == draft['sha256']:
                os.replace(copy, path)
                log(state, 'minuta_restaurada', f'{item["id"]} v{draft["versao"]}: {copy.name} voltou para minutas/')
                break


def gate_open(state):
    docs = state['documentos']
    return docs is not None and (not docs['faltas'] or bool(docs.get('prosseguir')))


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
            return ('Verifique pelo conteúdo Edital, TR, ETP, Planilha, Pesquisa de preços, Minuta e RERI e registre '
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
    limit, today = parse_date(prazo.get('data_limite')), now().date()
    if limit and today > limit:
        found.append(f'prazo de impugnação vencido em {limit:%d/%m/%Y}, segundo o prazo registrado: avise o analista.')
    elif limit == today:
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


def cell(text, limit=120):
    text = ' '.join(str(text).split()).replace('|', '\\|')
    return text if len(text) <= limit else text[:limit - 1] + '…'


def draft_label(draft):
    if not draft['status']:
        return '—'
    text = f'{DRAFT_LABEL[draft["status"]]} v{draft["versao"]}'
    return text + ' (não registrada)' if draft['status'] == 'em_revisao' and not draft['sha256'] else text


def evidence_label(item):
    parts = []
    if item['evidencia']:
        parts.append(f'decisão: "{item["evidencia"]}"')
    if item['minuta']['evidencia']:
        parts.append(f'minuta: "{item["minuta"]["evidencia"]}"')
    return ' / '.join(parts) or '—'


def render_log(state):
    certame, docs, prazo = state['certame'], state['documentos'], state['prazo']
    sphere = f' (esfera {certame["esfera"]})' if certame.get('esfera') else ''
    if docs is None:
        docs_line = 'portão não registrado'
    else:
        docs_line = (f'presentes {", ".join(docs["presentes"]) or "nenhum"}; '
                     f'faltas {", ".join(docs["faltas"]) or "nenhuma"}; RERI {docs["reri"]}'
                     + ('; prosseguir autorizado' if docs.get('prosseguir') else ''))
    if prazo is None:
        prazo_line = 'não calculado'
    else:
        limit = parse_date(prazo.get('data_limite'))
        prazo_line = f'data-limite {limit:%d/%m/%Y}' if limit else f'data-limite {prazo.get("data_limite")}'
        prazo_line += f' (abertura {prazo.get("abertura")})'
    lines = ['<!-- Gerado por scripts/estado.py a partir de estado.json. Não edite: use o estado.py. -->', '',
             f'# Registro da triagem {certame["slug"]}', '',
             f'- Certame: {certame["orgao"]}, {certame["modalidade"]} {certame["numero"]}/{certame["ano"]}{sphere}',
             f'- Fase: {phase(state)}',
             f'- Documentos: {docs_line}',
             f'- Prazo: {prazo_line}',
             f'- Estudo: {state["estudo_sha256"] or "sem hash registrado"}',
             '', '## Itens', '']
    if state['itens']:
        lines += ['| ID | Classe | Título | Decisão | Minuta | Evidência |', '| :-- | :-- | :-- | :-- | :-- | :-- |']
        lines += [f'| {item["id"]} | {KIND_LABEL.get(item["classe"], item["classe"])} | {cell(item["titulo"])} | '
                  f'{item["decisao"].replace("_", " ")} | {draft_label(item["minuta"])} | '
                  f'{cell(evidence_label(item))} |' for item in ordered(state['itens'])]
    else:
        lines.append('Nenhum item registrado.')
    lines += ['', '## Últimos eventos', '']
    lines += [f'- {event["quando"]} {event["acao"]}: {cell(event["detalhe"], 200)}'
              for event in state['eventos'][-LAST_EVENTS:]]
    return '\n'.join(lines) + '\n'


def invalidate_piece(state, kind, reason):
    if state['peca'].get(kind):
        state['peca'][kind] = None
        log(state, 'peca_invalidada', f'confirmação da peça de {KIND_LABEL[kind]} desfeita: {reason}')


def pick(state, text):
    ids = list(dict.fromkeys(part.upper() for part in split_list(text)))
    if not ids:
        raise Refusal('informe os IDs separados por vírgula.')
    known = {item['id']: item for item in state['itens']}
    unknown = [item_id for item_id in ids if item_id not in known]
    if unknown:
        raise Refusal(f'IDs não registrados: {", ".join(unknown)}.')
    return [known[item_id] for item_id in ids]


def require_gate(state):
    if not gate_open(state):
        raise Refusal('o portão documental não foi resolvido: registre "documentos" (e "prosseguir", se houver '
                      'faltas, com a frase do analista) antes disso.')


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


def current_review(state, item_id):
    review = in_review(state)
    if not review:
        raise Refusal('nenhuma minuta em revisão: abra a próxima com "minuta --acao abrir".')
    if review[0]['id'] != item_id:
        raise Refusal(f'a minuta em revisão é {review[0]["id"]}, não {item_id}: decida uma por vez.')
    return review[0]


def open_draft(state, folder, args):
    review = in_review(state)
    if review:
        draft = review[0]['minuta']
        raise Refusal(f'a minuta {review[0]["id"]} v{draft["versao"]} já está em revisão: decida-a antes de abrir '
                      'outra (uma por vez).')
    current = phase(state)
    if current != 'minutas':
        raise Refusal(f'não há minuta a abrir na fase "{current}". {next_action(state, folder, current)}')
    item = queue(state)[0]
    if args.id and args.id.upper() != item['id']:
        raise Refusal(f'a próxima da fila é {item["id"]}: as minutas seguem a ordem IMP e depois ESC, por número.')
    draft = item['minuta']
    draft.update(status='em_revisao', versao=draft['versao'] + 1, sha256=None, evidencia=None, quando=stamp())
    log(state, 'minuta_abrir', f'{item["id"]} v{draft["versao"]}')
    return (f'Minuta {item["id"]} v{draft["versao"]} aberta: escreva {draft_path(folder, item["id"])} e registre com '
            f'"minuta --id {item["id"]} --acao registrar".')


def register_draft(state, folder, item):
    path = draft_path(folder, item['id'])
    if not path.is_file():
        raise Refusal(f'{path} não existe: escreva a minuta antes de registrar.')
    if not path.read_bytes().strip():
        raise Refusal(f'{path} está vazio: escreva a minuta antes de registrar.')
    draft = item['minuta']
    draft['sha256'] = sha256_file(path)
    log(state, 'minuta_registrar', f'{item["id"]} v{draft["versao"]} ({draft["sha256"][:12]})')
    return (f'Minuta {item["id"]} v{draft["versao"]} registrada: apresente-a com o checklist de auditoria e peça a '
            'decisão (aprovo / ajuste: ... / descarto).')


def decide_draft(state, folder, item, action, text):
    draft, path = item['minuta'], draft_path(folder, item['id'])
    version = draft['versao']
    if not draft['sha256']:
        raise Refusal(f'a minuta {item["id"]} v{version} ainda não foi registrada: rode "minuta --id {item["id"]} '
                      '--acao registrar" e apresente-a antes de pedir a decisão.')
    if not matches(folder, item):
        raise Refusal(f'{path} mudou (ou sumiu) depois do registro: registre de novo e apresente a versão atual '
                      'antes de pedir a decisão.')
    evidence = check_evidence(text, action, item['id'])
    entry = {'versao': version, 'acao': action, 'evidencia': evidence, 'sha256': draft['sha256'], 'quando': stamp()}
    draft['historico'].append(entry)
    if action == 'aprovar':
        draft.update(status='aprovada', evidencia=evidence, quando=entry['quando'])
        message = f'Minuta {item["id"]} v{version} aprovada.'
    elif action == 'ajustar':
        entry['arquivo'] = archive(folder, item['id'], version)
        draft.update(versao=version + 1, sha256=None, evidencia=None, quando=entry['quando'])
        message = (f'Ajuste registrado: a v{version} foi para {entry["arquivo"]}. Escreva a v{version + 1} em {path} '
                   'aplicando o ajuste e registre de novo.')
    else:
        entry['arquivo'] = archive(folder, item['id'], version)
        draft.update(status='descartada', evidencia=evidence, quando=entry['quando'])
        message = f'Minuta {item["id"]} v{version} descartada (arquivo em {entry["arquivo"]}).'
    log(state, f'minuta_{action}', f'{item["id"]} v{version}: "{evidence}"')
    return message


def cmd_draft(state, folder, args):
    require_gate(state)
    if args.acao == 'abrir':
        return open_draft(state, folder, args)
    if not args.id:
        raise Refusal('informe --id com a minuta em revisão.')
    item = current_review(state, args.id.upper())
    if args.acao == 'registrar':
        return register_draft(state, folder, item)
    return decide_draft(state, folder, item, args.acao, args.evidencia)


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


def find_model(assets, kind):
    found = sorted(path for path in Path(assets).glob(f'modelo-{kind}.*') if path.is_file())
    return str(found[0]) if found else None


def piece_check(state, folder, assets):
    pending = []
    if not gate_open(state):
        pending.append('portão documental não resolvido')
    elif state['itens_registrados_em'] is None:
        pending.append('levantamento não registrado')
    pending += [f'{item_id}: decisão pendente' for item_id in ids_with(state, 'pendente')]
    for item in queue(state):
        draft = item['minuta']
        opened = draft['status'] == 'em_revisao'
        pending.append(f'{item["id"]}: minuta em revisão (v{draft["versao"]})' if opened
                       else f'{item["id"]}: minuta ainda não aberta')
    pending += [f'{item["id"]}: minuta alterada ou removida depois de aprovada'
                for item in approved(state) if not matches(folder, item)]
    by_kind = {kind: [approval(item) for item in approved(state, kind)] for kind in KINDS.values()}
    if not any(by_kind.values()):
        pending.append('nenhuma minuta aprovada')
    return {'pronto': not pending, 'pendencias': pending, 'aprovadas_por_tipo': by_kind,
            'modelos': {kind: find_model(assets, kind) for kind in KINDS.values()}, 'confirmadas': state['peca']}


def confirm_piece(state, folder, args):
    if not args.tipo or not args.formato:
        raise Refusal('informe --tipo impugnacao|esclarecimento e --formato unico|por_ponto.')
    label, check = KIND_LABEL[args.tipo], piece_check(state, folder, args.assets)
    if not check['pronto']:
        raise Refusal('a peça ainda não pode ser confirmada; pendências: ' + '; '.join(check['pendencias']) + '.')
    approvals = check['aprovadas_por_tipo'][args.tipo]
    if not approvals:
        raise Refusal(f'não há minuta de {label} aprovada: não há peça de {label} a confirmar.')
    model = check['modelos'][args.tipo]
    if not model:
        raise Refusal(f'não há modelo de {label} em {args.assets} (modelo-{args.tipo}.*): a peça final só sai quando '
                      'o modelo existir (fase futura). Informe o analista e pare aqui; não gere a peça por outro meio.')
    evidence = check_evidence(args.evidencia, 'confirmar')
    state['peca'][args.tipo] = {'formato': args.formato, 'evidencia': evidence, 'quando': stamp(),
                                'modelo': Path(model).name, 'aprovadas': approvals}
    ids = ', '.join(entry['id'] for entry in approvals)
    log(state, 'peca_confirmar', f'{label} ({args.formato}) com {ids}: "{evidence}"')
    return (f'Peça de {label} confirmada ({args.formato}) com {ids}. Este script não gera o PDF; '
            'não assine, não protocole, não envie.')


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


def changing(change):
    """Carrega o estado sob a trava da pasta, aplica a mudança, grava estado.json e registro.md e devolve o status."""
    def handler(args):
        folder = located(args.pasta)
        state_file(folder)
        with locked(folder):
            state = load(folder)
            restore(folder, state)
            message = change(state, folder, args)
            save(folder, state)
        return {'mensagem': message, **status(state, folder, args.manifesto)}
    return handler


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


def cmd_piece(args):
    if args.acao == 'confirmar':
        return changing(confirm_piece)(args)
    folder = located(args.pasta)
    return piece_check(load(folder), folder, args.assets)


def cmd_validate(args):
    found = violations(located(args.pasta))
    print(json.dumps({'valido': not found, 'violacoes': found}, ensure_ascii=False, indent=2))
    if found:
        print(f'erro: {len(found)} violação(ões) de invariante.', file=sys.stderr)
        return 1
    return 0


def certame_args(parser):
    parser.add_argument('--orgao', required=True, help='órgão ou ente (ex.: "Secretaria de Saúde de X")')
    parser.add_argument('--modalidade', required=True, help='modalidade (ex.: PE, CC)')
    parser.add_argument('--numero', required=True, help='número do certame')
    parser.add_argument('--ano', required=True, help='ano com 4 dígitos')


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='comando', required=True, metavar='COMANDO')
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--manifesto', type=Path, default=DEFAULT_MANIFEST, help='MANIFEST.json do estudo')
    folder = argparse.ArgumentParser(add_help=False, parents=[common])
    folder.add_argument('--pasta', type=Path, required=True, help='pasta do edital')

    p = sub.add_parser('slug', help='imprime o slug da pasta do edital')
    certame_args(p)
    p.set_defaults(handler=cmd_slug)
    p = sub.add_parser('iniciar', parents=[common], help='cria a pasta do edital')
    certame_args(p)
    p.add_argument('--raiz', type=Path, required=True, help='pasta onde ficam as triagens')
    p.add_argument('--esfera', choices=SPHERES)
    p.add_argument('--slug', help='slug próprio (padrão: orgao-modalidade-numero-ano)')
    p.set_defaults(handler=cmd_init)
    p = sub.add_parser('status', parents=[folder], help='fase, próxima ação e alertas')
    p.set_defaults(handler=cmd_status)
    p = sub.add_parser('documentos', parents=[folder], help='registra o portão documental')
    p.add_argument('--presentes', default='', help=f'códigos separados por vírgula: {",".join(DOC_CODES)}')
    p.add_argument('--faltas', default='', help='códigos que faltam, separados por vírgula')
    p.add_argument('--reri', choices=RERI_VALUES)
    p.add_argument('--esfera', choices=SPHERES)
    p.set_defaults(handler=changing(cmd_documents))
    p = sub.add_parser('prosseguir', parents=[folder], help='registra a decisão de seguir sem os documentos que faltam')
    p.add_argument('--evidencia', required=True, help='frase literal do analista')
    p.set_defaults(handler=changing(cmd_proceed))
    p = sub.add_parser('prazo', parents=[folder], help='guarda o JSON de "prazo.py --json"')
    p.add_argument('--dados', required=True, help='arquivo JSON ou - para ler da entrada padrão')
    p.set_defaults(handler=changing(cmd_deadline))
    p = sub.add_parser('itens', parents=[folder], help='registra (ou acrescenta) os itens do levantamento')
    p.add_argument('--arquivo', required=True, help='JSON com a lista de {id, classe, titulo} (ou -)')
    p.set_defaults(handler=changing(cmd_items))
    p = sub.add_parser('decidir', parents=[folder], help='registra a seleção do analista')
    p.add_argument('--ids', required=True, help='IDs separados por vírgula ou PENDENTES')
    p.add_argument('--decisao', required=True, choices=DECISIONS)
    p.add_argument('--evidencia', required=True, help='frase literal do analista')
    p.set_defaults(handler=changing(cmd_decide))
    p = sub.add_parser('minuta', parents=[folder], help='abre, registra e decide a minuta em revisão')
    p.add_argument('--acao', required=True, choices=('abrir', 'registrar', 'aprovar', 'ajustar', 'descartar'))
    p.add_argument('--id', help='ID da minuta em revisão')
    p.add_argument('--evidencia', help='frase literal do analista (aprovar, ajustar, descartar)')
    p.set_defaults(handler=changing(cmd_draft))
    p = sub.add_parser('reabrir', parents=[folder], help='volta itens para a seleção')
    p.add_argument('--ids', required=True, help='IDs separados por vírgula')
    p.add_argument('--motivo', required=True)
    p.set_defaults(handler=changing(cmd_reopen))
    p = sub.add_parser('peca', parents=[folder], help='verifica ou confirma a peça final (não gera PDF)')
    p.add_argument('--acao', required=True, choices=('verificar', 'confirmar'))
    p.add_argument('--tipo', choices=tuple(KINDS.values()))
    p.add_argument('--formato', choices=('unico', 'por_ponto'))
    p.add_argument('--evidencia', help='frase literal do analista')
    p.add_argument('--assets', type=Path, default=DEFAULT_ASSETS, help='pasta dos modelos da peça')
    p.set_defaults(handler=cmd_piece)
    p = sub.add_parser('validar', parents=[folder], help='confere os invariantes; sai com 1 se houver violação')
    p.set_defaults(handler=cmd_validate)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        outcome = args.handler(args)
    except Refusal as exc:
        print(f'erro: {exc}', file=sys.stderr)
        return 1
    except OSError as exc:
        target = exc.filename or 'um arquivo da triagem'
        print(f'erro: não foi possível ler ou gravar {target}: {exc.strerror or exc}. Confira o caminho e as '
              'permissões e rode de novo.', file=sys.stderr)
        return 1
    if isinstance(outcome, dict):
        print(json.dumps(outcome, ensure_ascii=False, indent=2))
        return 0
    return outcome


if __name__ == '__main__':
    sys.exit(main())
