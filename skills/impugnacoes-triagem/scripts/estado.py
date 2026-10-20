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
  estado.py documentos --pasta DIR --presentes EDITAL,TR --faltas ETP,PLANILHA,PESQUISA,MINUTA
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
import json
import sys
from pathlib import Path

from triagem.comandos import (cmd_decide, cmd_deadline, cmd_documents, cmd_init, cmd_items, cmd_proceed, cmd_reopen,
                              cmd_slug, cmd_status)
from triagem.comum import DECISIONS, DOC_CODES, KINDS, SPHERES, Refusal
from triagem.invariantes import cmd_validate
from triagem.minutas import cmd_draft
from triagem.peca import cmd_piece
from triagem.persistencia import changing

SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = SKILL_DIR / 'references' / 'estudo' / 'MANIFEST.json'
DEFAULT_ASSETS = SKILL_DIR / 'assets'


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
    p = sub.add_parser('reabrir', parents=[folder], help='volta itens para a seleção (o analista mudou de ideia)')
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
