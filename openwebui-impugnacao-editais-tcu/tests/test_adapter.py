import asyncio
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import impugnacao_tcu as mod


class AdapterTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.tool = mod.Tools()
        self.tool.valves.DATA_DIR = self.tmp.name
        self.user = {'id': 'alice'}
        self.source = Path(self.tmp.name) / 'upload.txt'
        self.source.write_text('Execução por 12 meses.\nGarantia contratual.\nTerceira linha.')
        self.item = types.SimpleNamespace(id='file1', user_id='alice', filename='edital.txt', path=str(self.source))
        self.files = [{'type': 'file', 'file': {'id': 'file1'}}]
        async def get(fid):
            return self.item if fid == self.item.id else None
        fm = types.ModuleType('open_webui.models.files')
        fm.Files = types.SimpleNamespace(get_file_by_id=get)
        sm = types.ModuleType('open_webui.storage.provider')
        sm.Storage = types.SimpleNamespace(get_file=lambda path: path)
        self.patcher = patch.dict(sys.modules, {'open_webui.models.files': fm, 'open_webui.storage.provider': sm})
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    async def index(self):
        return await self.tool.indexar_anexos('teste', ['file1'], __files__=self.files, __user__=self.user)

    def test_frontmatter_requirements_are_valid_after_openwebui_split(self):
        import ast
        from packaging.requirements import Requirement
        header = ast.get_docstring(ast.parse(Path(mod.__file__).read_text()))
        value = next(line.split(':', 1)[1].strip() for line in header.splitlines()
                     if line.startswith('requirements:'))
        requirements = [Requirement(part.strip()) for part in value.split(',')]
        self.assertEqual(len(requirements), 1)
        self.assertEqual(requirements[0].name, 'pypdf')
        import pypdf
        self.assertIn(pypdf.__version__, requirements[0].specifier)

    async def test_upload_read_search_and_persist(self):
        self.assertTrue((await self.index())['ok'])
        first = await self.tool.ler_documento('teste', 'file1', limite=1, __user__=self.user)
        self.assertFalse(first['fim'])
        second = await self.tool.ler_documento('teste', 'file1', inicio=first['proximo_inicio'], __user__=self.user)
        self.assertTrue(second['fim'])
        new = mod.Tools()
        new.valves.DATA_DIR = self.tmp.name
        result = await new.pesquisar_evidencias('teste', 'garantia', __user__=self.user)
        self.assertEqual(len(result['results']['edital']), 1)
        self.assertEqual(result['results']['edital'][0]['source'], 'arquivo:file1')

    async def test_user_and_case_isolation(self):
        await self.index()
        for user, case in [({'id': 'bob'}, 'teste'), (self.user, 'outro')]:
            result = await self.tool.pesquisar_evidencias(case, 'garantia', __user__=user)
            self.assertFalse(result['results']['edital'])

    async def test_foreign_and_unattached_files_denied(self):
        self.assertFalse((await self.tool.indexar_anexos('teste', ['file1'], __files__=self.files, __user__={'id':'bob'}))['ok'])
        self.assertFalse((await self.tool.indexar_anexos('teste', ['file1'], __files__=[], __user__=self.user))['ok'])
        self.assertFalse((await self.tool.consultar_status('teste'))['ok'])

    async def test_traversal_and_invalid_corpus_denied(self):
        self.assertFalse((await self.tool.consultar_status('../escape', __user__=self.user))['ok'])
        self.assertFalse((await self.tool.pesquisar_evidencias('teste', 'x', corpus='SQL', __user__=self.user))['ok'])

    async def test_reindex_and_empty_failure_preserves_previous(self):
        await self.index()
        self.source.write_text('Parcelamento')
        await self.index()
        self.assertFalse((await self.tool.pesquisar_evidencias('teste', 'garantia', __user__=self.user))['results']['edital'])
        self.source.write_text('')
        self.assertFalse((await self.index())['ok'])
        self.assertTrue((await self.tool.pesquisar_evidencias('teste', 'parcelamento', __user__=self.user))['results']['edital'])

    async def test_pdf_page_without_text(self):
        from pypdf import PdfWriter
        writer = PdfWriter()
        writer.add_blank_page(width=100, height=100)
        writer.write(self.source)
        self.item.filename = 'scan.pdf'
        result = await self.index()
        self.assertFalse(result['ok'])
        self.assertIn('OCR', result['resultados'][0]['erro'])

    async def test_sync_file_api_supported(self):
        sys.modules['open_webui.models.files'].Files.get_file_by_id = lambda fid: self.item
        result = await self.tool.listar_anexos(__files__=self.files, __user__=self.user)
        self.assertEqual(result['anexos'][0]['nome'], 'edital.txt')

    async def test_tcu_limits_and_mock_collection(self):
        self.assertFalse((await self.tool.coletar_acordaos_tcu('teste', paginas=4, __user__=self.user))['ok'])
        with patch.object(mod, 'fetch_page', return_value=([{'key':'a','titulo':'Teste','sumario':'Parcelamento'}], 'https://example.invalid')):
            collected = await self.tool.coletar_acordaos_tcu('teste', quantidade=1, paginas=1, __user__=self.user)
            self.assertTrue(collected['ok'])
            self.assertEqual(collected['received'], 1)
        result = await self.tool.pesquisar_evidencias('teste', 'parcelamento', corpus='tcu', __user__=self.user)
        self.assertIn('não conferido', result['results']['tcu'][0]['metadata']['legal_status'])
        self.tool.valves.TCU_ENABLED = False
        self.assertFalse((await self.tool.coletar_acordaos_tcu('teste', __user__=self.user))['ok'])


if __name__ == '__main__':
    unittest.main()
