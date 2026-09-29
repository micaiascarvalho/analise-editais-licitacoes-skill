#!/usr/bin/env python3
"""Local evidence index and bounded public TCU catalogue collector. Python 3.10+."""
import argparse
import hashlib
import json
import re
import sqlite3
import sys
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


def sync(db, start, quantity, pages, fetch=fetch_page):
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


def positive(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError('Deve ser positivo.')
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', required=True)
    commands = parser.add_subparsers(dest='command', required=True)
    doc = commands.add_parser('ingest')
    doc.add_argument('--corpus', choices=('edital', 'exemplo'), required=True)
    doc.add_argument('files', nargs='+')
    tcu = commands.add_parser('sync-tcu')
    tcu.add_argument('--start', type=int, default=0)
    tcu.add_argument('--page-size', type=positive, default=20)
    tcu.add_argument('--pages', type=positive, default=1)
    lookup = commands.add_parser('search')
    lookup.add_argument('query')
    lookup.add_argument('--corpus', choices=(*CORPORA, 'todos'), default='todos')
    lookup.add_argument('--limit', type=positive, default=5)
    commands.add_parser('status')
    args = parser.parse_args()
    if args.command == 'sync-tcu' and (args.start < 0 or args.page_size > 100 or args.pages > 100):
        parser.error('Use início >= 0, page-size <= 100 e pages <= 100 por execução.')
    try:
        db = connect(args.db)
        try:
            if args.command == 'ingest':
                result = [ingest(db, f, args.corpus) for f in args.files]
            elif args.command == 'sync-tcu':
                result = sync(db, args.start, args.page_size, args.pages)
            elif args.command == 'search':
                result = search(db, args.query, args.corpus, args.limit)
            else:
                result = status(db)
            print(json.dumps(result, ensure_ascii=False, indent=2))
        finally:
            db.close()
    except Exception as exc:
        print(json.dumps({'error': str(exc), 'type': type(exc).__name__,
                          'note': 'Nenhuma validação jurídica inferida; operações anteriores podem estar salvas.'},
                         ensure_ascii=False), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
