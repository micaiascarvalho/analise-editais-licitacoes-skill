"""Peça final: verificação, confirmação e invalidação da confirmação (este script não gera PDF)."""
from pathlib import Path

from .arquivos import matches
from .comum import KIND_LABEL, KINDS, Refusal, log, stamp
from .evidencia import check_evidence
from .fases import approval, approved, gate_open, ids_with, queue
from .persistencia import changing, load, located


def invalidate_piece(state, kind, reason):
    if state['peca'].get(kind):
        state['peca'][kind] = None
        log(state, 'peca_invalidada', f'confirmação da peça de {KIND_LABEL[kind]} desfeita: {reason}')


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


def cmd_piece(args):
    if args.acao == 'confirmar':
        return changing(confirm_piece)(args)
    folder = located(args.pasta)
    return piece_check(load(folder), folder, args.assets)
