# Contexto da Sessão — Auditoria e Mapeamento de Fontes

Esta pasta reúne o necessário para continuar o trabalho em outro computador (ou em outra sessão do Claude Code) sem depender do histórico da conversa.

## 1. O que foi feito (sessão de 2026-10-14)

1. **Pedido inicial:** mapear, para o Edital e cada anexo, as fontes internas e externas a consultar para decidir o que impugnar.
2. **Auditoria prévia:** antes do mapeamento, os 14 arquivos `Estrutura`/`Analise` de `briefing/Mapeamento_Analise/` foram auditados. Resultado: 107 pontos (31 Alta, 38 Média, 28 Baixa, 10 Melhoria), com justificativa, fonte e sugestão — ver `Relatorio_Auditoria_107_pontos.md`.
   - A Lei 14.133/2021 foi conferida artigo por artigo no texto do Planalto.
   - Súmulas e acórdãos foram conferidos só em fontes secundárias; quatro citações não foram localizadas (Acórdãos 1.182/2020 e 2.380/2013, REsp 1.733.688/SC, Nota Técnica SEI 2.012/2020).
3. **Correções aplicadas (todas as gravidades):**
   - `c29449b` — Alta e Média
   - `eb6431e` — Melhorias
   - `837df5f` — Baixa
4. **Mapeamento de fontes em 6 fases:** plano em `briefing/Mapeamento_Analise/02 - Plano do Mapeamento de Fontes.md` (commit `6bfc323`).
   - Fase 1 (catálogo `01 - Catalogo de Fontes.md`): concluída, commit `1d04c47`. `conferido` só para artigos da Lei 14.133 conferidos no Planalto.
   - Fase 2 (`Edital/Fontes - Edital.md`): concluída, commit `4f29ecb` (13 seções; arts. 14, 15 e 90 entraram no catálogo como `a conferir`).
   - Fase 3 (`Fontes - Termo de Referencia.md` e `Fontes - ETP.md`): concluída. Feita por workflow (rascunho, revisão por 4 lentes, correção, simetria TR x ETP, catálogo e revisão final). Entraram no catálogo os arts. 16, 117 e 140 da Lei 14.133 (conferidos), a Súmula 281 do TCU e as NR-15 e NR-16 (a conferir). Os ajustes de simetria no mapa do Edital ficaram registrados na seção 7 do plano, para a Fase 6.
   - Fase 4 (`Fontes - Planilha de Custos.md` e `Fontes - Pesquisa de Precos.md`): concluída. Planilha com os 6 módulos e os submódulos 2.1 a 2.3, 4.1 e 4.2, mais a seção 7 (planilha como um todo); Pesquisa com os 5 parâmetros, validade, tratamento matemático, cruzamentos no processo e os 5 vícios. Nenhuma fonte nova; siglas PL-F e PP-F no catálogo. Aviso prévio só por `EXT-TCU-AC1186-2017`. Ajustes de simetria e a divergência do catálogo sobre o aviso prévio ficaram na seção 7 do plano.
   - Fase 5 (`Fontes - Minuta Contratual.md` e `Fontes - RERI.md`): concluída. Minuta com as 9 cláusulas (focos da Análise; cláusulas 1, 6 e 9 derivadas da Estrutura); RERI com os 3 atos, os 5 checkpoints do loop e o modelo da tabela de controle dinâmico. Entraram no catálogo os arts. 157 e 158 da Lei 14.133 (conferidos no Planalto); siglas MC-F e RR-F. Ajustes de simetria na seção 7.2 do plano.
   - Fase 6 (consolidação): concluída. As 20 pendências da seção 7 do plano foram conferidas e aplicadas ou decididas. O resultado está na seção 7.3 do plano. As maiores mudanças foram a simetria do mapa do Edital, a citação uniforme `INT-EDITAL (seção N)` e as cláusulas da Minuta nas matrizes. Foram criadas voltas no TR, no ETP, na Planilha e na Pesquisa. A coluna "Usado em" do catálogo foi recalculada por script, e o `00 - Objetivos_Organizacao.md` passou a listar os mapas, o catálogo e o plano. A verificação por script (IDs, seções, simetria, citação por extenso, "Usado em") está na seção 8 do plano.
   - **Mapeamento concluído.** Os 7 mapas e o catálogo estão prontos para uso na análise de editais.

## 2. Decisões que valem para as próximas fases

- Um `Fontes - {Documento}.md` por pasta; catálogo único na raiz.
- Fontes externas citadas nos mapas **só por ID** do catálogo (nada de lei hardcoded no mapa — ver `Minhas observacoes.md`).
- Status `conferido` / `a conferir`; campo **esfera** (federal/estadual/municipal) para normas como IN SEGES 5/2017, 65/2021, 73/2022 e Lei 9.784/1999.
- Foco da Servfaz: serviços com dedicação exclusiva de mão de obra (repactuação, art. 63 §1º, art. 121 §3º, CCT).
- Sem dados pessoais (PII) nas saídas; grafia "Servfaz".
- Uma fase por sessão, terminando com commit e atualização da tabela "Andamento".

## 3. Pendências conhecidas (não cobertas pela auditoria)

O que ficou "a conferir" ou para decidir depois do mapeamento:

- **Aviso prévio nas prorrogações:** decidir se o 0,83% (`EXT-MGI-NT35883`, `EXT-TCU-AC58-2026`, ambos conferidos) volta aos arquivos de estudo e ao mapa da Planilha, que hoje seguem só o `EXT-TCU-AC1186-2017`, ou se as duas fontes vão para "Não usar" (catálogo, observação 7).
- **Arquivos de estudo desatualizados em relação ao catálogo** (itens 14 e 19 do plano; a Fase 6 não os alterou). Ainda marcam como "a conferir" ou "fonte secundária" fontes já conferidas: Súmula 254 e Lei 14.973/2024 na Estrutura da Planilha; esclarecimento do MEC na Análise da Planilha; IN 65/2021 e Acórdão 1.445/2015 na Análise da Pesquisa; arts. 141 e 22 na Estrutura da Minuta; Acórdãos 2.032/2021, 2.078/2014 e 930/2008 na Análise da RERI. A Estrutura da Minuta não cita os arts. 157 e 158 na defesa prévia (7.2). A Estrutura da RERI diz "a localizar" para o efeito vinculante do esclarecimento, já resolvido por `EXT-TCU-AC915-2009`. Os módulos 4.1-D e 4.1-E (acidente e maternidade) não têm fonte no catálogo.
- **Fontes `a conferir` no catálogo:** `EXT-PEND-ATESTPRIV` (sem acórdão; a tese fica só com a lei), `EXT-BASE-NFE`, `EXT-BASE-PAINELCONTRAT`, `EXT-IN5-2014` e as que dependem do ente, da categoria ou do objeto (`EXT-REG-ENTE`, `EXT-NORMA-CCT`, `EXT-ISS-MUNICIPAL`, normas ABNT, INMETRO, ANVISA, ANATEL, conselhos, CFC, NR-17, modelos da AGU, Diário Oficial, site do órgão, TJ). Lista completa na seção 9.2 do catálogo.

- "jurisprudência pacífica do TCU", sem acórdão, na Análise da Minuta (seção de reajuste).
- "ou anular a fase preparatória" no fecho da Análise do ETP.
- Fechos de tom promocional ("tese perfeita de impugnação", "um passo à frente") nas Análises da Minuta e da RERI.
- Confirmar no portal do TCU/STF as fontes `a conferir` antes de usar em peça.

## 4. Como retomar em outro computador

1. `git pull` deste repositório.
2. (Opcional) Restaurar a memória do Claude Code: copie os arquivos de `memoria/` para `~/.claude/projects/<pasta-do-projeto>/memory/` (o nome da pasta é o caminho do repositório com `/` trocado por `-`).
3. Abra o Claude Code na raiz do repositório e peça, por exemplo:
   > Leia `briefing/Contexto_Sessao/README.md` e `briefing/Mapeamento_Analise/02 - Plano do Mapeamento de Fontes.md` e execute a próxima fase pendente.

## 5. Arquivos desta pasta

| Arquivo | Conteúdo |
| :-- | :-- |
| `README.md` | Este resumo. |
| `Relatorio_Auditoria_107_pontos.md` | Relatório completo da auditoria (IDs, gravidade, justificativa, fontes consultadas). |
| `memoria/` | Cópia das memórias do Claude Code deste projeto (referência PNCP/base legal, checklist dos 6 documentos, mapeamento em fases). |
