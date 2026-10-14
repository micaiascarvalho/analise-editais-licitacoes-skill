---
name: pncp-api-e-base-legal-sigilo
description: "Endpoints do PNCP que funcionam via curl e a base legal verificada (Lei 14.133 arts. 13, 18, 24, 25, 54) sobre orçamento sigiloso e publicidade dos documentos da fase preparatória"
metadata:
  node_type: memory
  type: reference
  originSessionId: 75992c45-fa9d-4fbc-a62e-2cef04caa42a
  modified: 2026-10-14T18:48:28.432Z
---

**PNCP (sem login, via curl/python; no zsh use python ou bash, pois `$var` não separa palavras):**
- Achar a compra: `GET https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=AAAAMMDD&dataFinal=...&codigoModalidadeContratacao=6&cnpj=<CNPJ>&pagina=1&tamanhoPagina=50` (6 = pregão eletrônico; olhar `numeroCompra` e `processo`; pagina até achar).
- Detalhe da compra: `https://pncp.gov.br/api/consulta/v1/orgaos/<cnpj>/compras/<ano>/<seq>` (campos `orcamentoSigilosoCodigo`, `valorTotalEstimado`, `valorTotalHomologado`, `situacaoCompraNome`).
- Itens e arquivos: `https://pncp.gov.br/api/pncp/v1/orgaos/<cnpj>/compras/<ano>/<seq>/itens` e `/arquivos`.
- O CBM-DF publica sob o CNPJ do Fundo Constitucional do DF (05448380000145), não do CBMDF.

**Base legal conferida no texto do Planalto e no Guia do TCU (licitacoesecontratos.tcu.gov.br, item 4.5.6):** art. 13 (atos públicos; publicidade diferida do orçamento), art. 18 (ETP, TR, orçamento com composições, minuta anexa obrigatória), art. 24 (sigilo só se justificado; quantitativos e dados para propostas continuam públicos; não vale para controle), art. 25 §3º (todos os anexos do edital divulgados no mesmo dia), art. 54 caput e §3º (anexos no PNCP; documentos da fase preparatória que não integraram o edital vão ao PNCP após a homologação). Acórdão 232/2022-Plenário (conforme o Guia): orçamento sigiloso não impede publicar o ETP, só as partes sigilosas.

**Onde achar documentos além do PNCP (verificado em 2026-10-14):**
- Compras.gov.br público: `https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/quadro-informativo?compra=<idCompra>` (avisos, impugnações e respostas, esclarecimentos; abre sem captcha). `idCompra` = UASG(6)+modalidade(05)+número(5)+ano; o campo `linkSistemaOrigem` do PNCP traz o link certo (a UASG do FMS no PNCP é 927337, o edital imprime 977337).
- Site do órgão: o CBM-DF publica as planilhas de custo (Anexos II a XVI) numa página própria do PE (`cbm.df.gov.br/lai/...pe-no-90099-2025...`); o FMS publica edital, esclarecimentos e impugnações em `site.fms.pmt.pi.gov.br/page_generic?id=8`.
- SEI Pesquisa Pública (São Luís e GDF existem; São Luís tem captcha que não posso resolver): só mostra documentos marcados como públicos.
- Pedido formal: LAI (Lei 12.527 arts. 10, 11 e 15: 20 dias +10, recurso em 10 dias; art. 7º §3º limita documentos preparatórios até o ato decisório) e representação ao tribunal de contas (Lei 14.133 art. 170 §4º).
- O edital da SEMED chama a pesquisa de preços de "Mapa de Apuração de Preço, que consta no processo"; o ETP da Prefeitura de São Luís lista a "Pesquisa de Preços" como Anexo II do próprio ETP.

**Why:** evita refazer a pesquisa quando o usuário perguntar o que é público ou onde achar anexos.

**How to apply:** conferir se o texto da lei mudou antes de citar em peça; o código verificador+CRC do SEI só abre o próprio documento, não o processo. Relacionado: [[checklist-seis-documentos-impugnacao]].
