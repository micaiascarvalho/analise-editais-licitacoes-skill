# Pipeline local e fontes oficiais

## O que está implementado

`scripts/pipeline.py` indexa PDFs textuais (com `pypdf`), DOCX (XML, inclusive tabelas) e TXT/MD em SQLite FTS5; coleta páginas da API oficial de acórdãos; pesquisa por corpus com BM25 e retorna texto e proveniência. Documentos do edital e exemplos são corpora separados. Não usa o arquivo `chroma.sqlite3` existente nem envia documentos para serviços de embeddings.

A combinação de fontes é automatizada na busca; a avaliação contextual e jurídica é feita pelo agente seguindo o SKILL.md. Não há motor vetorial, OCR automático, atualização agendada ou importação CSV nesta versão. Cabeçalhos, rodapés e notas de DOCX não entram no índice: conferir no documento original quando relevantes. PDFs sem texto geram avisos por página e exigem OCR/leitura visual antes de concluir a análise.

O script não baixa o inteiro teor dos acórdãos: guarda os links devolvidos pelo TCU para consulta pelo agente. Os resultados do catálogo são candidatos, não precedentes validados.

## Fontes verificadas em 28/09/2026

- [Documentação da API](https://sites.tcu.gov.br/dados-abertos/webservices-tcu/): `GET https://dados-abertos.apps.tcu.gov.br/api/acordao/recupera-acordaos?inicio=0&quantidade=20`. `inicio` é deslocamento, não número da página. A documentação consultada não oferece filtro textual nesse endpoint.
- [Bases para download](https://sites.tcu.gov.br/dados-abertos/jurisprudencia/): acórdãos, jurisprudência selecionada, publicações, súmulas e respostas a consultas. A API de acórdãos não equivale às cinco bases.
- [Dicionário de dados](https://sites.tcu.gov.br/dados-abertos/jurisprudencia/dicionario-dados.html): diferencia sumário, relatório, voto, decisão, enunciado, excerto e visão geral gerada por IA.
- [Pesquisa oficial](https://pesquisa.apps.tcu.gov.br/): descoberta e conferência complementar.
- [Lei 14.133/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm): conferir o texto e alterações aplicáveis na data da análise.

Uma consulta real de dois registros confirmou o endpoint e o campo `urlArquivoPdf`, cuja capitalização difere de `urlArquivoPDF` na documentação. O adaptador aceita ambos. A API devolveu metadados e sumário, não voto e relatório integrais.

## Comandos

Execute com Python 3; para PDFs é necessário `pypdf`. No Codex desktop, obtenha o Python pelo carregador de dependências. Os caminhos abaixo são relativos à pasta da skill; escolha um banco próprio da análise, nunca um banco preexistente de outro sistema.

```bash
python3 scripts/pipeline.py --db /tmp/analise-tcu.sqlite ingest --corpus edital /caminho/edital.pdf /caminho/tr.docx
python3 scripts/pipeline.py --db /tmp/analise-tcu.sqlite ingest --corpus exemplo /caminho/impugnacao.docx
python3 scripts/pipeline.py --db /tmp/analise-tcu.sqlite sync-tcu --start 0 --page-size 20 --pages 2
python3 scripts/pipeline.py --db /tmp/analise-tcu.sqlite search 'parcelamento limpeza habilitação' --corpus todos --limit 5
python3 scripts/pipeline.py --db /tmp/analise-tcu.sqlite status
```

`todos` pesquisa os três corpora e reserva até `limit` resultados por corpus, para não deixar a quantidade de acórdãos ocultar cláusulas do edital. A consulta combina os termos por OR; use consultas curtas, variantes e leitura contextual para avaliar resultados. O score é relevância lexical, não força jurídica.

Os caminhos absolutos, SHA-256 e localizadores permitem conferir o texto. Reindexar o mesmo caminho substitui seus trechos no corpus escolhido; use bancos separados por certame para evitar mistura de versões e clientes. Ao trocar um arquivo de caminho, o anterior continua indexado: crie banco novo para uma versão limpa.

## Paginação, cobertura e falhas

Coleta limitada por execução, sem alegar carga integral. Cada página é validada e gravada em transação; erro preserva páginas anteriores e encerra com código de falha. Duplicatas são atualizadas por chave oficial. Página repetida ou sem novas chaves no mesmo lote interrompe com erro para evitar laço. Resposta vazia marca fim observado; limite de páginas marca apenas limite atingido. O próximo deslocamento é informativo: a API não documenta snapshot ou ordenação estável, portanto não garante continuidade sem lacunas entre execuções. Revarrer faixas sobrepostas e deduplicar é necessário numa sincronização de produção.

Cada página coletada guarda deslocamento, quantidade, horário e URL. A resposta do comando informa a condição de parada; preserve essa resposta junto ao relatório se precisar auditar a execução. O status mostra contagens e as últimas 20 páginas coletadas; não certifica cobertura integral. Não concluir “não existe jurisprudência” a partir da busca local. Sem conexão, pesquisar o cache e declarar sua data/limites; complementar nas fontes oficiais disponíveis.

Uma evolução para carga histórica e busca vetorial deve adicionar importação dos CSVs oficiais, coleta de inteiros teores, controle de versões e atualização, embeddings com modelo definido e testes de recuperação. Embeddings de documentos da empresa em provedor externo dependem de escolha explícita do destino. Não é necessário para usar a skill inicial.
