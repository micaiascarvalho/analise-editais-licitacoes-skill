# 01 - Catálogo de Fontes

Catálogo único das fontes citadas nos 14 arquivos `Estrutura - *.md` e `Analise - *.md` desta pasta. Os mapas `Fontes - {Documento}.md` (fases 2 a 5) citam as fontes externas **só pelo ID**; o nome, o local de consulta e o status ficam aqui. Quando a lei ou a jurisprudência mudar, atualize este arquivo, não os mapas (ver `Minhas observacoes.md` e `02 - Plano do Mapeamento de Fontes.md`).

## Como ler

**IDs:** `INT-*` para documentos do próprio processo; `EXT-{GRUPO}-{CHAVE}` para fontes externas. A chave `GERAL` indica a norma citada sem artigo específico. Um ID por artigo: os incisos e parágrafos citados vão na coluna Nome.

**Esfera:** `federal (nacional)` para lei ou súmula que vale para todos os entes; `federal (União)` para norma infralegal federal, quando o ente do edital pode ter regulamento próprio (confira o regulamento do ente, `EXT-REG-ENTE`); `estadual` ou `municipal` quando a fonte é do ente.

**Status:**

- `conferido`: texto lido na fonte oficial (Planalto, Pesquisa de Jurisprudência do TCU, portal do STF, TCE/SP, Portal de Compras do Governo Federal) ou, para bases de dados, endereço oficial aberto e funcionando. A última conferência foi em 2026-10-15 (seção 9). Antes de citar em peça, confira se o texto mudou.
- `a conferir`: ainda não lido na fonte oficial, ou com divergência anotada no Nome. A lista do que falta e o motivo estão na seção 9.2.
- `n/a`: fontes internas e prova de mercado, que dependem do caso concreto.

**Usado em (siglas dos arquivos):**

| Sigla | Arquivo |
| :-- | :-- |
| ED-E / ED-A | `Edital/Estrutura - Edital.md` / `Edital/Analise - Edital.md` |
| ETP-E / ETP-A | `Estudo Técnico Preliminar/Estrutura - ETP.md` / `Analise - Estudo tecnico Preliminar.md` |
| TR-E / TR-A | `Termo de Referência/Estrutura - Termo de Refencia.md` / `Analise - Termo de Referencia.md` |
| PL-E / PL-A | `Planilha de Custos/Estrutura - Planilha de Custos.md` / `Analise - Planilha de Custos.md` |
| PP-E / PP-A | `Pesquisa(Mapa) de Preços/Estrutura - Pesquisa de Precos.md` / `Analise - Pesquisa de Precos.md` |
| MC-E / MC-A | `Minuta Contratual/Estrutura - Minuta Contratual.md` / `Analise - Minuta Contratual.md` |
| RR-E / RR-A | `Retificações, Esclarecimentos e Respostas/Estrutura - RERI.md` / `Analise - RERI.md` |
| ED-F | `Edital/Fontes - Edital.md` (só para fontes acrescentadas na fase 2) |
| TR-F | `Termo de Referência/Fontes - Termo de Referencia.md` (fase 3) |
| ETP-F | `Estudo Técnico Preliminar/Fontes - ETP.md` (fase 3) |

---

## 1. Fontes internas

Onde consultar, para todas: arquivos da compra no PNCP (`EXT-BASE-PNCP`), quadro informativo do Compras.gov.br (`EXT-BASE-COMPRASGOV`) ou site do órgão (`EXT-BASE-SITEORGAO`). Documento da fase preparatória que não integrou o edital só vai ao PNCP depois da homologação (`EXT-LEI14133-ART54`); antes disso, o caminho é pedido de esclarecimento ou acesso via LAI (`EXT-LEI12527-GERAL`).

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| INT-EDITAL | Edital da licitação | Documento do processo | do ente licitante | PNCP, Compras.gov.br, site do órgão | todos os 14 arquivos, TR-F, ETP-F | n/a |
| INT-TR | Termo de Referência (ou Projeto Básico, em obras e serviços de engenharia) | Anexo do edital | do ente licitante | PNCP, Compras.gov.br, site do órgão | ED-E, ED-A, ETP-A, TR-E, TR-A, PL-A, PP-E, PP-A, RR-E, RR-A, TR-F, ETP-F | n/a |
| INT-ETP | Estudo Técnico Preliminar | Documento da fase preparatória | do ente licitante | PNCP (se anexo ao edital ou após a homologação); pedido de esclarecimento ou LAI | ED-A, ETP-E, ETP-A, TR-E, TR-A, TR-F, ETP-F | n/a |
| INT-PLANILHA | Planilha de custos e formação de preços (orçamento estimado) | Anexo do edital | do ente licitante | PNCP, site do órgão | ED-A, PL-E, PL-A, TR-A, RR-E, RR-A, TR-F, ETP-F | n/a |
| INT-PESQUISA | Pesquisa de preços / mapa comparativo de cotações | Documento da fase preparatória ou anexo | do ente licitante | PNCP, site do órgão; pedido de esclarecimento se o orçamento for sigiloso | ED-A, ETP-A, TR-E, PP-E, PP-A, TR-F, ETP-F | n/a |
| INT-MINUTA | Minuta do contrato | Anexo do edital | do ente licitante | PNCP, Compras.gov.br, site do órgão | ED-A, ETP-A, MC-E, MC-A, PL-A, RR-E, RR-A, TR-F, ETP-F | n/a |
| INT-RERI | Retificações, esclarecimentos e respostas a impugnações | Atos publicados durante a divulgação | do ente licitante | Quadro informativo do Compras.gov.br, PNCP, Diário Oficial, site do órgão | RR-E, RR-A, TR-F, ETP-F | n/a |
| INT-HIST-CONTRATO | Contrato anterior e histórico de consumo ou execução | Documento do órgão | do ente licitante | Portal da Transparência do órgão (`EXT-BASE-TRANSPARENCIA`), PNCP (contratos anteriores) | ETP-E, ETP-A, TR-F, ETP-F | n/a |
| INT-DOTACAO | Dotação orçamentária e fonte de recursos | Indicação no edital, TR ou processo | do ente licitante | Edital, TR (seção de adequação orçamentária), processo | ED-E, ED-A, TR-E, MC-A, TR-F | n/a |
| INT-PCA | Plano de Contratações Anual (PCA) | Documento de planejamento do órgão | do ente licitante | PNCP (planos de contratação), site do órgão | ETP-E, TR-E, TR-F, ETP-F | n/a |

---

## 2. Legislação

### 2.1 Lei nº 14.133/2021

Onde consultar, para todas: texto compilado no Planalto, `https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm`. Tipo: lei federal de normas gerais. Esfera: federal (nacional).

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-LEI14133-GERAL | Lei 14.133/2021, referência geral (regime jurídico, preâmbulo do edital; capítulo de contratos, arts. 89 a 154) | Lei | federal (nacional) | Planalto | todos os 14 arquivos, TR-F | conferido |
| EXT-LEI14133-ART4 | Art. 4º: aplicação da LC 123/2006 e seus limites | Lei | federal (nacional) | Planalto | ED-E, ED-A | conferido |
| EXT-LEI14133-ART5 | Art. 5º: princípios (razoabilidade, proporcionalidade, julgamento objetivo, segurança jurídica, economicidade, motivação) | Lei | federal (nacional) | Planalto | TR-A, PL-A, PP-A, MC-A, RR-A, TR-F | conferido |
| EXT-LEI14133-ART6 | Art. 6º, XXIII: definição de termo de referência e alíneas "a" a "j" ("i": estimativa do valor com memória de cálculo, em documento separado e classificado; "j": adequação orçamentária). Obrigações das partes não é alínea; vem do modelo da AGU | Lei | federal (nacional) | Planalto | TR-E, TR-A, PL-A, TR-F | conferido |
| EXT-LEI14133-ART9 | Art. 9º, I, "a": vedação a cláusulas que restrinjam a competitividade | Lei | federal (nacional) | Planalto | TR-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART11 | Art. 11, III: objetivo de evitar sobrepreço, preços inexequíveis e superfaturamento | Lei | federal (nacional) | Planalto | PL-A, PP-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART14 | Art. 14: impedimentos para disputar a licitação ou participar da execução do contrato | Lei | federal (nacional) | Planalto | ED-F | conferido |
| EXT-LEI14133-ART15 | Art. 15: participação em consórcio, salvo vedação justificada no processo | Lei | federal (nacional) | Planalto | ED-F, ETP-F | conferido |
| EXT-LEI14133-ART16 | Art. 16: participação de profissionais organizados em cooperativa, condicionada aos incisos I a IV (constituição regular, regime cooperado demonstrado, qualquer cooperado apto a executar; cooperativas da Lei 12.690/2012 só em serviços especializados e complementares) | Lei | federal (nacional) | Planalto | ETP-F | conferido |
| EXT-LEI14133-ART17 | Art. 17, § 3º: amostra na pré-qualificação / fases do processo | Lei | federal (nacional) | Planalto | TR-A, TR-F | conferido |
| EXT-LEI14133-ART18 | Art. 18: fase preparatória (caput: compatibilização com as leis orçamentárias; IV: orçamento com composição de custos; X: análise de riscos); § 1º, I a XIII: elementos do ETP; § 2º: elementos obrigatórios | Lei | federal (nacional) | Planalto | ED-E, ED-A, ETP-E, ETP-A, TR-A, PL-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART22 | Art. 22: matriz de alocação de riscos, facultativa no caput; § 3º: obrigatória em obras e serviços de grande vulto (acima de R$ 200 milhões, art. 6º, XXII) e nos regimes de contratação integrada e semi-integrada | Lei | federal (nacional) | Planalto | MC-E, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART23 | Art. 23: valor estimado (caput: compatível com o mercado, bancos de dados públicos, economia de escala; § 1º, I a V: parâmetros para bens e serviços, prazos de 1 ano e 6 meses; § 2º: obras e serviços de engenharia, SINAPI/SICRO) | Lei | federal (nacional) | Planalto | ED-A, ETP-A, PL-A, PP-E, PP-A, RR-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART24 | Art. 24: orçamento sigiloso (só se justificado; quantitativos e dados da proposta continuam públicos) | Lei | federal (nacional) | Planalto | ED-A, ETP-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART25 | Art. 25: conteúdo do edital (caput); § 3º: anexos divulgados na mesma data, sem cadastro; § 7º: reajuste com data-base do orçamento; § 8º, I e II: reajuste e repactuação | Lei | federal (nacional) | Planalto | ED-E, ED-A, MC-E, MC-A, PL-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART40 | Art. 40: compras (III: quantidades pelo consumo provável; V, "b", e §§ 2º e 3º: parcelamento; § 1º: conteúdo do TR em compras) | Lei | federal (nacional) | Planalto | ED-A, ETP-A, TR-E, TR-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART41 | Art. 41: marca e amostra (I: indicação de marca excepcional; II: amostra na pré-qualificação; parágrafo único: amostra só do provisoriamente vencedor) | Lei | federal (nacional) | Planalto | TR-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART47 | Art. 47, II, e § 1º: parcelamento em serviços | Lei | federal (nacional) | Planalto | ED-A, ETP-A, TR-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART54 | Art. 54, caput e § 3º: publicidade no PNCP; documentos da fase preparatória após a homologação | Lei | federal (nacional) | Planalto | ETP-A, RR-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART55 | Art. 55: prazos mínimos de divulgação (8, 15, 10 e 25 dias úteis); § 1º: alteração que afeta propostas exige nova divulgação e reabertura dos prazos | Lei | federal (nacional) | Planalto | ED-A, PL-A, RR-E, RR-A | conferido |
| EXT-LEI14133-ART57 | Art. 57: intervalo mínimo de diferença entre lances | Lei | federal (nacional) | Planalto | ED-A | conferido |
| EXT-LEI14133-ART59 | Art. 59: desclassificação (III: acima do orçamento estimado; §§ 2º a 4º: exequibilidade) | Lei | federal (nacional) | Planalto | ED-A, PL-A, RR-A, TR-F | conferido |
| EXT-LEI14133-ART60 | Art. 60: critérios de desempate; § 1º: preferências; § 2º: ressalva da LC 123/2006 | Lei | federal (nacional) | Planalto | ED-E | conferido |
| EXT-LEI14133-ART63 | Art. 63: habilitação (§ 1º: declaração de que a proposta cobre os custos trabalhistas; §§ 2º e 3º: vistoria substituível por declaração) | Lei | federal (nacional) | Planalto | ED-A, PL-A, TR-A, TR-F | conferido |
| EXT-LEI14133-ART65 | Art. 65, § 1º: empresa criada no exercício financeiro da licitação atende à habilitação e pode substituir os demonstrativos contábeis pelo balanço de abertura | Lei | federal (nacional) | Planalto | ED-F, TR-F (acrescentada na conferência de 2026-10-15; base de `EXT-PEND-TEMPOEXIST`) | conferido |
| EXT-LEI14133-ART67 | Art. 67: qualificação técnica (§ 1º: parcelas de maior relevância; § 2º: limite de 50% e vedação de tempo e local; § 5º: experiência de até 3 anos em serviços contínuos) | Lei | federal (nacional) | Planalto | ED-A, TR-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART69 | Art. 69: qualificação econômico-financeira (II: certidão negativa de falência; § 5º: vedação de índices não usuais; índices devidamente justificados) | Lei | federal (nacional) | Planalto | ED-A, ETP-F | conferido |
| EXT-LEI14133-ART90 | Art. 90: convocação do adjudicatário para assinar o contrato no prazo e nas condições do edital | Lei | federal (nacional) | Planalto | ED-F | conferido |
| EXT-LEI14133-ART92 | Art. 92: cláusulas necessárias (V: preço, pagamento, reajuste e encargos moratórios; X: prazo de resposta à repactuação; XI: prazo de resposta ao reequilíbrio; § 3º: data-base do reajuste) | Lei | federal (nacional) | Planalto | TR-E, MC-E, MC-A, TR-F | conferido |
| EXT-LEI14133-ART94 | Art. 94: divulgação no PNCP como condição de eficácia (20 dias úteis na licitação; 10 na contratação direta) | Lei | federal (nacional) | Planalto | MC-E | conferido |
| EXT-LEI14133-ART96 | Art. 96, § 1º: escolha da modalidade de garantia pelo contratado (arts. 96 a 102: garantias) | Lei | federal (nacional) | Planalto | ED-A, MC-E, MC-A | conferido |
| EXT-LEI14133-ART98 | Art. 98: garantia de até 5% do valor inicial, até 10% se justificada pela complexidade e pelos riscos; parágrafo único: valor anual em contratos contínuos acima de 1 ano | Lei | federal (nacional) | Planalto | MC-E (sem número de artigo no texto) | conferido |
| EXT-LEI14133-ART99 | Art. 99: em obras e serviços de engenharia de grande vulto, seguro-garantia com cláusula de retomada de até 30% do valor inicial | Lei | federal (nacional) | Planalto | MC-E (sem número de artigo no texto) | conferido |
| EXT-LEI14133-ART102 | Art. 102: em obras e serviços de engenharia, seguro-garantia com cláusula de retomada pela seguradora. O percentual de até 30% em obras de grande vulto está no art. 99 (`EXT-LEI14133-ART99`) | Lei | federal (nacional) | Planalto | MC-E | conferido |
| EXT-LEI14133-ART103 | Art. 103: matriz de alocação de riscos; § 5º: exceções à renúncia de reequilíbrio | Lei | federal (nacional) | Planalto | ETP-A, MC-E, MC-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART106 | Art. 106: vigência inicial de até 5 anos em serviços e fornecimentos contínuos (arts. 105 a 114: duração) | Lei | federal (nacional) | Planalto | TR-E, MC-E, TR-F | conferido |
| EXT-LEI14133-ART107 | Art. 107: prorrogações sucessivas até 10 anos | Lei | federal (nacional) | Planalto | TR-E, MC-E, TR-F | conferido |
| EXT-LEI14133-ART111 | Art. 111: prorrogação automática do contrato por escopo | Lei | federal (nacional) | Planalto | MC-E | conferido |
| EXT-LEI14133-ART117 | Art. 117: execução do contrato acompanhada e fiscalizada por um ou mais fiscais do contrato, representantes da Administração especialmente designados (requisitos do art. 7º), ou por seus substitutos; § 1º: registro das ocorrências pelo fiscal. A divisão em gestor, fiscal técnico e fiscal administrativo não está na lei; vem do regulamento (`EXT-REG-ENTE`) | Lei | federal (nacional) | Planalto | TR-F (acrescentada na fase 3) | conferido |
| EXT-LEI14133-ART118 | Art. 118: preposto | Lei | federal (nacional) | Planalto | TR-A, TR-F | conferido |
| EXT-LEI14133-ART121 | Art. 121, § 3º: garantias trabalhistas em dedicação exclusiva (conta vinculada, pagamento direto, condicionamento do pagamento) | Lei | federal (nacional) | Planalto | PL-A, MC-A, TR-F | conferido |
| EXT-LEI14133-ART124 | Art. 124, I: alterações unilaterais; II, "d": restabelecimento do equilíbrio econômico-financeiro por acordo (força maior, caso fortuito, fato do príncipe ou fatos imprevisíveis) (arts. 124 a 136: alterações e recomposição de preços) | Lei | federal (nacional) | Planalto | MC-E, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART125 | Art. 125: limites de acréscimo e supressão (25%; 50% em reformas) | Lei | federal (nacional) | Planalto | MC-E | conferido |
| EXT-LEI14133-ART135 | Art. 135, I e II: datas-base da repactuação (proposta; acordo, convenção ou dissídio coletivo) | Lei | federal (nacional) | Planalto | PL-A, MC-E, MC-A, TR-F | conferido |
| EXT-LEI14133-ART137 | Art. 137, § 2º, IV: suspensão ou extinção por atraso de pagamento superior a 2 meses (arts. 137 a 139: extinção) | Lei | federal (nacional) | Planalto | MC-E, MC-A | conferido |
| EXT-LEI14133-ART138 | Art. 138, § 2º: indenização na extinção por culpa exclusiva da Administração | Lei | federal (nacional) | Planalto | MC-E | conferido |
| EXT-LEI14133-ART140 | Art. 140: recebimento do objeto (I: obras e serviços, provisório pelo fiscal e definitivo por servidor ou comissão, mediante termo detalhado; II: compras); § 3º: prazos e métodos dos recebimentos provisório e definitivo definidos em regulamento ou no contrato | Lei | federal (nacional) | Planalto | TR-F (acrescentada na fase 3) | conferido |
| EXT-LEI14133-ART141 | Art. 141: ordem cronológica de pagamentos por fonte de recursos e categoria de contrato; § 1º: hipóteses de quebra justificada; § 2º: a inobservância imotivada leva à apuração de responsabilidade (arts. 141 a 146: pagamentos) | Lei | federal (nacional) | Planalto | TR-A, MC-E, MC-A, TR-F | conferido |
| EXT-LEI14133-ART143 | Art. 143: pagamento da parcela incontroversa | Lei | federal (nacional) | Planalto | TR-A, MC-A, TR-F | conferido |
| EXT-LEI14133-ART147 | Arts. 147 a 150: nulidades; art. 147: avaliação do interesse público antes de declarar nulidade | Lei | federal (nacional) | Planalto | ETP-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART150 | Art. 150: indicação dos créditos orçamentários, sob pena de nulidade | Lei | federal (nacional) | Planalto | ED-E, ED-A, MC-A, TR-F | conferido |
| EXT-LEI14133-ART151 | Arts. 151 a 154: meios alternativos de resolução de controvérsias (conciliação, mediação, comitê de disputas, arbitragem) | Lei | federal (nacional) | Planalto | MC-E | conferido |
| EXT-LEI14133-ART156 | Art. 156: sanções (advertência, multa, impedimento, inidoneidade); § 3º: multa entre 0,5% e 30% (arts. 155 a 163: infrações e sanções) | Lei | federal (nacional) | Planalto | ED-A, MC-E, MC-A | conferido |
| EXT-LEI14133-ART162 | Art. 162: multa de mora na forma do edital ou contrato | Lei | federal (nacional) | Planalto | MC-A | conferido |
| EXT-LEI14133-ART164 | Art. 164: impugnação e esclarecimento até 3 dias úteis antes da abertura; parágrafo único: resposta em até 3 dias úteis, divulgada no sítio oficial | Lei | federal (nacional) | Planalto | ED-E, ED-A, RR-E, RR-A, TR-F, ETP-F | conferido |
| EXT-LEI14133-ART165 | Art. 165: recursos (3 dias úteis); § 1º, I: intenção de recorrer "imediatamente" | Lei | federal (nacional) | Planalto | ED-A | conferido |
| EXT-LEI14133-ART170 | Art. 170, § 4º: representação ao tribunal de contas | Lei | federal (nacional) | Planalto | RR-A | conferido |
| EXT-LEI14133-ART183 | Art. 183, III: contagem de prazos em dias úteis | Lei | federal (nacional) | Planalto | ED-A, TR-F, ETP-F | conferido |

### 2.2 Constituição e outras leis

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-CF88-ART5 | CF/88, art. 5º, LIV e LV: devido processo legal, contraditório e ampla defesa | Constituição | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm` | ED-A | conferido |
| EXT-CF88-ART37 | CF/88, art. 37, caput (princípios da Administração) e XXI (manutenção das condições efetivas da proposta) | Constituição | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm` | ED-A, MC-A, TR-F, ETP-F | conferido |
| EXT-LC123-ART44 | LC 123/2006, art. 44: empate ficto de ME/EPP | Lei complementar | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm` | ED-E | conferido |
| EXT-LC123-ART47 | LC 123/2006, art. 47: tratamento diferenciado de ME/EPP nas contratações públicas | Lei complementar | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm` | ED-A, ETP-F | conferido |
| EXT-LC123-ART48 | LC 123/2006, art. 48: itens exclusivos até R$ 80 mil; III: cota reservada de até 25% para bens divisíveis | Lei complementar | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm` | ED-E, ED-A, ETP-F | conferido |
| EXT-LC123-ART49 | LC 123/2006, art. 49: exceções ao tratamento diferenciado | Lei complementar | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm` | ED-E, ED-A | conferido |
| EXT-LEI11101-GERAL | Lei 11.101/2005: recuperação judicial e falência | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11101.htm` | ED-A | conferido |
| EXT-LEI9784-GERAL | Lei 9.784/1999: processo administrativo federal (vista dos autos, decisão motivada). Estados e municípios podem ter lei própria; cite a do ente | Lei | federal (União) | `https://www.planalto.gov.br/ccivil_03/leis/l9784.htm` | ED-A, RR-A | conferido |
| EXT-LEI9784-ART50 | Lei 9.784/1999, art. 50: dever de motivação | Lei | federal (União) | `https://www.planalto.gov.br/ccivil_03/leis/l9784.htm` | RR-A | conferido |
| EXT-LEI9784-ART66 | Lei 9.784/1999, art. 66, § 2º: prazos em dias contam-se de modo contínuo | Lei | federal (União) | `https://www.planalto.gov.br/ccivil_03/leis/l9784.htm` | ED-A | conferido |
| EXT-LEI8666-GERAL | Lei 8.666/1993 (revogada): art. 48 (inexequibilidade) e sorteio como desempate. Uso só histórico, para datar súmulas antigas | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/l8666cons.htm` | ED-E, ED-A | conferido |
| EXT-LEI12527-GERAL | Lei 12.527/2011 (LAI): pedido de acesso (art. 10); resposta em até 20 dias, prorrogáveis por 10 (art. 11, §§ 1º e 2º); recurso em 10 dias (art. 15); documento preparatório acessível com a edição do ato decisório (art. 7º, § 3º) | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm` | ETP-A, TR-F, ETP-F | conferido |
| EXT-CC-ART393 | Código Civil, art. 393: caso fortuito e força maior | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm` | MC-A | conferido |
| EXT-CLT-ART73 | CLT, art. 73: adicional noturno de no mínimo 20% sobre a hora diurna (caput); hora noturna reduzida de 52min30s (§ 1º) | Decreto-lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm` | PL-E, TR-F | conferido |
| EXT-CLT-ART192 | CLT, art. 192: adicional de insalubridade (10%, 20%, 40%) | Decreto-lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm` | PL-E, TR-F | conferido |
| EXT-CLT-ART193 | CLT, art. 193: adicional de periculosidade (30%) | Decreto-lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm` | PL-E, TR-F | conferido |
| EXT-CLT-ART473 | CLT, art. 473: ausências legais remuneradas (2 dias por falecimento, 3 por casamento, 5 por nascimento, adoção ou guarda compartilhada, 1 por doação de sangue a cada 12 meses, entre outras) | Decreto-lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm` | PL-E | conferido |
| EXT-LEI7418-GERAL | Lei 7.418/1985, art. 4º, parágrafo único: o empregador custeia o que exceder 6% do salário básico (vale-transporte) | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/l7418.htm` | PL-E, PL-A | conferido |
| EXT-LC110-GERAL | LC 110/2001: contribuição social adicional de 10% sobre o FGTS (extinta). Uso só histórico | Lei complementar | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp110.htm` | PL-E, PL-A | conferido |
| EXT-LEI13932-ART12 | Lei 13.932/2019, art. 12: extinção dos 10% adicionais do FGTS a partir de 01/01/2020 | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13932.htm` | PL-E, PL-A | conferido |
| EXT-LEI12506-GERAL | Lei 12.506/2011: aviso prévio proporcional (3 dias por ano, até 90 dias) | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12506.htm` | PL-E, PL-A | conferido |
| EXT-LC116-ART3 | LC 116/2003, art. 3º: ISS devido no local do estabelecimento prestador, salvo os incisos I a XXII, em que vale o local da prestação. Limpeza de imóveis (subitem 7.10, inciso VII) e vigilância (subitem 11.02, inciso XVI) estão nas exceções | Lei complementar | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm` | PL-A | conferido |
| EXT-LEI12546-GERAL | Lei 12.546/2011: CPRB (desoneração da folha) | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12546.htm` | PL-E | conferido |
| EXT-LEI14973-GERAL | Lei 14.973/2024: transição da desoneração. CPRB a 80% em 2025, 60% em 2026 e 40% em 2027, com contribuição sobre a folha de 25%, 50% e 75% da alíquota do art. 22, I e III, da Lei 8.212/1991 (5%, 10% e 15%); regime pleno em 2028 | Lei | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/l14973.htm` | PL-E | conferido |
| EXT-LC214-ART348 | LC 214/2025, art. 348: em 2026, IBS (0,1%, art. 343) e CBS (0,9%, art. 346) compensáveis com PIS/Cofins; § 1º: recolhimento dispensado para quem cumpre as obrigações acessórias | Lei complementar | federal (nacional) | `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm` | PL-E | conferido |
| EXT-ISS-MUNICIPAL | Lei do ISS do município competente (alíquota por item da lista de serviços) | Lei municipal | municipal | Site da prefeitura ou câmara municipal do município competente | PL-E, PL-A | a conferir |

---

## 3. Normas técnicas e regulatórias

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-REG-ENTE | Regulamento próprio do ente licitante (decreto estadual ou municipal de licitações, pesquisa de preços, pagamentos, modelo de planilha, processo administrativo) | Decreto / regulamento | estadual ou municipal | Diário Oficial e site do ente; legislação citada no preâmbulo do edital | ED-A, TR-E, PL-E, PP-E, PP-A, MC-E, MC-A, RR-A, TR-F, ETP-F | a conferir |
| EXT-IN73-GERAL | IN SEGES/ME 73/2022: licitação por menor preço ou maior desconto, forma eletrônica (art. 23: modo aberto com 10 minutos e prorrogações de 2 minutos) | Instrução normativa | federal (União) | `https://www.gov.br/compras/pt-br/acesso-a-informacao/legislacao/instrucoes-normativas/instrucao-normativa-seges-me-no-73-de-30-de-setembro-de-2022` | ED-A | conferido |
| EXT-IN65-GERAL | IN SEGES/ME 65/2021: procedimento de pesquisa de preços | Instrução normativa | federal (União) | `https://www.gov.br/compras/pt-br/acesso-a-informacao/legislacao/instrucoes-normativas/instrucao-normativa-seges-me-no-65-de-7-de-julho-de-2021` | PP-E | conferido |
| EXT-IN65-ART5 | IN SEGES/ME 65/2021, art. 5º, § 1º: prioridade aos parâmetros I e II | Instrução normativa | federal (União) | `https://www.gov.br/compras/pt-br/acesso-a-informacao/legislacao/instrucoes-normativas/instrucao-normativa-seges-me-no-65-de-7-de-julho-de-2021` | PP-E, PP-A, TR-F | conferido |
| EXT-IN65-ART6 | IN SEGES/ME 65/2021, art. 6º, caput (média, mediana ou menor valor; descarte de inexequíveis, inconsistentes e excessivos) e § 6º (limite da mediana do Painel) | Instrução normativa | federal (União) | `https://www.gov.br/compras/pt-br/acesso-a-informacao/legislacao/instrucoes-normativas/instrucao-normativa-seges-me-no-65-de-7-de-julho-de-2021` | PP-E, PP-A, TR-F | conferido |
| EXT-IN5-2017 | IN SEGES/MPDG 5/2017: serviços com dedicação exclusiva; modelo de planilha de custos (Anexo VII-D: Submódulo 2.1; Módulo 4 com 4.1, alíneas A a F, e 4.2 intrajornada); Anexo VI-B (produtividade de referência em limpeza e conservação) e Anexo VII-A, itens 7.3 e 10.6 a 10.7.1 (qualificação técnica em dedicação exclusiva), citados no mapa do TR (itens dos anexos a conferir) | Instrução normativa | federal (União) | `https://www.gov.br/compras/pt-br/acesso-a-informacao/legislacao/instrucoes-normativas/instrucao-normativa-no-5-de-26-de-maio-de-2017-atualizada` | PL-E, TR-F | conferido |
| EXT-IN7-2018 | IN 7/2018: alteração da IN 5/2017 (modelo de planilha) | Instrução normativa | federal (União) | Texto atualizado da IN 5/2017 (mesmo endereço de `EXT-IN5-2017`) | PL-E | conferido |
| EXT-IN98-2022 | IN SEGES/ME 98/2022: **autoriza** aplicar a IN 5/2017, "no que couber", às contratações da Lei 14.133/2021 (não "determina") | Instrução normativa | federal (União) | `https://www.gov.br/compras/pt-br/acesso-a-informacao/legislacao/instrucoes-normativas/instrucao-normativa-seges-me-no-98-de-26-de-dezembro-de-2022` | PL-E | conferido |
| EXT-IN77-2022 | IN SEGES/ME 77/2022: ordem cronológica de pagamentos; art. 7º: até 10 dias úteis para liquidação (do recebimento da nota fiscal) e até 10 dias úteis para pagamento (da liquidação), na esfera federal | Instrução normativa | federal (União) | `https://www.gov.br/compras/pt-br/acesso-a-informacao/legislacao/instrucoes-normativas/instrucao-normativa-seges-me-no-77-de-4-de-novembro-de-2022` | TR-E, TR-F | conferido |
| EXT-IN5-2014 | IN SLTI/MP 5/2014 (revogada): pesquisa de preços. Uso só histórico, para datar o Acórdão 1.445/2015 | Instrução normativa | federal (União) | `https://www.gov.br/compras` (Legislação) | PP-A | a conferir |
| EXT-MGI-NT35883 | Nota Técnica SEI 35883/2026/MGI: provisão de aviso prévio em prorrogações (fonte secundária) | Nota técnica | federal (União) | `https://www.gov.br/compras` (a localizar) | PL-E | a conferir |
| EXT-AGU-MODELOS | Modelos padronizados da AGU (termo de referência, edital, contrato) | Modelo de documento | federal (União) | `https://www.gov.br/agu` (modelos de licitações e contratos) | TR-E, TR-F | a conferir |
| EXT-NORMA-CCT | Convenção Coletiva de Trabalho da categoria (piso, benefícios, data-base, adicionais) | Instrumento coletivo de trabalho | por base territorial do sindicato | Sistema Mediador do MTE (`EXT-BASE-MEDIADOR`); sindicatos da categoria | ED-A, TR-A, PL-E, PL-A, MC-E, MC-A, RR-A, TR-F | a conferir |
| EXT-MTE-NR17 | Norma Regulamentadora NR-17 (ergonomia) do MTE | Norma regulamentadora | federal (nacional) | `https://www.gov.br/trabalho-e-emprego` (Normas Regulamentadoras) | TR-E, TR-F | a conferir |
| EXT-MTE-NR15 | Norma Regulamentadora NR-15 (atividades e operações insalubres e graus; Anexo 14, agentes biológicos) do MTE | Norma regulamentadora | federal (nacional) | `https://www.gov.br/trabalho-e-emprego` (Normas Regulamentadoras) | TR-F | a conferir |
| EXT-MTE-NR16 | Norma Regulamentadora NR-16 (atividades e operações perigosas, inclusive segurança pessoal ou patrimonial) do MTE | Norma regulamentadora | federal (nacional) | `https://www.gov.br/trabalho-e-emprego` (Normas Regulamentadoras) | TR-F | a conferir |
| EXT-NORMA-ABNT | Normas técnicas ABNT (NBR) aplicáveis ao objeto | Norma técnica | nacional | `https://www.abntcatalogo.com.br` | ED-A, TR-E, TR-A, TR-F, ETP-F | a conferir |
| EXT-REG-INMETRO | Portarias e certificações do INMETRO | Regulamento técnico | federal (nacional) | `https://www.gov.br/inmetro` | ED-A, TR-E, TR-A, TR-F, ETP-F | a conferir |
| EXT-REG-ANVISA | Registros e regulamentos da ANVISA | Regulamento sanitário | federal (nacional) | `https://www.gov.br/anvisa` | ED-A, TR-E, TR-F | a conferir |
| EXT-REG-ANATEL | Homologações e regulamentos da ANATEL | Regulamento de telecomunicações | federal (nacional) | `https://www.gov.br/anatel` | ED-A, TR-F | a conferir |
| EXT-REG-CONSELHOS | Legislação dos conselhos profissionais (CONFEA/CREA, CAU, CRA, CFC): atividades privativas e registro | Lei e resolução de conselho | federal (nacional) | `https://www.confea.org.br`, `https://caubr.gov.br`, `https://cfa.org.br`, `https://cfc.org.br` | ED-A, TR-F | a conferir |
| EXT-REG-CFC | Normas contábeis do CFC (índices de liquidez e solvência) | Norma contábil | federal (nacional) | `https://cfc.org.br` | ED-A | a conferir |

---

## 4. Jurisprudência

Toda a jurisprudência fica `a conferir` até ser lida no portal do tribunal. Súmulas e acórdãos do TCU vinculam a esfera federal; em estados e municípios, servem como reforço, ao lado da jurisprudência do tribunal de contas do ente.

### 4.1 Súmulas do TCU

Onde consultar: Pesquisa de Jurisprudência do TCU, `https://pesquisa.apps.tcu.gov.br`.

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-TCU-SUM177 | Súmula 177: definição precisa e suficiente do objeto é regra indispensável da competição; na compra, a quantidade demandada integra a definição do objeto | Súmula | federal | Pesquisa TCU | ETP-A, TR-A, PP-A, TR-F, ETP-F | conferido |
| EXT-TCU-SUM247 | Súmula 247: adjudicação por item quando o objeto é divisível | Súmula | federal | Pesquisa TCU | ED-A, ETP-A, TR-A, TR-F, ETP-F | conferido |
| EXT-TCU-SUM254 | Súmula 254: IRPJ e CSLL não são despesa indireta passível de inclusão no BDI do orçamento-base, por serem tributos diretos e personalísticos (texto oficial conferido) | Súmula | federal | Pesquisa TCU | PL-E, PL-A, ED-F | conferido |
| EXT-TCU-SUM262 | Súmula 262: prazo para o licitante demonstrar a exequibilidade antes da desclassificação (firmada sob a Lei 8.666/1993) | Súmula | federal | Pesquisa TCU | ED-A | conferido |
| EXT-TCU-SUM263 | Súmula 263: quantitativos mínimos proporcionais nas parcelas de maior relevância | Súmula | federal | Pesquisa TCU | ED-A, TR-A, TR-F | conferido |
| EXT-TCU-SUM275 | Súmula 275: capital social, patrimônio líquido ou garantias, de forma não cumulativa | Súmula | federal | Pesquisa TCU | ED-A | conferido |
| EXT-TCU-SUM281 | Súmula 281: vedação à participação de cooperativas quando o serviço exige subordinação jurídica, pessoalidade e habitualidade (Acórdão 1.789/2012-Plenário); em reanálise após o Acórdão 2.463/2019-1ª Câmara e mitigada pelo Acórdão 1.587/2022-Plenário (fonte secundária) | Súmula | federal | Pesquisa TCU | ETP-F | a conferir |

### 4.2 Acórdãos e informativos do TCU

Onde consultar: Pesquisa de Jurisprudência do TCU, `https://pesquisa.apps.tcu.gov.br`.

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-TCU-AC930-2008 | Acórdão 930/2008-Plenário: modificação do edital que afeta propostas exige reabrir o prazo inicialmente estabelecido (sob o Decreto 5.450/2005) | Acórdão | federal | Pesquisa TCU | RR-E, RR-A | conferido |
| EXT-TCU-AC1094-2004 | Acórdão 1.094/2004-Plenário: tempo de existência do licitante não mede a qualificação; indevido pontuá-lo na proposta técnica (enunciado da Jurisprudência Selecionada do TCU) | Acórdão | federal | Pesquisa TCU | ED-F, TR-F (apoio parcial a `EXT-PEND-TEMPOEXIST`) | conferido |
| EXT-TCU-AC915-2009 | Acórdão 915/2009-Plenário: assertiva do pregoeiro em esclarecimento tem efeito vinculante para os participantes; descumpri-la pode responsabilizar o pregoeiro (enunciado da Jurisprudência Selecionada do TCU) | Acórdão | federal | Pesquisa TCU | ED-F (resolve `EXT-PEND-VINCESCLAR`) | conferido |
| EXT-TCU-AC964-2012 | Acórdão 964/2012-Plenário: a perda da regularidade fiscal justifica sanções, mas não autoriza reter pagamento por serviço prestado (acórdãos anteriores, como 2.219/2010 e 446/2011, admitiam a retenção) (enunciado da Jurisprudência Selecionada do TCU) | Acórdão | federal | Pesquisa TCU | TR-F (resolve `EXT-PEND-RETENCAO`) | conferido |
| EXT-TCU-AC2078-2014 | Acórdão 2.078/2014-Plenário: alteração que afeta propostas exige divulgação pela mesma forma do original e reabertura do prazo inicialmente estabelecido (caso Sebrae, sob a Lei 8.666) | Acórdão | federal | Pesquisa TCU | RR-A | conferido |
| EXT-TCU-AC1445-2015 | Acórdão 1.445/2015-Plenário: orçamento só com consulta a fornecedores contraria a jurisprudência; priorizar Portal de Compras e contratações similares (IN 5/2014, art. 2º, I e III) | Acórdão | federal | Pesquisa TCU | PP-A | conferido |
| EXT-TCU-AC2637-2015 | Acórdão 2.637/2015-Plenário: pesquisa de preços com amplitude insuficiente (poucos fornecedores, mercado vasto) e cotação discrepante | Acórdão | federal | Pesquisa TCU | PP-A | conferido |
| EXT-TCU-AC1186-2017 | Acórdão 1.186/2017-Plenário: aviso prévio trabalhado de até 1,94% só no 1º ano e até 0,194% a cada ano de prorrogação (Lei 12.506/2011), conforme itens 9.1.1 e 9.2; cálculo [(100%/30) x 7]/12, vindo dos Acórdãos 1.904/2007 e 3.006/2010 | Acórdão | federal | Pesquisa TCU | PL-E | conferido |
| EXT-TCU-AC248-2017 | Acórdão 248/2017-Plenário: restringir a um fabricante só é aceitável com ETP fundado em ampla pesquisa e comparação efetiva de alternativas e custos (enunciado da Jurisprudência Selecionada do TCU) | Acórdão | federal | Pesquisa TCU | TR-F, ETP-F (resolve `EXT-PEND-MOTIVCOMP`) | conferido |
| EXT-TCU-AC7184-2018 | Acórdão 7.184/2018-Segunda Câmara: o critério de reajuste no edital e no contrato é imposição, não discricionariedade, mesmo em vigência até 12 meses; a falta da cláusula não impede o reequilíbrio (sob a Lei 8.666) (enunciado da Jurisprudência Selecionada do TCU) | Acórdão | federal | Pesquisa TCU | — (resolve `EXT-PEND-REAJUSTE`) | conferido |
| EXT-TCU-AC2622-2013 | Acórdão 2.622/2013-Plenário: percentuais de referência de BDI e de administração local em obras públicas; administração local como custo direto | Acórdão | federal | Pesquisa TCU | — (acrescentada na conferência de 2026-10-15; reforço de `EXT-PEND-BDI`) | conferido |
| EXT-TCU-AC1101-2020 | Acórdão 1.101/2020-Plenário: vedada a limitação injustificada do número de atestados e a vedação de soma de atestados sem justificativa técnica | Acórdão | federal | Pesquisa TCU | ED-A, TR-F | conferido |
| EXT-TCU-AC1182-2020 | Acórdão 1.182/2020-Plenário: **citação errada**. O acórdão com esse número trata de superfaturamento em obra ferroviária, não de provisão de férias. Não usar; ver `EXT-ADM-MEC-2024` | Acórdão | federal | Pesquisa TCU | PL-A | a conferir |
| EXT-TCU-AC1201-2020 | Acórdão 1.201/2020-Plenário: empresa em recuperação judicial pode participar, amparada em certidão do juízo que ateste a aptidão econômica e financeira | Acórdão | federal | Pesquisa TCU | ED-A | conferido |
| EXT-TCU-AC2032-2021 | Acórdão 2.032/2021-Plenário: alteração significativa do edital, mesmo por resposta a esclarecimento, sem republicação e reabertura de prazos ofende publicidade, vinculação e isonomia | Acórdão | federal | Pesquisa TCU | RR-A, ED-F | conferido |
| EXT-TCU-AC2460-2022 | Acórdão 2.460/2022-Plenário: é irregular desclassificar proposta só porque o BDI excede o percentual do edital; a análise é do preço final (no mesmo sentido, Acórdãos 648/2016 e 1.511/2018) (enunciado da Jurisprudência Selecionada do TCU) | Acórdão | federal | Pesquisa TCU | ED-F (resolve `EXT-PEND-BDI`) | conferido |
| EXT-TCU-AC1616-2023 | Acórdão 1.616/2023-Plenário: simulação da pesquisa de preços em contratação de TI; exame da conduta das empresas cotantes (art. 46 da Lei 8.443/1992, inidoneidade) | Acórdão | federal | Pesquisa TCU | — (acrescentada na conferência de 2026-10-15; resolve `EXT-PEND-FRAUDECOT`) | conferido |
| EXT-TCU-AC465-2024 | Acórdão 465/2024-Plenário: o limite do art. 59, § 4º, gera presunção relativa de inexequibilidade; dar ao licitante a chance de demonstrar a exequibilidade (art. 59, § 2º) | Acórdão | federal | Pesquisa TCU | ED-F (acrescentada na conferência de 2026-10-15; resolve `EXT-PEND-EXEQ14133`) | conferido |
| EXT-TCU-AC1798-2024 | Acórdão 1.798/2024-Plenário: parentesco entre sócios, sozinho, não é fraude; indícios convergentes (mesmo IP nos lances, contador ou endereço em comum) podem caracterizá-la | Acórdão | federal | Pesquisa TCU | — (acrescentada na conferência de 2026-10-15; reforço de `EXT-PEND-FRAUDECOT`) | conferido |
| EXT-TCU-AC214-2025 | Acórdão 214/2025-Plenário: reafirma, por maioria, a presunção relativa do Acórdão 465/2024 | Acórdão | federal | Pesquisa TCU | ED-F (acrescentada na conferência de 2026-10-15) | conferido |
| EXT-TCU-AC1505-2026 | Acórdão 1.505/2026-Plenário: verificada a irregularidade fiscal, é vedado reter pagamento por serviço executado ou bem entregue, sob pena de enriquecimento sem causa (enunciado da Jurisprudência Selecionada do TCU) | Acórdão | federal | Pesquisa TCU | TR-F (resolve `EXT-PEND-RETENCAO`) | conferido |
| EXT-TCU-AC58-2026 | Acórdão de Relação 58/2026-Plenário (serviço de recepcionistas; cópia à Câmara Nacional de Modelos da AGU). Existe, mas a tese sobre aviso prévio está nos pareceres, não no texto público | Acórdão | federal | Pesquisa TCU | PL-E, PL-A | a conferir |
| EXT-TCU-INFO2026-INDICES | Informativo do TCU de 2026: índices contábeis acima de 1 cumulados com PL de até 10% | Informativo de jurisprudência | federal | `https://portal.tcu.gov.br` (Informativos de Licitações e Contratos) | ED-A | a conferir |

### 4.3 Outros tribunais e precedentes administrativos

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-STF-SV4 | Súmula Vinculante 4 do STF: salário mínimo não pode ser indexador de vantagem nem ser substituído por decisão judicial. Pelo RE 565.714, a base do adicional de insalubridade segue o salário mínimo até lei nova | Súmula vinculante | federal (nacional) | `https://portal.stf.jus.br` (Súmulas Vinculantes) | PL-E | conferido |
| EXT-STF-SV21 | Súmula Vinculante 21 do STF: inconstitucional exigir depósito ou arrolamento prévio para recurso administrativo | Súmula vinculante | federal (nacional) | `https://portal.stf.jus.br` (Súmulas Vinculantes) | ED-A | conferido |
| EXT-STF-TEMA846 | Tema 846 da repercussão geral do STF (RE 878.313): constitucional a contribuição de 10% da LC 110/2001, pela persistência do objeto; trânsito em julgado em 27/10/2020 | Tese de repercussão geral | federal (nacional) | `https://portal.stf.jus.br` (Repercussão Geral) | PL-A | conferido |
| EXT-TST-SUM60 | Súmula 60 do TST: integração do adicional noturno habitual | Súmula | federal (nacional) | `https://www.tst.jus.br` (Súmulas) | PL-E, TR-F | a conferir |
| EXT-TST-SUM172 | Súmula 172 do TST: horas extras habituais no DSR | Súmula | federal (nacional) | `https://www.tst.jus.br` (Súmulas) | PL-E | a conferir |
| EXT-TST-SUM448 | Súmula 448 do TST: insalubridade na limpeza de banheiros de uso público | Súmula | federal (nacional) | `https://www.tst.jus.br` (Súmulas) | PL-A, TR-F | a conferir |
| EXT-STJ-RESP1733688 | REsp 1.733.688/SC (retenção de pagamento): **não localizado; não usar** até achar precedente verificado (ver `EXT-PEND-RETENCAO`) | Acórdão | federal (nacional) | `https://scon.stj.jus.br` | MC-A | a conferir |
| EXT-TCESP-SUM50 | Súmula 50 do TCE/SP: a Administração não pode impedir empresa em recuperação judicial; pode exigir na habilitação o plano homologado e em vigor, sem dispensar os requisitos econômico-financeiros (reforço só para órgão paulista) | Súmula | estadual (SP) | `https://tce.sp.gov.br/legislacao/resolucao/resolucao-052019/sumula-50` | ED-A | conferido |
| EXT-TJ-GERAL | Precedentes dos tribunais de justiça (genérico; localizar por tema e estado do ente) | Acórdão | estadual | Portal de jurisprudência do TJ do estado do ente | ED-A | a conferir |
| EXT-ADM-MEC-2024 | Esclarecimento do MEC em pregão de 2024: provisão de férias e substituto como alternativas (fonte secundária) | Precedente administrativo | federal (União) | PNCP / Compras.gov.br (a localizar) | PL-A | a conferir |

### 4.4 Fundamentos a localizar

Teses que os arquivos usam sem fonte localizada. Os mapas podem citar estes IDs, mas a peça só cita a tese depois que o fundamento for achado e conferido.

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-PEND-TEMPOEXIST | Vedação de exigir tempo mínimo de existência da empresa na habilitação. Apoio parcial: `EXT-TCU-AC1094-2004` (tempo de existência não mede qualificação, em pontuação técnica) e `EXT-LEI14133-ART65`; acórdão específico sobre habilitação ainda a localizar | Jurisprudência a localizar | federal | Pesquisa TCU | ED-A, TR-F | a conferir |
| EXT-PEND-BDI | **Resolvido:** ver `EXT-TCU-AC2460-2022` (julgamento) e `EXT-TCU-AC2622-2013` (composição do BDI em obras) | Jurisprudência a localizar | federal | Pesquisa TCU | ED-A | conferido |
| EXT-PEND-EXEQ14133 | **Resolvido:** ver `EXT-TCU-AC465-2024` e `EXT-TCU-AC214-2025` (presunção relativa sob o art. 59, § 4º) | Jurisprudência a localizar | federal | Pesquisa TCU | ED-A | conferido |
| EXT-PEND-VINCESCLAR | **Resolvido:** ver `EXT-TCU-AC915-2009` (resposta a esclarecimento é vinculante) e `EXT-TCU-AC2032-2021` (resposta não altera regra sem republicação) | Jurisprudência a localizar | federal | Pesquisa TCU | RR-E | conferido |
| EXT-PEND-ATESTPRIV | Vedação de aceitar só atestados de pessoa jurídica de direito público. Sem enunciado na Jurisprudência Selecionada; o Acórdão 657/2016 não trata disso. Usar a lei: `EXT-CF88-ART37` (XXI) e `EXT-LEI14133-ART9` (I, "a") | Jurisprudência a localizar | federal | Pesquisa TCU | TR-A, TR-F | a conferir |
| EXT-PEND-MOTIVCOMP | **Resolvido:** ver `EXT-TCU-AC248-2017` (escolha sem ETP com comparação efetiva de alternativas é inaceitável) e `EXT-LEI14133-ART18` (§ 1º, V) | Jurisprudência a localizar | federal | Pesquisa TCU | ETP-A | conferido |
| EXT-PEND-FRAUDECOT | **Resolvido:** ver `EXT-TCU-AC1616-2023` (simulação da pesquisa de preços) e `EXT-TCU-AC1798-2024` (indícios convergentes) | Jurisprudência a localizar | federal | Pesquisa TCU | PP-A | conferido |
| EXT-PEND-REAJUSTE | **Resolvido:** ver `EXT-TCU-AC7184-2018` (critério de reajuste é imposição, não discricionariedade) | Jurisprudência a localizar | federal | Pesquisa TCU | MC-A | conferido |
| EXT-PEND-RETENCAO | **Resolvido:** ver `EXT-TCU-AC964-2012` e `EXT-TCU-AC1505-2026` (irregularidade fiscal não autoriza reter pagamento de serviço prestado) | Jurisprudência a localizar | federal | Pesquisa TCU; `https://scon.stj.jus.br` | MC-A | conferido |

---

## 5. Bases de dados

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-BASE-PNCP | Portal Nacional de Contratações Públicas: editais, anexos, contratos, histórico de participantes e preços homologados | Base de dados pública | federal (nacional) | `https://pncp.gov.br` (redireciona para `https://www.gov.br/pncp`); API de consulta em `https://pncp.gov.br/api/consulta` | ED-A, ETP-A, MC-E, PP-E, PP-A, RR-A, TR-F, ETP-F | conferido |
| EXT-BASE-PAINELPRECOS | Painel de Preços do Governo Federal. Segundo o comunicado nº 30/25 do Portal de Compras, deixou de ser atualizado com dados até 04/07/2025; para preços recentes, usar `EXT-BASE-PESQPRECOS` | Base de dados pública | federal (União) | `https://paineldeprecos.planejamento.gov.br` | PP-E, PP-A, ETP-F | a conferir |
| EXT-BASE-PESQPRECOS | Pesquisa de Preços do Compras.gov.br (versão sem login, histórico de 12 meses) | Base de dados pública | federal (União) | `https://pesquisaprecos.compras.gov.br` | TR-F, ETP-F (acrescentada na conferência de 2026-10-15) | conferido |
| EXT-BASE-PAINELCONTRAT | "Painel de Contratações Públicas" citado no ETP. O Painel de Compras do Portal de Compras pede login e, segundo o comunicado nº 30/25, deixou de ser atualizado; na prática, usar o PNCP (`EXT-BASE-PNCP`) ou `EXT-BASE-PESQPRECOS` | Base de dados pública | federal | `https://www.gov.br/compras/pt-br/cidadao/painel-de-compras` (pede login) | ETP-A, ETP-F | a conferir |
| EXT-BASE-BPS | Banco de Preços em Saúde | Base de dados pública | federal (União) | `https://www.gov.br/saude/pt-br/acesso-a-informacao/banco-de-precos` | PP-E | conferido |
| EXT-BASE-NFE | Base nacional de notas fiscais eletrônicas (parâmetro V do art. 23, § 1º). O portal da NF-e existe, mas o uso para pesquisa de preços depende de regulamentação ainda não editada (segundo relatório de pesquisa da Receita Federal) | Base de dados | federal (nacional) | `https://www.nfe.fazenda.gov.br` | PP-E | a conferir |
| EXT-BASE-CATMAT | Catálogo de materiais e serviços (CATMAT/CATSER) | Catálogo público | federal (União) | `https://catalogo.compras.gov.br` | PP-A | conferido |
| EXT-BASE-COMPRASGOV | Compras.gov.br: portal da sessão, regulamento do portal, quadro informativo (avisos, esclarecimentos, impugnações), registros de instabilidade | Portal eletrônico | federal (União) | `https://www.gov.br/compras`; quadro informativo público em `https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/quadro-informativo?compra=<idCompra>` | ED-E, ED-A, TR-F, ETP-F | conferido |
| EXT-BASE-SITEORGAO | Sítio eletrônico oficial do órgão licitante (respostas a esclarecimentos, anexos, avisos) | Site oficial | do ente licitante | Site do órgão | RR-E, TR-F | a conferir |
| EXT-BASE-DIARIO | Diário Oficial do ente (avisos de retificação) | Publicação oficial | federal, estadual ou municipal | Diário Oficial do ente | RR-A | a conferir |
| EXT-BASE-TRANSPARENCIA | Portal da Transparência do órgão (execução e consumo de contratos anteriores) | Base de dados pública | do ente licitante | Portal do ente; na esfera federal, `https://portaldatransparencia.gov.br` | ETP-A, TR-F, ETP-F | conferido |
| EXT-BASE-CNPJ | Cadastro CNPJ da Receita Federal / RedeSim: QSA, endereço, CNAE principal e secundários. Registrar só o vínculo encontrado, sem nomes nem CPF | Base de dados pública | federal (nacional) | `https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/` (comprovante de CNPJ); dados abertos do CNPJ | ED-A, PP-A, TR-F, ETP-F | conferido |
| EXT-BASE-CNAE | Classificação Nacional de Atividades Econômicas (CNAE) | Classificação oficial | federal (nacional) | `https://concla.ibge.gov.br` | ED-A, TR-A, PP-A, TR-F, ETP-F | conferido |
| EXT-BASE-MEDIADOR | Sistema Mediador do MTE: CCTs registradas | Base de dados pública | federal (nacional) | `https://mediador.trabalho.gov.br/sistemas/mediador` (o endereço antigo `www3.mte.gov.br` redireciona para cá) | ED-A, PL-E, PL-A, TR-F | conferido |
| EXT-BASE-FPAS | Tabela de códigos FPAS da Receita Federal (alíquotas de terceiros por atividade) | Tabela oficial | federal (nacional) | IN RFB 2.110/2022, Anexo V (consolidada, alterada pela IN RFB 2.289/2025), em `https://normas.receita.fazenda.gov.br`; também a Tabela 4 do Manual do eSocial | PL-E, PL-A | a conferir |
| EXT-BASE-SINAPI | SINAPI (Caixa): custos e índices da construção civil | Sistema oficial de custos | federal (nacional) | `https://www.caixa.gov.br/poder-publico/modernizacao-gestao/sinapi/Paginas/default.aspx` | ED-A, PP-E, PP-A, MC-E | conferido |
| EXT-BASE-SICRO | SICRO (DNIT): custos de obras rodoviárias | Sistema oficial de custos | federal (nacional) | `https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/custos-referenciais/sistemas-de-custos/sicro` | ED-A, PP-E | conferido |
| EXT-BASE-IBGE | Índices do IBGE (IPCA, INPC) | Índice oficial | federal (nacional) | `https://www.ibge.gov.br/explica/inflacao.php` (IPCA e INPC) | MC-E, PP-A, ETP-F | conferido |
| EXT-BASE-FGV | Índices e tabelas da FGV (IGP-M e outros) | Índice de referência | nacional | `https://portalibre.fgv.br` (FGV IBRE, IGP-M) | MC-E, PP-E, PP-A, ETP-F | conferido |
| EXT-BASE-ANP | Levantamento de preços de combustíveis da ANP | Tabela oficial | federal (nacional) | `https://www.gov.br/anp/pt-br/assuntos/precos-e-defesa-da-concorrencia/precos/levantamento-de-precos-de-combustiveis-ultimas-semanas-pesquisadas` | PP-E, PP-A | conferido |
| EXT-BASE-FIPE | Tabela FIPE (veículos) | Tabela de referência | nacional | `https://veiculos.fipe.org.br` | PP-E | conferido |
| EXT-BASE-SUSEP | SUSEP: seguradoras autorizadas (seguro-garantia) | Base de dados pública | federal (nacional) | `https://www.gov.br/susep/pt-br` | MC-E | conferido |

---

## 6. Prova de mercado

Provas produzidas pela Servfaz para cada caso. Não têm texto a conferir; o cuidado é guardar data, origem e, nas cotações, CNPJ e descrição exata do item.

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| EXT-MERC-COTACOES | Cotações e orçamentos formais de fornecedores (data, CNPJ, descrição exata do item) | Prova de mercado | n/a | Solicitação formal aos fornecedores | PP-E, PP-A | n/a |
| EXT-MERC-DECLARACOES | Declarações de fabricantes e transportadoras (prazos de fabricação e entrega, preço de custo) | Prova de mercado | n/a | Solicitação formal aos fabricantes e transportadoras | ED-A, TR-A, PP-A, TR-F | n/a |
| EXT-MERC-FICHAS | Fichas técnicas e catálogos dos principais fabricantes (comparação com a especificação do TR) | Prova de mercado | n/a | Sites e catálogos dos fabricantes | TR-A, TR-F, ETP-F | n/a |
| EXT-MERC-ALTERNATIVAS | Levantamento de soluções alternativas de mercado e de como outros órgãos resolveram o mesmo problema | Prova de mercado | n/a | Fabricantes, contratações de outros órgãos no PNCP | ETP-A, ETP-F | n/a |
| EXT-MERC-SITES | Preços em sites de comércio eletrônico, com data, hora e URL | Prova de mercado | n/a | Sites de domínio amplo | PP-E, PP-A | n/a |
| EXT-MERC-MIDIA | Pesquisa publicada em mídia especializada | Prova de mercado | n/a | Publicações do setor | PP-E | n/a |
| EXT-MERC-BOLSAS | Cotações de bolsas de mercadorias (insumos como cobre e combustível) | Prova de mercado | n/a | Bolsas de mercadorias | PP-A | n/a |
| EXT-MERC-VISTORIA | Vistoria ou levantamento técnico do local de execução | Prova de mercado | n/a | Visita técnica ou declaração do responsável técnico | ETP-A, ETP-F, TR-F | n/a |

---

## 7. Observações

1. **Faixas de artigos nos títulos da Minuta.** Os títulos de `Estrutura - Minuta Contratual.md` citam faixas (arts. 89 a 154, 105 a 114, 141 a 146, 96 a 102, 124 a 136, 155 a 163, 137 a 139). No catálogo, cada faixa aponta para o artigo citado no corpo: 105–114 → `ART106`, `ART107`, `ART111`; 141–146 → `ART141`, `ART143`; 96–102 → `ART96`, `ART102`; 124–136 → `ART124`, `ART125`, `ART135`; 155–163 → `ART156`, `ART162`; 137–139 → `ART137`, `ART138`; 151–154 → `ART151`; 89–154 → `GERAL`. Se um mapa precisar de um artigo da faixa que não está aqui, ele entra primeiro no catálogo.
2. **Mesmo número, leis diferentes.** "Art. 5º" na Análise do Edital é da CF/88 (`EXT-CF88-ART5`); nas demais Análises, é da Lei 14.133 (`EXT-LEI14133-ART5`). "Arts. 5º e 6º" na Estrutura da Pesquisa são da IN 65/2021. "Art. 66" é da Lei 9.784/1999 e "art. 48" aparece na LC 123/2006 e na Lei 8.666/1993.
3. **Fontes só históricas:** `EXT-LEI8666-GERAL`, `EXT-LC110-GERAL`, `EXT-IN5-2014`. Servem para datar súmulas e acórdãos antigos, não como fundamento.
4. **Não usar:** `EXT-STJ-RESP1733688` (não localizado), `EXT-TCU-AC1182-2020` (número errado: o acórdão trata de outro assunto) e os `EXT-PEND-*` ainda `a conferir`.
5. **Fonte interna nova.** `INT-PCA` não estava na lista do plano; foi acrescentada porque o ETP (inciso II) e o TR (seção II) pedem o cruzamento com o Plano de Contratações Anual.
6. **URLs.** Os endereços do Planalto seguem o padrão do texto compilado; os demais apontam para o portal oficial do órgão quando o caminho exato não foi confirmado. Confira o link ao trocar o status para `conferido`.

## 8. Como foi verificado

Busca nos 14 arquivos por `art.`/`arts.`, `Lei`, `LC`, `Súmula`, `Acórdão`, `IN `, `Tema`, `REsp`, `Nota Técnica`, `NR-` e pelos nomes das bases (PNCP, Painel, SINAPI, SICRO, Mediador, RedeSim, CNAE, FPAS, ANP, FIPE, IPCA, IGP-M, CATMAT). Cada ocorrência foi associada a um ID deste catálogo. Os casos ambíguos estão na seção 7.

## 9. Conferência nas fontes oficiais (2026-10-15)

### 9.1 O que foi conferido e o que mudou

- **Lei 14.133/2021:** todos os artigos do catálogo foram lidos no Planalto. Acrescentados `ART65`, `ART98` e `ART99`. Ajustes: o art. 22 torna a matriz de riscos **facultativa**, e obrigatória só em grande vulto ou contratação integrada/semi-integrada (§ 3º); o seguro-garantia de 30% está no art. 99, não no 102; a alínea "i" do art. 6º, XXIII, manda a estimativa constar de documento separado e classificado.
- **Constituição e demais leis:** todas lidas no Planalto e conferidas. A Lei 14.973/2024 confirma 10% sobre a folha em 2026 (50% da alíquota de 20%), e a LC 116/2003 confirma limpeza (7.10) e vigilância (11.02) entre as exceções do ISS.
- **INs federais:** 65/2021, 73/2022, 77/2022, 98/2022 e 5/2017 (com a IN 7/2018) lidas no Portal de Compras. Dois ajustes: a IN 98/2022 **autoriza** aplicar a IN 5/2017 no que couber, e não "determina" como diz `Estrutura - Planilha de Custos.md`; e a IN 77/2022 fixa até 10 + 10 dias úteis (liquidação + pagamento) na esfera federal, o que dá número ao prazo de pagamento tratado como "parâmetro de regulamento" na Minuta.
- **Súmulas do TCU** 177, 247, 254, 262, 263 e 275: texto oficial conferido.
- **Acórdãos do TCU:** 930/2008, 2.078/2014, 1.445/2015, 2.637/2015, 1.186/2017, 1.101/2020, 1.201/2020 e 2.032/2021 conferidos; acrescentados 2.622/2013, 1.616/2023, 465/2024, 1.798/2024 e 214/2025. O **1.182/2020 está errado** (outro assunto). O 1.186/2017 confere quanto à exclusão do aviso prévio trabalhado após o 1º ano, mas o número 1,94% não aparece no texto público.
- **STF e TCE/SP:** SV 4, SV 21, Tema 846 e Súmula 50 do TCE/SP conferidos nos portais oficiais.
- **Bases:** PNCP, BPS, CATMAT, Transparência, CNPJ, CNAE, Mediador (endereço mudou), SINAPI, SICRO, ANP e FIPE abertas e conferidas. O **Painel de Preços** não respondeu e, segundo o comunicado nº 30/25 do Portal de Compras, deixou de ser atualizado em 04/07/2025; acrescentada `EXT-BASE-PESQPRECOS`.
- **Acórdão 657/2016-Plenário:** citado na web como fundamento de `EXT-PEND-ATESTPRIV`, mas não trata do tema. Não usar.

- **Segunda rodada (mesmo dia):** o 1,94% do aviso prévio está no item 9.2 do Acórdão 1.186/2017, com 0,194% por ano de prorrogação. Na Jurisprudência Selecionada do TCU foram achados os fundamentos de cinco pendências (BDI, vinculação do esclarecimento, comparação de soluções no ETP, reajuste e retenção) e apoio parcial ao tempo de existência. Os acórdãos novos foram conferidos pelo enunciado; antes de citar trecho literal, abra o inteiro teor. IBGE, FGV IBRE, SUSEP e Portal de Compras abriram e foram conferidos.

- **Fase 3 (mapas do TR e do ETP):** acrescentados `EXT-LEI14133-ART117` (fiscalização do contrato) e `EXT-LEI14133-ART140` (recebimento provisório e definitivo; § 3º remete prazos e métodos ao regulamento ou ao contrato), ambos lidos no Planalto. As siglas TR-F e ETP-F foram acrescentadas na coluna "Usado em" das fontes que esses mapas citam.

### 9.2 O que ficou para conferência manual

| ID | Por que não foi conferido | O que fazer |
| :-- | :-- | :-- |
| EXT-TST-SUM60, EXT-TST-SUM172, EXT-TST-SUM448 | As páginas de súmulas do TST não abriram (endereços antigos dão 404); o texto só apareceu citado em decisões no site do TST | Abrir as súmulas no site do TST e conferir o enunciado |
| EXT-TCU-AC58-2026 | Acórdão de relação: a tese sobre aviso prévio em prorrogações está nos pareceres, que não aparecem no texto público | Baixar o processo TC 028.944/2024-0 ou os pareceres no portal do TCU |
| EXT-MGI-NT35883 | Nota técnica do SEI do MGI; não localizada em página pública | Localizar no Portal de Compras ou pedir o documento |
| EXT-TCU-INFO2026-INDICES | Informativo sem número nem data no arquivo de origem | Indicar o número do informativo ou do acórdão |
| EXT-BASE-PAINELPRECOS | Site fora do ar no teste; o comunicado nº 30/25 pede login no Portal de Compras | Confirmar o comunicado e decidir se o Painel sai do catálogo |
| EXT-ADM-MEC-2024 | Esclarecimento de pregão sem número ou link | Indicar o pregão (número e UASG) para localizar no Compras.gov.br |
| EXT-STJ-RESP1733688 | Não localizado; a pista é o AgInt no REsp 1.742.457/CE (via fonte secundária) | Conferir o AgInt no site do STJ |
| EXT-PEND-TEMPOEXIST, EXT-PEND-ATESTPRIV | Sem enunciado específico na Jurisprudência Selecionada do TCU (buscas por "tempo de existência", "tempo mínimo de constituição", "atestado" + "direito privado"/"órgão público") | Pesquisar na base de acórdãos completos ou reescrever a tese só com a lei (art. 65, § 1º; CF, art. 37, XXI; art. 9º, I, "a") |
| EXT-BASE-FPAS | Anexo V da IN RFB 2.110/2022 indicado por parecer da Receita, mas não aberto | Abrir a IN consolidada no portal de normas da Receita e conferir o Anexo V |
| EXT-BASE-NFE, EXT-BASE-PAINELCONTRAT | NF-e: base sem regulamentação para pesquisa de preços; Painel de Compras pede login e parou de ser atualizado | Decidir se ficam no catálogo só como referência |
| EXT-IN5-2014 | Norma revogada, uso só histórico | Conferir só se for citada em peça |
| EXT-REG-ENTE, EXT-ISS-MUNICIPAL, EXT-NORMA-CCT, EXT-BASE-SITEORGAO, EXT-BASE-DIARIO, EXT-TJ-GERAL, EXT-NORMA-ABNT, EXT-REG-INMETRO, EXT-REG-ANVISA, EXT-REG-ANATEL, EXT-REG-CONSELHOS, EXT-REG-CFC, EXT-MTE-NR17, EXT-AGU-MODELOS | Dependem do ente, da categoria ou do objeto de cada edital | Conferir caso a caso, na análise de cada edital |
| EXT-TCU-SUM281 | Acrescentada na fase 3 a partir de fonte secundária; a súmula está em reanálise (Acórdão 2.463/2019-1ª Câmara) | Conferir o enunciado e a situação atual na Pesquisa de Jurisprudência do TCU |
| EXT-MTE-NR15, EXT-MTE-NR16, itens dos Anexos VI-B e VII-A de EXT-IN5-2017 | Acrescentados ou detalhados na fase 3; as páginas não foram abertas | Conferir o anexo e os itens citados no portal do MTE e no Portal de Compras |
