import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from docx import Document
from docx.oxml.ns import qn

import gerar_minuta
from gerar_minuta import Refusal, STYLES

# Dados fictícios.
MINUTA = '''---
tipo: impugnacao
---

**ILUSTRÍSSIMO SENHOR PREGOEIRO DA SECRETARIA MUNICIPAL DE EXEMPLÓPOLIS.**

**Referente:** Pregão Eletrônico nº 1/2026.

# DA TEMPESTIVIDADE

Texto com **negrito** e _itálico_.

# DOS PONTOS IMPUGNADOS

**III.1 – CAPITAL E PATRIMÔNIO CUMULATIVOS**

| # | Cláusula impugnada | Vício |
| :-- | :-- | :-- |
| III.1 | Item 8.6.3 | Cumulação vedada |

> “Trecho literal do edital.”

# DOS PEDIDOS

1. o **CONHECIMENTO** da impugnação;
1. o **PROVIMENTO** do pedido;

2. a retificação do item;
2. a republicação do edital;

<!-- centralizado -->
Teresina, 9 de setembro de 2026.
<!-- /centralizado -->

Fulano de Tal
Sócio Administrador
'''


class GerarMinutaTests(unittest.TestCase):
    def convert(self, text, name='minuta.md'):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        source = Path(self.tmp.name) / name
        source.write_text(text, encoding='utf-8')
        return source, Document(str(gerar_minuta.convert(source)))

    def test_conventions(self):
        source, doc = self.convert(MINUTA)
        self.assertEqual(source.with_suffix('.docx').name, 'minuta.docx')
        styles = [p.style.name for p in doc.paragraphs]
        texts = [p.text for p in doc.paragraphs]
        self.assertEqual(sum(1 for s in styles if s == STYLES['titulo']), 3)
        self.assertIn(STYLES['subtitulo'], styles)
        self.assertIn(STYLES['citacao'], styles)
        self.assertIn(STYLES['centro'], styles)
        self.assertEqual(doc.tables[0].cell(0, 1).text, 'Cláusula impugnada')
        self.assertFalse(any('**' in t or '---' in t for t in texts))
        body = next(p for p in doc.paragraphs if p.text.startswith('Texto com'))
        self.assertEqual([(r.text, r.bold, r.italic) for r in body.runs if r.bold or r.italic],
                         [('negrito', True, None), ('itálico', None, True)])
        self.assertTrue(doc.sections[0].header.paragraphs or doc.sections[0].header.tables)

    def test_lists_restart_and_close_with_period(self):
        _, doc = self.convert(MINUTA)
        alineas = [p for p in doc.paragraphs if p.style.name == STYLES['alinea']]
        lists = [p._p.pPr.find(qn('w:numPr')).find(qn('w:numId')).get(qn('w:val')) for p in alineas]
        self.assertEqual(len(set(lists)), 2)  # cada lista recomeça em a)
        self.assertTrue(alineas[1].text.endswith('.'), alineas[1].text)
        self.assertTrue(alineas[3].text.endswith('.'), alineas[3].text)

    def test_signature_block_has_no_space_between_lines(self):
        _, doc = self.convert(MINUTA)
        name = next(p for p in doc.paragraphs if p.text == 'Fulano de Tal')
        self.assertEqual(name.paragraph_format.space_after.pt, 0)

    def test_refuses_unfilled_or_internal(self):
        for text in ('Texto {{CAMPO}}.\n', 'Fonte [EXT-LEI14133-ART5 · conferido].\n', 'Ver catálogo de fontes.\n'):
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'minuta.md'
                path.write_text(text, encoding='utf-8')
                with self.assertRaises(Refusal):
                    gerar_minuta.convert(path)
                self.assertFalse(path.with_suffix('.docx').exists())

    def test_catalog_of_services_is_allowed(self):
        self.convert('O Catálogo de Serviços do órgão não prevê o item.\n')

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'minuta.md'
            source.write_text(MINUTA, encoding='utf-8')
            target = Path(tmp) / 'saida.docx'
            with redirect_stdout(io.StringIO()):
                self.assertEqual(gerar_minuta.main([str(source), '--saida', str(target)]), 0)
            self.assertTrue(target.is_file())
            source.write_text('{{CAMPO}}\n', encoding='utf-8')
            with redirect_stderr(io.StringIO()) as err:
                self.assertEqual(gerar_minuta.main([str(source)]), 1)
            self.assertIn('linha 1', err.getvalue())
            with redirect_stderr(io.StringIO()):
                self.assertEqual(gerar_minuta.main([str(Path(tmp) / 'nao-existe.md')]), 1)


# Markdown comum, como sai de um gerador de chat (dados fictícios).
COMUM = '''**ILUSTRÍSSIMO SENHOR PREGOEIRO.**

## IMPUGNAÇÃO AO EDITAL

---

### I. DA TEMPESTIVIDADE

Texto com *itálico* simples.

#### 1. Do primeiro ponto

> *"Trecho literal do edital."* [fonte]

Verifica-se que:
1. primeiro;
2. segundo;

### IV. DOS PEDIDOS

1. O **CONHECIMENTO** da impugnação;
2. No mérito, o **ACOLHIMENTO**, para que:
   - **a)** A exclusão do item 1;
   - **b)** A adequação do item 2;
3. A republicação do edital;

- solto um;
- solto dois;
'''


class MarkdownComumTests(unittest.TestCase):
    convert = GerarMinutaTests.convert

    def test_common_markdown(self):
        _, doc = self.convert(COMUM)
        rows = [(p.style.name, p.text) for p in doc.paragraphs]
        titles = [t for s, t in rows if s == STYLES['titulo']]
        self.assertEqual(titles, ['DA TEMPESTIVIDADE', 'DOS PEDIDOS'])  # "I." digitado sai: a numeração é automática
        self.assertIn((STYLES['centro'], 'IMPUGNAÇÃO AO EDITAL'), rows)
        self.assertIn((STYLES['subtitulo'], '1. Do primeiro ponto'), rows)
        self.assertTrue(all('---' not in t and '#' not in t and '*' not in t for _, t in rows))
        italic = next(p for p in doc.paragraphs if p.text.startswith('Texto com'))
        self.assertEqual([r.text for r in italic.runs if r.italic], ['itálico'])

    def test_nested_items_stay_in_one_list(self):
        _, doc = self.convert(COMUM)
        alineas = [p for p in doc.paragraphs if p.style.name == STYLES['alinea']]
        numbered = [p for p in alineas if p._p.pPr.find(qn('w:numPr')) is not None]
        merits = [p for p in numbered if p.text.startswith(('O CONHECIMENTO', 'No mérito', 'A republicação'))]
        ids = {p._p.pPr.find(qn('w:numPr')).find(qn('w:numId')).get(qn('w:val')) for p in merits}
        self.assertEqual(len(merits), 3)
        self.assertEqual(len(ids), 1)  # a republicação é c), não recomeça em a)
        subs = [p for p in alineas if p.text.startswith(('a) A exclusão', 'b) A adequação'))]
        self.assertEqual(len(subs), 2)
        self.assertTrue(all(p.paragraph_format.left_indent > p.style.paragraph_format.left_indent for p in subs))
        self.assertTrue(subs[1].text.endswith(';'))  # o ponto final vai ao último item da lista, não ao sub-item
        self.assertTrue(merits[2].text.endswith('.'))

    def test_loose_bullets_become_numbered(self):
        _, doc = self.convert(COMUM)
        loose = [p for p in doc.paragraphs if p.text.startswith('solto')]
        self.assertTrue(all(p._p.pPr.find(qn('w:numPr')) is not None for p in loose))
        self.assertTrue(loose[-1].text.endswith('.'))

    def test_refuses_blank_fields_citations_and_unsupported_markup(self):
        cases = {'CNPJ [Inserir CNPJ].': 'Inserir CNPJ', 'Protocolo em [Data do Protocolo].': 'Data do Protocolo',
                 'Conforme o edital [1].': '[1]', 'Ver [2, 3].': '[2, 3]', '```\ncódigo\n```': '```',
                 '![logo](a.png)': '![logo]', 'Veja [o edital](http://x.br).': 'o edital', 'Linha<br>quebra': '<br>',
                 '##### Subtítulo fundo': '#####', 'Texto ~~riscado~~.': '~~'}
        for text, found in cases.items():
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'minuta.md'
                path.write_text(text + '\n', encoding='utf-8')
                with self.assertRaisesRegex(Refusal, found.replace('[', r'\[').replace('(', r'\(')):
                    gerar_minuta.convert(path)
                self.assertFalse(path.with_suffix('.docx').exists(), text)

    def test_legal_text_with_brackets_and_comparisons_is_allowed(self):
        self.convert('Índice [sic] inferior a 1,0 e valor < 10 ou > 5; art. 67, § 2º.\n')


if __name__ == '__main__':
    unittest.main()
