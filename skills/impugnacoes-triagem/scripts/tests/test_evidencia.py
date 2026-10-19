import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from triagem.comum import Refusal
from triagem.evidencia import check_evidence


class EvidenciaTests(unittest.TestCase):
    def assert_evidence(self, accepted, refused):
        for action, phrase, extra in accepted:
            with self.subTest(aceita=phrase, action=action):
                check_evidence(phrase, action, **extra)
        for action, phrase, extra in refused:
            with self.subTest(recusa=phrase, action=action), self.assertRaises(Refusal):
                check_evidence(phrase, action, **extra)

    def test_discard_evidence_refuses_negation_and_unrelated_words(self):
        item = {'item_id': 'IMP-20'}
        self.assert_evidence(
            accepted=[('descartar', phrase, item) for phrase in (
                'Descarto, não vale a pena', 'não vale a pena, descarta', 'tira esse', 'pode tirar',
                'não usar este ponto', 'pode excluir', 'não é exclusivo, então descarta', 'retirar o ponto')],
            refused=[('descartar', phrase, item) for phrase in (
                'não descarte essa, aprovo', 'não quero tirar', 'não retire esse ponto', 'tiragem', 'atira')])

    def test_batch_and_other_item_approvals_refused(self):
        item = {'item_id': 'IMP-20'}
        self.assert_evidence(
            accepted=[('aprovar', phrase, item) for phrase in (
                'Aprovo.', 'aprovado', 'aprovo a v2', 'Aprovo a IMP-20', 'aprovo a imp 20', 'Aprovo sem ressalvas',
                'No geral ficou bom, aprovo')],
            refused=[('aprovar', phrase, item) for phrase in (
                'aprovo ambas', 'aprovo as duas', 'aprovo em bloco', 'aprova geral, manda o PDF', 'aprovo as minutas',
                'aprovo esta e as próximas', 'aprovo o restante', 'minutas aprovadas', 'aprovo a IMP 02',
                'aprovo a imp02', 'aprovo a IMP-2', 'aprovo o esclarecimento 1', 'aprovo a impugnação 3')])

    def test_negative_and_conditional_evidence_refused(self):
        item = {'item_id': 'IMP-20'}
        self.assert_evidence(
            accepted=[
                ('prosseguir', 'Não tenho o ETP, segue', {}),
                ('prosseguir', 'Sem problema, prossiga sem o ETP', {}),
                ('decidir', 'não incluir a IMP-20', {'decision': 'descartar'}),
                ('decidir', 'deixa os dois para depois', {'decision': 'avaliar_depois'}),
                ('confirmar', 'Confirmo, pode gerar', {}),
                ('aprovar', 'Aprovo. Qual a próxima?', item),
                ('aprovar', 'Aprovo, se puder já abre a próxima', item),
                ('ajustar', 'ajuste: não cite o acórdão, use a lei', item),
            ],
            refused=[
                ('prosseguir', 'não', {}),
                ('prosseguir', 'não prossiga, vou mandar o ETP', {}),
                ('decidir', 'não incluir a IMP-20', {'decision': 'incluir'}),
                ('decidir', 'ainda não', {'decision': 'avaliar_depois'}),
                ('confirmar', 'não confirmo ainda', {}),
                ('confirmar', 'ainda não', {}),
                ('ajustar', 'não, ainda não', item),
            ] + [('aprovar', phrase, item) for phrase in (
                'Antes de aprovar, ajuste o fundamento do pedido', 'Aprovo, mas troque o fundamento',
                'aprovaria se corrigir', 'não sei se aprovo', 'ainda não dá para aprovar', 'nunca aprovaria isso',
                'aprovo? não', 'aprovo desde que corrija a página')])


if __name__ == '__main__':
    unittest.main()
