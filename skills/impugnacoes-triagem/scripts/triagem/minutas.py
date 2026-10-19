"""Comando "minuta": uma minuta em revisão por vez (abrir, registrar, aprovar, ajustar, descartar)."""
from .arquivos import archive, draft_path, matches
from .comum import Refusal, log, sha256_file, stamp
from .evidencia import check_evidence
from .fases import in_review, next_action, phase, queue, require_gate


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
