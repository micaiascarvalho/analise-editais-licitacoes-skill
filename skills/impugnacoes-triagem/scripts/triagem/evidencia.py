"""Evidência do analista: frases genéricas, lote, negação, condição e aprovação de uma minuta por vez."""
import re

from .comum import Refusal, canonical_id, clauses, id_number, plain

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
    'reabrir': 'peça ao analista o motivo da reabertura (por exemplo: o que o fez mudar de ideia sobre o item)',
    'confirmar': 'liste as versões aprovadas e peça ao analista a confirmação explícita da peça',
}


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
