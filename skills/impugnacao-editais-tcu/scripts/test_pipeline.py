import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from pipeline import connect, ingest, search, sync


def record(key, pdf_key='urlArquivoPdf'):
    return {'key': key, 'titulo': 'Acórdão de teste', 'sumario': 'Parcelamento de serviços',
            'urlAcordao': 'https://example.invalid/' + key, pdf_key: 'https://example.invalid/a.pdf'}


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.db = connect(':memory:')

    def tearDown(self):
        self.db.close()

    def test_reindex_replaces_old_text_and_keeps_corpora_distinct(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / 'edital.txt'
            file.write_text('Garantia contratual', encoding='utf-8')
            ingest(self.db, file, 'edital')
            ingest(self.db, file, 'exemplo')
            file.write_text('Parcelamento justificado', encoding='utf-8')
            ingest(self.db, file, 'edital')
            result = search(self.db, 'garantia', 'todos', 5)['results']
            self.assertFalse(result['edital'])
            self.assertEqual(len(result['exemplo']), 1)

    def test_dedup_and_pdf_aliases(self):
        for field in ('urlArquivoPdf', 'urlArquivoPDF'):
            sync(self.db, 0, 1, 1, lambda *_: ([record('a', field)], 'test'))
        rows = search(self.db, 'parcelamento', 'tcu', 5)['results']['tcu']
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0]['metadata']['pdf_url'])
        self.assertIn('não conferido', rows[0]['metadata']['legal_status'])

    def test_offsets_and_empty_page(self):
        offsets = []
        def fetch(start, size):
            offsets.append(start)
            return ([record(str(start))] if start < 2 else []), 'test'
        result = sync(self.db, 0, 1, 5, fetch)
        self.assertEqual(offsets, [0, 1, 2])
        self.assertEqual(result['received'], 2)
        self.assertIn('fim observado', result['stop'])

    def test_repeated_page_stops_and_preserves_completed_page(self):
        with self.assertRaisesRegex(ValueError, 'repetida'):
            sync(self.db, 0, 1, 2, lambda *_: ([record('a')], 'test'))
        self.assertEqual(self.db.execute('SELECT count(*) FROM evidence').fetchone()[0], 1)

    def test_network_failure_does_not_erase_saved_page(self):
        def fetch(start, size):
            if start:
                raise TimeoutError('indisponível')
            return [record('a')], 'test'
        with self.assertRaises(TimeoutError):
            sync(self.db, 0, 1, 2, fetch)
        self.assertEqual(self.db.execute('SELECT count(*) FROM collection').fetchone()[0], 1)

    def test_docx_table_text_has_honest_locator(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / 'test.docx'
            xml = '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:tbl><w:tr><w:tc><w:p><w:r><w:t>Garantia</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:body></w:document>'
            with ZipFile(file, 'w') as archive:
                archive.writestr('word/document.xml', xml)
            ingest(self.db, file, 'edital')
            rows = search(self.db, 'garantia', 'edital', 5)['results']['edital']
            self.assertIn('página não verificada', rows[0]['locator'])

    def test_literal_search_handles_punctuation_and_accents(self):
        sync(self.db, 0, 1, 1, lambda *_: ([record('a')], 'test'))
        self.assertTrue(search(self.db, 'servicos " OR ()', 'tcu', 5)['results']['tcu'])
        with self.assertRaises(ValueError):
            search(self.db, '"()', 'todos', 5)

    def test_foreign_database_is_rejected(self):
        import sqlite3
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'other.sqlite'
            with sqlite3.connect(path) as other:
                other.execute('CREATE TABLE unrelated(x)')
            with self.assertRaisesRegex(ValueError, 'outro sistema'):
                connect(path)


if __name__ == '__main__':
    unittest.main()
