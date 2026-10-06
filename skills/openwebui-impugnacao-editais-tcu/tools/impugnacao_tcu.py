"""
title: Impugnacao Editais TCU
description: Indexa anexos próprios por certame e pesquisa evidências e catálogo parcial do TCU.
author: Local
version: 1.0.1
requirements: pypdf==6.10.0
"""
import asyncio
import inspect
import os
import tempfile
from contextlib import closing
from typing import Optional, List
from pydantic import BaseModel, Field

import hashlib
import json
import re
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

API = 'https://dados-abertos.apps.tcu.gov.br/api/acordao/recupera-acordaos'
CORPORA = ('edital', 'exemplo', 'tcu')


def now():
    return datetime.now(timezone.utc).isoformat()


def connect(path):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    # Refuse unrelated SQLite databases rather than attempting migrations.
    tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if tables and 'impugnacao_meta' not in tables:
        db.close()
        raise ValueError('Banco de outro sistema; escolha um arquivo novo.')
    db.executescript('''
        CREATE TABLE IF NOT EXISTS impugnacao_meta(version INTEGER NOT NULL);
        INSERT INTO impugnacao_meta SELECT 1 WHERE NOT EXISTS(SELECT 1 FROM impugnacao_meta);
        CREATE VIRTUAL TABLE IF NOT EXISTS evidence USING fts5(
            body, uid UNINDEXED, corpus UNINDEXED, source UNINDEXED,
            locator UNINDEXED, metadata UNINDEXED, tokenize='unicode61 remove_diacritics 2');
        CREATE TABLE IF NOT EXISTS collection(
            at TEXT, start INTEGER, requested INTEGER, received INTEGER, source TEXT);
    ''')
    return db


def put(db, uid, corpus, source, locator, body, metadata):
    db.execute('DELETE FROM evidence WHERE uid=?', (uid,))
    db.execute('INSERT INTO evidence VALUES (?,?,?,?,?,?)',
               (body, uid, corpus, source, locator, json.dumps(metadata, ensure_ascii=False)))


def pieces(text, size=6000):
    # No overlap: source locators plus part numbers allow deterministic reconstruction.
    return [text[i:i + size] for i in range(0, len(text), size)]


def extract(path):
    suffix = path.suffix.lower()
    if suffix == '.pdf':
        from pypdf import PdfReader
        for number, page in enumerate(PdfReader(str(path)).pages, 1):
            yield f'página PDF {number}', page.extract_text() or ''
    elif suffix == '.docx':
        with ZipFile(path) as archive:
            root = ET.fromstring(archive.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        for number, para in enumerate(root.findall('.//w:body//w:p', ns), 1):
            text = ''.join(n.text or '' for n in para.findall('.//w:t', ns))
            if text.strip():
                yield f'parágrafo XML {number} (página não verificada)', text
    elif suffix in ('.txt', '.md'):
        for number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
            if line.strip():
                yield f'linha {number}', line
    else:
        raise ValueError(f'Formato não suportado: {suffix}')


def ingest(db, filename, corpus):
    path = Path(filename).resolve(strict=True)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    units = list(extract(path))  # Extract successfully before replacing an older version.
    warnings = [f'{loc}: sem texto; requer inspeção/OCR' for loc, text in units if not text.strip()]
    if not any(text.strip() for _, text in units):
        raise ValueError(f'{path.name}: nenhum texto extraído; requer inspeção/OCR')
    count = 0
    with db:
        db.execute('DELETE FROM evidence WHERE source=? AND corpus=?', (str(path), corpus))
        for locator, text in units:
            for part, body in enumerate(pieces(text), 1):
                if not body.strip():
                    continue
                count += 1
                uid = hashlib.sha256(f'{corpus}:{path}:{locator}:{part}'.encode()).hexdigest()
                put(db, uid, corpus, str(path), f'{locator}, trecho {part}', body,
                    {'sha256': digest, 'indexed_at': now(), 'kind': 'documento',
                     'legal_status': 'não avaliado'})
    return {'source': str(path), 'chunks': count, 'warnings': warnings}


def fetch_page(start, quantity):
    url = API + '?' + urllib.parse.urlencode({'inicio': start, 'quantidade': quantity})
    request = urllib.request.Request(url, headers={'User-Agent': 'edital-tcu-local/1.0'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                data = response.read(20_000_001)
            if len(data) > 20_000_000:
                raise ValueError('Resposta excedeu limite de 20 MB por página.')
            result = json.loads(data)
            if not isinstance(result, list) or len(result) > quantity:
                raise ValueError('Contrato da API alterado: esperada lista paginada.')
            for record in result:
                if not isinstance(record, dict) or not isinstance(record.get('key'), str) or not record['key']:
                    raise ValueError('Registro sem chave oficial válida.')
            return result, url
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
        time.sleep(2 ** attempt)


def sync(db, start, quantity, pages, fetch=None):
    fetch = fetch or fetch_page
    seen = set()
    received = 0
    offset = start
    stop = 'limite de páginas; cobertura parcial'
    for _ in range(pages):
        records, url = fetch(offset, quantity)
        keys = {r['key'] for r in records}
        if records and not (keys - seen):
            raise ValueError(f'Paginação repetida no deslocamento {offset}; coleta interrompida.')
        with db:
            for record in records:
                meta = dict(record)
                meta.update({'collected_at': now(), 'kind': 'sumario_api',
                             'legal_status': 'candidato; inteiro teor não conferido',
                             'pdf_url': record.get('urlArquivoPdf') or record.get('urlArquivoPDF')})
                text = '\n'.join(str(record.get(key) or '') for key in
                                 ('titulo', 'sumario', 'relator', 'colegiado'))
                put(db, 'tcu:' + record['key'], 'tcu', record.get('urlAcordao') or url,
                    record.get('titulo') or record['key'], text, meta)
            db.execute('INSERT INTO collection VALUES (?,?,?,?,?)',
                       (now(), offset, quantity, len(records), url))
        seen.update(keys)
        received += len(records)
        offset += len(records)
        if not records:
            stop = 'fim observado nesta consulta; completude histórica não garantida'
            break
    return {'received': received, 'unique_keys_in_run': len(seen),
            'next_offset': offset, 'stop': stop}


def search(db, query, corpus, limit):
    tokens = re.findall(r'[^\W_]+', query, flags=re.UNICODE)
    if not tokens:
        raise ValueError('Consulta sem termos pesquisáveis.')
    match = ' OR '.join('"' + token + '"' for token in tokens[:40])
    result = {}
    for group in CORPORA if corpus == 'todos' else (corpus,):
        rows = db.execute('''SELECT body,source,locator,metadata,bm25(evidence) AS score
            FROM evidence WHERE evidence MATCH ? AND corpus=?
            ORDER BY score LIMIT ?''', (match, group, limit))
        result[group] = [dict(row) | {'metadata': json.loads(row['metadata'])} for row in rows]
    return {'query': query, 'method': 'lexical FTS5/BM25; termos OR',
            'warning': 'Resultados candidatos; busca local parcial não demonstra ausência de jurisprudência.',
            'results': result}


def status(db):
    return {'counts': [dict(r) for r in db.execute(
        'SELECT corpus,count(*) AS chunks,count(DISTINCT source) AS sources FROM evidence GROUP BY corpus')],
        'recent_pages': [dict(r) for r in db.execute('SELECT * FROM collection ORDER BY rowid DESC LIMIT 20')],
        'coverage': 'Apenas documentos e páginas efetivamente indexados; sem garantia de completude.'}



def user_id(user):
    value = (user or {}).get('id')
    if not isinstance(value, str) or not value:
        raise ValueError('Usuário autenticado não recebido pelo Open WebUI.')
    return value


def database_path(tool, user, certame):
    owner = user_id(user)
    if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]{0,79}', certame):
        raise ValueError('certame_id: use 1 a 80 letras, números, hífen ou sublinhado.')
    if tool.valves.DATA_DIR:
        root = Path(tool.valves.DATA_DIR)
    else:
        from open_webui.env import DATA_DIR
        root = Path(DATA_DIR) / 'impugnacao_tcu'
    root = root.expanduser().resolve()
    folder = root / hashlib.sha256(owner.encode()).hexdigest()
    folder.mkdir(parents=True, exist_ok=True, mode=0o700)
    return folder / (certame + '.sqlite3')


def attached_ids(files):
    found = []
    for item in files or []:
        if not isinstance(item, dict) or item.get('type') not in (None, 'file'):
            continue
        nested = item.get('file') or {}
        value = item.get('id') or (nested.get('id') if isinstance(nested, dict) else None)
        if isinstance(value, str) and value and value not in found:
            found.append(value)
    return found


async def owned_file(file_id, owner):
    from open_webui.models.files import Files
    # Current Open WebUI uses async DB methods; accept earlier sync methods too.
    method = Files.get_file_by_id
    if inspect.iscoroutinefunction(method):
        item = await method(file_id)
    else:
        item = await asyncio.to_thread(method, file_id)
    if not item or item.user_id != owner:
        raise ValueError('Arquivo indisponível ou não pertence ao usuário atual.')
    return item


def ingest_upload(path, record, db_path, corpus, maximum):
    source = Path(path)
    if not source.is_file() or source.stat().st_size > maximum:
        raise ValueError('Arquivo inexistente ou acima do limite configurado.')
    suffix = Path(record.filename).suffix.lower()
    if suffix not in ('.pdf', '.docx', '.txt', '.md'):
        raise ValueError('Use PDF textual, DOCX, TXT ou MD.')
    raw = source.read_bytes()
    if len(raw) > maximum:
        raise ValueError('Arquivo acima do limite configurado.')
    if suffix == '.docx':
        import io
        with ZipFile(io.BytesIO(raw)) as z:
            if sum(i.file_size for i in z.infolist()) > maximum * 5:
                raise ValueError('DOCX descompactado acima do limite.')
    with tempfile.TemporaryDirectory() as tmp:
        local = Path(tmp) / ('documento' + suffix)
        local.write_bytes(raw)
        units = list(extract(local))
    if sum(len(body) for _, body in units) > 10_000_000:
        raise ValueError('Texto extraído acima de 10 milhões de caracteres.')
    warnings = [loc + ': sem texto; exige OCR/inspeção' for loc, body in units if not body.strip()]
    if suffix == '.docx':
        warnings.append('DOCX: cabeçalhos, rodapés e notas não indexados; estrutura de tabelas não preservada; conferir original.')
    if not any(body.strip() for _, body in units):
        raise ValueError('Nenhum texto extraído; requer OCR/inspeção. Índice anterior preservado.')
    label = 'arquivo:' + record.id
    meta = {'file_id': record.id, 'filename': record.filename,
            'sha256': hashlib.sha256(raw).hexdigest(), 'indexed_at': now(),
            'kind': 'documento', 'legal_status': 'não avaliado', 'warnings': warnings}
    count = 0
    with closing(connect(db_path)) as db:
        with db:
            db.execute('DELETE FROM evidence WHERE source=? AND corpus=?', (label, corpus))
            for locator, body in units:
                for part, chunk in enumerate(pieces(body), 1):
                    if not chunk.strip():
                        continue
                    count += 1
                    put(db, f'{corpus}:{record.id}:{count}', corpus, label,
                        f'{locator}, trecho {part}', chunk, meta)
    return {'file_id': record.id, 'filename': record.filename, 'chunks': count,
            'warnings': warnings, 'sha256': meta['sha256']}


def db_operation(path, operation, *args):
    with closing(connect(path)) as db:
        return operation(db, *args)


def inventory(db):
    result = status(db)
    result['documents'] = [dict(row) | {'metadata': json.loads(row['metadata'])}
        for row in db.execute("SELECT corpus,source,metadata,count(*) AS chunks FROM evidence WHERE corpus != 'tcu' GROUP BY corpus,source")]
    return result


def read_chunks(db, file_id, corpus, start, limit):
    source = 'arquivo:' + file_id
    total = db.execute('SELECT count(*) FROM evidence WHERE source=? AND corpus=?', (source, corpus)).fetchone()[0]
    if not total:
        raise ValueError('Arquivo não indexado neste certame/corpus.')
    rows = db.execute('SELECT body,locator,metadata FROM evidence WHERE source=? AND corpus=? ORDER BY rowid LIMIT ? OFFSET ?',
                      (source, corpus, limit, start)).fetchall()
    end = start + len(rows)
    return {'file_id': file_id, 'inicio': start, 'total_trechos': total,
            'proximo_inicio': end, 'fim': end >= total,
            'trechos': [dict(r) | {'metadata': json.loads(r['metadata'])} for r in rows]}


class Tools:
    class Valves(BaseModel):
        DATA_DIR: str = Field(default='', description='Diretório persistente. Vazio: DATA_DIR do Open WebUI/impugnacao_tcu.')
        MAX_FILE_MB: int = Field(default=25, ge=1, le=100, description='Tamanho máximo por anexo.')
        TCU_ENABLED: bool = Field(default=True, description='Permitir consulta pública à API oficial do TCU.')

    def __init__(self):
        self.valves = self.Valves()

    async def listar_anexos(self, __files__: Optional[list] = None, __user__: Optional[dict] = None) -> dict:
        """Lista IDs e nomes dos anexos próprios acessíveis nesta conversa para indexação."""
        try:
            owner = user_id(__user__)
            result = []
            for fid in attached_ids(__files__):
                try:
                    item = await owned_file(fid, owner)
                    result.append({'id': item.id, 'nome': item.filename, 'ok': True})
                except ValueError as exc:
                    result.append({'id': fid, 'ok': False, 'erro': str(exc)})
            return {'ok': True, 'anexos': result, 'aviso': 'Somente uploads próprios. Anexe arquivos se a lista estiver vazia.'}
        except Exception as exc:
            return {'ok': False, 'erro': str(exc)}

    async def indexar_anexos(self, certame_id: str, arquivo_ids: List[str], corpus: str = 'edital',
                             __files__: Optional[list] = None, __user__: Optional[dict] = None) -> dict:
        """Indexa anexos próprios selecionados. Retorna cobertura, hashes e avisos; não valida juridicamente.
        :param certame_id: Identificador estável do certame e versão.
        :param arquivo_ids: IDs retornados por listar_anexos; máximo 20.
        :param corpus: edital ou exemplo.
        """
        try:
            owner = user_id(__user__)
            path = database_path(self, __user__, certame_id)
            if corpus not in ('edital', 'exemplo'):
                raise ValueError('corpus deve ser edital ou exemplo.')
            ids = list(dict.fromkeys(arquivo_ids))
            if not 1 <= len(ids) <= 20 or not set(ids).issubset(attached_ids(__files__)):
                raise ValueError('Selecione de 1 a 20 IDs presentes nos anexos desta conversa.')
            from open_webui.storage.provider import Storage
            result = []
            for fid in ids:
                try:
                    item = await owned_file(fid, owner)
                    if not item.path:
                        raise ValueError('Upload original indisponível; reanexe o arquivo.')
                    local = await asyncio.to_thread(Storage.get_file, item.path)
                    value = await asyncio.to_thread(ingest_upload, local, item, path, corpus,
                                                    self.valves.MAX_FILE_MB * 1024 * 1024)
                    result.append({'ok': True, **value})
                except Exception as exc:
                    result.append({'ok': False, 'file_id': fid, 'erro': str(exc)})
            return {'ok': all(x['ok'] for x in result), 'certame_id': certame_id, 'resultados': result,
                    'aviso': 'Falhas não apagam versões anteriores. Novo upload recebe novo ID; use novo certame_id para versão limpa.'}
        except Exception as exc:
            return {'ok': False, 'erro': str(exc)}

    async def pesquisar_evidencias(self, certame_id: str, consulta: str, corpus: str = 'todos', limite: int = 5,
                                   __user__: Optional[dict] = None) -> dict:
        """Busca lexical de candidatos no índice do usuário/certame. Não substitui leitura integral ou pesquisa oficial.
        :param certame_id: Identificador usado na indexação.
        :param consulta: Palavras ou variantes do tema procurado.
        :param corpus: todos, edital, exemplo ou tcu.
        :param limite: De 1 a 10 resultados por corpus.
        """
        try:
            if corpus not in (*CORPORA, 'todos') or not 1 <= limite <= 10:
                raise ValueError('Corpus inválido ou limite fora de 1 a 10.')
            result = await asyncio.to_thread(db_operation, database_path(self, __user__, certame_id), search, consulta, corpus, limite)
            return {'ok': True, **result}
        except Exception as exc:
            return {'ok': False, 'erro': str(exc)}

    async def ler_documento(self, certame_id: str, arquivo_id: str, inicio: int = 0, limite: int = 5,
                            corpus: str = 'edital', __user__: Optional[dict] = None) -> dict:
        """Lê sequencialmente os trechos indexados; avance proximo_inicio até fim=true. Não confirma fidelidade visual.
        :param certame_id: Identificador usado na indexação.
        :param arquivo_id: ID do arquivo indexado, consultável no status.
        :param inicio: Deslocamento inicial, começando em zero.
        :param limite: De 1 a 10 trechos por chamada.
        :param corpus: edital ou exemplo.
        """
        try:
            if inicio < 0 or not 1 <= limite <= 10 or corpus not in ('edital', 'exemplo'):
                raise ValueError('Paginação ou corpus inválido.')
            result = await asyncio.to_thread(db_operation, database_path(self, __user__, certame_id), read_chunks,
                                             arquivo_id, corpus, inicio, limite)
            return {'ok': True, **result}
        except Exception as exc:
            return {'ok': False, 'erro': str(exc)}

    async def consultar_status(self, certame_id: str, __user__: Optional[dict] = None) -> dict:
        """Mostra inventário e limites da cobertura local do usuário/certame, sem certificar completude."""
        try:
            result = await asyncio.to_thread(db_operation, database_path(self, __user__, certame_id), inventory)
            return {'ok': True, 'certame_id': certame_id, **result}
        except Exception as exc:
            return {'ok': False, 'erro': str(exc)}

    async def coletar_acordaos_tcu(self, certame_id: str, inicio: int = 0, quantidade: int = 20, paginas: int = 1,
                                   __user__: Optional[dict] = None) -> dict:
        """Coleta amostra paginada do catálogo TCU, sem filtro temático nem inteiro teor. Não é busca por assunto.
        :param certame_id: Identificador do certame cujo catálogo será alimentado.
        :param inicio: Deslocamento na API, a partir de zero.
        :param quantidade: Registros por página, de 1 a 100.
        :param paginas: Páginas por chamada, de 1 a 3.
        """
        try:
            if not self.valves.TCU_ENABLED:
                raise ValueError('Coleta TCU desativada nas Valves.')
            if inicio < 0 or not 1 <= quantidade <= 100 or not 1 <= paginas <= 3:
                raise ValueError('Use inicio >= 0, quantidade 1..100 e paginas 1..3.')
            result = await asyncio.to_thread(db_operation, database_path(self, __user__, certame_id), sync,
                                             inicio, quantidade, paginas)
            return {'ok': True, **result}
        except Exception as exc:
            return {'ok': False, 'erro': str(exc), 'aviso': 'Páginas já gravadas foram preservadas. Confira consultar_status antes de repetir.'}
