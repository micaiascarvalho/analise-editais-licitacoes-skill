# Fontes - Pesquisa de Preços

Este mapa diz, para cada parte de `Estrutura - Pesquisa de Precos.md` e para cada vício de `Analise - Pesquisa de Precos.md`, **onde buscar a prova e o fundamento** antes de decidir se a pesquisa de preços (mapa comparativo de cotações) é impugnável. Cada linha cruza a pesquisa com outro documento do processo (fontes `INT-*`, com a seção a abrir), aponta as fontes externas pelo ID do `01 - Catalogo de Fontes.md` (o texto, a esfera e o status ficam lá) e fecha com o critério de decisão. As seções 1 a 5 são os 5 parâmetros de `EXT-LEI14133-ART23` (§ 1º, I a V); as seções 6 e 7 são os requisitos de validade e o tratamento matemático (itens 2 e 3 da Estrutura), e a seção 8 reúne os cruzamentos da pesquisa com o resto do processo, que voltam dos mapas do Edital, do TR e do ETP. As seções 1 a 8 vêm só da Estrutura e estão marcadas **[derivada da Estrutura]**; as seções 9 a 13 são os 5 vícios da Análise e o checklist final. Antes de citar uma fonte `a conferir` em peça, confira-a no catálogo; `EXT-IN5-2014` é só histórica.

**Como usar:** leia a pergunta-chave, abra o mapa de preços no item indicado e as fontes internas na seção indicada, e extraia o que a coluna "Prova" pede. Para bens e serviços em geral **não há ordem obrigatória** de parâmetros (`EXT-LEI14133-ART23`, § 1º: "combinada ou não"); a prioridade aos parâmetros I e II, os métodos estatísticos e o descarte de valores vêm do regulamento (`EXT-IN65-ART5` e `EXT-IN65-ART6`, só na União), e estados e municípios podem ter regulamento próprio (`EXT-REG-ENTE`). Obras e serviços de engenharia seguem `EXT-LEI14133-ART23` (§ 2º), com `EXT-BASE-SINAPI` e `EXT-BASE-SICRO` (seção 1). O Painel de Preços deixou de ser atualizado e saiu do catálogo: a base oficial é `EXT-BASE-PESQPRECOS`, ao lado do `EXT-BASE-PNCP`. A pesquisa costuma ser documento da fase preparatória; se não foi publicada, peça esclarecimento ou acesso (`EXT-LEI14133-ART54`, `EXT-LEI12527-GERAL`) dentro do prazo de impugnação (`EXT-LEI14133-ART164`, `EXT-LEI14133-ART183`; ver `Fontes - Edital.md`, seção 9). Erro na pesquisa pede **retificação do valor estimado e reabertura do prazo** (`EXT-LEI14133-ART55`, § 1º). Para toda seção, confira também `INT-RERI`.

---

## 1. Parâmetro I: sistemas oficiais de preços e Banco de Preços em Saúde [derivada da Estrutura]

Base: `Estrutura - Pesquisa de Precos.md`, item 1, parâmetro I; nota sobre obras.

Pergunta-chave: "O preço tirado de sistema oficial é do mesmo item, está dentro da mediana e, em obra ou serviço de engenharia, vem das tabelas oficiais?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Item consultado e código do catálogo | INT-PESQUISA (item 1, parâmetro I); INT-TR (seção III, especificação) | EXT-BASE-PESQPRECOS, EXT-BASE-BPS, EXT-BASE-CATMAT | Código CATMAT/CATSER usado na consulta ao lado da especificação do TR | Código de outro item ou especificação diferente da do TR | Mesmo item e especificação |
| Preço acima da mediana do sistema | INT-PESQUISA (item 1, parâmetro I; item 3) | EXT-IN65-ART6 (§ 6º), EXT-BASE-PESQPRECOS, EXT-REG-ENTE | Mediana do item na consulta ao lado do preço adotado, quando o preço vem só do parâmetro I | Preço só do parâmetro I acima da mediana do sistema (União, ou ente que adota a mesma regra) | Preço dentro da mediana, ou cesta combinada |
| Obras e serviços de engenharia | INT-PESQUISA (item 1); INT-EDITAL (seção 7); INT-PLANILHA | EXT-LEI14133-ART23 (§ 2º), EXT-BASE-SINAPI, EXT-BASE-SICRO | Se o objeto é de engenharia e se a pesquisa usou as tabelas oficiais na ordem legal | Engenharia orçada pela cesta do § 1º, sem SINAPI ou SICRO | Objeto não é de engenharia, ou tabelas oficiais usadas |

---

## 2. Parâmetro II: contratações similares da Administração [derivada da Estrutura]

Base: `Estrutura - Pesquisa de Precos.md`, item 1, parâmetro II; volta do mapa do ETP, inciso VI.

Pergunta-chave: "As contratações similares usadas são do último ano, do mesmo objeto e porte, e foram atualizadas por índice?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Prazo de 1 ano e índice de atualização | INT-PESQUISA (item 1, parâmetro II; item 2, prazo) | EXT-LEI14133-ART23 (§ 1º, II), EXT-BASE-PNCP, EXT-BASE-IBGE, EXT-BASE-FGV | Data das contratações usadas e índice aplicado | Contratação com mais de 1 ano na data da pesquisa, ou sem atualização | Contratações do último ano, atualizadas |
| Base de preços consultada no ETP e na pesquisa | INT-ETP (inciso VI); INT-PESQUISA (item 1, parâmetros I e II) | EXT-BASE-PNCP, EXT-BASE-PESQPRECOS, EXT-IN65-ART5 (só União) | Fontes citadas no ETP ao lado das usadas na pesquisa definitiva | ETP e pesquisa sem nenhuma contratação similar disponível nas bases, sem justificativa (ver `Fontes - ETP.md`, inciso VI) | Bases consultadas ou ausência justificada |
| Similaridade de objeto, porte e local | INT-PESQUISA (item 1, parâmetro II); INT-TR (seções I e IV) | EXT-LEI14133-ART23 (caput), EXT-BASE-PNCP | Objeto, quantidade e local das contratações usadas ao lado do TR | Contratações de porte ou local muito diferentes, sem ajuste | Contratações comparáveis |

---

## 3. Parâmetro III: mídia especializada, tabelas de referência e sítios eletrônicos [derivada da Estrutura]

Base: `Estrutura - Pesquisa de Precos.md`, item 1, parâmetro III.

Pergunta-chave: "Os preços de mídia, tabela ou site têm data, hora e endereço, e são de tabela oficial ou site de domínio amplo?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Registro de data, hora e URL | INT-PESQUISA (item 1, parâmetro III) | EXT-LEI14133-ART23 (§ 1º, III), EXT-MERC-SITES | Captura de tela ou registro com data, hora e endereço da página | Preço de site sem data, hora ou endereço | Registro completo |
| Tabelas de referência setoriais | INT-PESQUISA (item 1, parâmetro III) | EXT-BASE-FIPE, EXT-BASE-ANP, EXT-BASE-FGV, EXT-MERC-MIDIA | Tabela usada, data de referência e se é a tabela própria do item (veículo, combustível) | Tabela de outro item, de outra região ou desatualizada | Tabela própria e atual |

---

## 4. Parâmetro IV: pesquisa direta com fornecedores [derivada da Estrutura]

Base: `Estrutura - Pesquisa de Precos.md`, item 1, parâmetro IV; os vícios das cotações estão nas seções 9 e 13.

Pergunta-chave: "Há ao menos 3 cotações formais, de até 6 meses antes da divulgação, com justificativa da escolha dos fornecedores?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Número e formalidade das cotações | INT-PESQUISA (item 1, parâmetro IV) | EXT-LEI14133-ART23 (§ 1º, IV), EXT-MERC-COTACOES | Pedido formal, data, CNPJ, assinatura e descrição exata em cada cotação | Menos de 3 cotações, cotação sem CNPJ ou sem descrição, ou sem justificativa da escolha | 3 ou mais cotações formais e justificadas |
| Prazo de 6 meses | INT-PESQUISA (item 1, parâmetro IV; item 2, prazo); INT-EDITAL (seção 1, data de divulgação) | EXT-LEI14133-ART23 (§ 1º, IV) | Data de cada cotação ao lado da data de divulgação do edital | Cotação obtida mais de 6 meses antes da divulgação | Todas dentro do prazo |

---

## 5. Parâmetro V: base nacional de notas fiscais eletrônicas [derivada da Estrutura]

Base: `Estrutura - Pesquisa de Precos.md`, item 1, parâmetro V.

Pergunta-chave: "Se a pesquisa cita notas fiscais, a base existe e é aplicável?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Uso de notas fiscais como parâmetro | INT-PESQUISA (item 1, parâmetro V) | EXT-BASE-NFE, EXT-LEI14133-ART23 (§ 1º, V) | Origem e data das notas citadas | — (base sem regulamentação para pesquisa de preços; nota de origem desconhecida pede esclarecimento) | Parâmetro não usado, ou notas identificadas |

---

## 6. Requisitos de validade de cada cotação [derivada da Estrutura]

Base: `Estrutura - Pesquisa de Precos.md`, item 2; checklist da Análise, perguntas 1, 3 e 4.

Pergunta-chave: "Cada preço do mapa está no prazo do seu parâmetro, é do mesmo objeto do TR e em condições comerciais comparáveis?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Prazo por parâmetro | INT-PESQUISA (item 2, prazo de validade dos dados) | EXT-LEI14133-ART23 (§ 1º, II e IV), EXT-REG-ENTE | Data de cada preço e o parâmetro de origem | Similar com mais de 1 ano ou cotação com mais de 6 meses | Todos no prazo |
| Defasagem entre o ETP e a pesquisa | INT-ETP (inciso VI); INT-PESQUISA (item 2, prazo de validade dos dados) | EXT-LEI14133-ART23, EXT-BASE-IBGE, EXT-BASE-FGV | Data da estimativa do ETP e da pesquisa definitiva | Edital publicado com a estimativa preliminar do ETP, sem pesquisa atualizada (ver `Fontes - ETP.md`, inciso VI) | Pesquisa definitiva recente |
| Identidade do objeto | INT-PESQUISA (item 2); INT-TR (seções I e III) | EXT-TCU-SUM177, EXT-BASE-CATMAT | Descrição de cada cotação ao lado da especificação do TR (marca, potência, garantia, local de entrega) | Preço de item diferente do especificado | Itens idênticos ou estritamente similares |
| Condições comerciais e quantidade | INT-PESQUISA (item 2); INT-TR (seção I, quantitativos) | EXT-LEI14133-ART23 (caput, economia de escala) | Quantidade cotada ao lado da licitada | Cotação de varejo unitário para compra em grande escala (ver seção 10) | Quantidades comparáveis |

---

## 7. Tratamento matemático e mapa de preços [derivada da Estrutura]

Base: `Estrutura - Pesquisa de Precos.md`, item 3; o vício correspondente está na seção 11.

Pergunta-chave: "O mapa tem ao menos 3 preços válidos, descartou os inexequíveis, inconsistentes e excessivos e usou um método admitido pelo regulamento?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Método estatístico | INT-PESQUISA (item 3, mapa de preços) | EXT-IN65-ART6 (caput; só União), EXT-REG-ENTE | Método declarado (média, mediana ou menor valor) e número de preços válidos | Método não previsto no regulamento, ou cálculo com menos de 3 preços sem justificativa | Método do regulamento sobre 3 ou mais preços |
| Descarte de valores | INT-PESQUISA (item 3) | EXT-IN65-ART6 (caput), EXT-LEI14133-ART11 (III) | Critério de descarte e valores mantidos | Valores excessivos ou inexequíveis mantidos no cálculo | Descarte aplicado e motivado |
| Preferência indevida pela mediana | INT-PESQUISA (item 3) | EXT-IN65-ART6 | Justificativa do órgão para o método | — (a IN não dá preferência à mediana; a escolha do método não é vício por si) | — |

---

## 8. A pesquisa no processo: valor, sigilo e publicidade [derivada da Estrutura]

Base: objetivo da Estrutura (fixar o valor estimado ou máximo aceitável); linhas de volta dos mapas do Edital, do TR e do ETP.

Pergunta-chave: "O valor do mapa é o mesmo do TR, da Planilha, do ETP e do teto do edital, e a pesquisa foi publicada ou teve o sigilo motivado?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Coerência do valor entre documentos (teto unitário x pesquisa) | INT-PESQUISA (item 3, mapa de preços); INT-TR (seção IX); INT-ETP (inciso VI); INT-PLANILHA (Módulo 6, preço final); INT-EDITAL (seção 7) | EXT-LEI14133-ART23, EXT-LEI14133-ART59 (III) | Valor de cada item no mapa ao lado do TR, da Planilha, do ETP e do teto do edital | Teto acima do mapa sem explicação, ou abaixo do menor valor da própria pesquisa (ver `Fontes - Termo de Referencia.md`, seção IX) | Valores coerentes (o do ETP é preliminar) |
| Memória de cálculo da estimativa | INT-PESQUISA (item 3, tratamento dos dados); INT-TR (seção IX); INT-PLANILHA (Módulos 1 a 6) | EXT-LEI14133-ART6 (XXIII, "i"), EXT-LEI14133-ART18 (caput, IV) | Se o processo tem o mapa com as fontes e o cálculo | Valor estimado sem mapa nem memória, com a ausência demonstrada | Mapa e memória no processo |
| Orçamento sigiloso | INT-PESQUISA (item 3, mapa de preços); INT-EDITAL (seções 3 e 7); INT-TR (seção IX); INT-ETP (inciso VI) | EXT-LEI14133-ART24, EXT-LEI12527-GERAL | Justificativa do sigilo e dados divulgados | Sigilo sem justificativa ou que oculta dados necessários à proposta | Sigilo motivado |
| Pesquisa não publicada | INT-EDITAL (seção 13); INT-PESQUISA | EXT-LEI14133-ART25 (§ 3º), EXT-LEI14133-ART54, EXT-LEI12527-GERAL, EXT-BASE-PNCP | Rol de anexos e arquivos no PNCP; se a pesquisa é anexo ou documento preparatório | Pesquisa listada como anexo e não publicada (ver `Fontes - Edital.md`, seção 13); se preparatória, pedir acesso antes de impugnar | Publicada, ou acesso pedido no prazo |
| Valor por item e ME/EPP | INT-PESQUISA (item 3, valor por item); INT-EDITAL (seção 4); INT-ETP (inciso VIII) | EXT-LC123-ART48 | Valor estimado de cada item ao lado do limite para item exclusivo | Item até o limite sem exclusividade e sem justificativa (ver `Fontes - Edital.md`, seção 4, e `Fontes - ETP.md`, inciso VIII) | Item acima do limite, ou exceção justificada |
| Pesquisa x planilha de custos (mão de obra) | INT-PESQUISA (item 1); INT-PLANILHA (Módulos 1 a 6) | EXT-NORMA-CCT, EXT-BASE-MEDIADOR | Se o valor de serviço com dedicação exclusiva veio de cotações globais ou da planilha com a CCT | Valor de posto fixado só por cotações, abaixo do custo da CCT vigente na planilha | Valor apoiado na planilha (ver `Fontes - Planilha de Custos.md`, seção 7) |

---

## 9. Vício 1: cotações de cobertura (orçamentos de fachada)

Base: `Analise - Pesquisa de Precos.md`, vício 1; checklist, pergunta 2.

Pergunta-chave: "As empresas que cotaram são independentes entre si e do ramo do objeto?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Vínculo entre cotantes | INT-PESQUISA (item 1, parâmetro IV) | EXT-BASE-CNPJ, EXT-TCU-AC1798-2024, EXT-TCU-AC1616-2023 | Quadro de sócios, endereço, contador, domínio de e-mail e telefone de cada cotante; registrar só o tipo de vínculo, sem nomes nem CPF | Indícios convergentes de vínculo (sócio em comum, mesmo endereço ou contador) entre cotantes; parentesco sozinho não basta | Empresas sem vínculo identificado |
| Ramo compatível com o objeto | INT-PESQUISA (item 1, parâmetro IV); INT-TR (seção I) | EXT-BASE-CNAE, EXT-BASE-CNPJ | CNAE principal e secundários de cada cotante ao lado do objeto | Cotante sem CNAE compatível com o objeto | CNAE compatível |
| Cotação montada para elevar a média | INT-PESQUISA (item 3) | EXT-LEI14133-ART11 (III), EXT-LEI14133-ART23, EXT-TCU-AC1616-2023 | Distância entre as cotações e os parâmetros I e II | Cotações muito acima das bases públicas que puxam o valor estimado | Cotações próximas das bases |

---

## 10. Vício 2: economia de escala invertida (varejo para atacado)

Base: `Analise - Pesquisa de Precos.md`, vício 2; checklist, pergunta 4.

Pergunta-chave: "O preço de referência reflete o volume licitado ou foi tirado do varejo unitário?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Volume licitado x fonte de varejo | INT-TR (seção I, quantitativos); INT-PESQUISA (item 1, parâmetro III) | EXT-LEI14133-ART23 (caput e § 1º), EXT-MERC-SITES | Quantidade licitada ao lado das fontes do mapa (sites de varejo, embalagem unitária) | Compra em grande escala precificada por varejo unitário | Fontes de porte compatível |
| Contratações de mesmo porte | INT-PESQUISA (item 1, parâmetro II) | EXT-BASE-PESQPRECOS, EXT-BASE-PNCP, EXT-TCU-AC2637-2015, EXT-TCU-SUM177 | Contratações homologadas de volume semelhante, com valor e data | Contratações de mesmo porte com preço bem menor, ignoradas | Mapa já considera contratações de porte similar |

---

## 11. Vício 3: falta de expurgo de valores discrepantes

Base: `Analise - Pesquisa de Precos.md`, vício 3; checklist, pergunta 5.

Pergunta-chave: "Refeita a conta sem o valor discrepante, o preço de referência cai?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Recálculo sem o discrepante | INT-PESQUISA (item 3, mapa de preços) | EXT-IN65-ART6 (caput; só União), EXT-REG-ENTE, EXT-LEI14133-ART23 | Mapa refeito com mediana ou com o descarte do valor excessivo; diferença no valor estimado | Valor manifestamente excessivo mantido na média, inflando o teto | Discrepante já descartado, ou diferença irrelevante |

---

## 12. Vício 4: orçamento defasado ou inexequível (teto irreal)

Base: `Analise - Pesquisa de Precos.md`, vício 4; checklist, pergunta 3.

Pergunta-chave: "O teto cobre o custo atual do insumo na data da publicação?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Data da pesquisa x variação do insumo | INT-PESQUISA (item 2, prazo); INT-EDITAL (seção 7, teto) | EXT-BASE-IBGE, EXT-BASE-FGV, EXT-BASE-ANP, EXT-BASE-SINAPI, EXT-MERC-BOLSAS | Índice ou cotação do insumo entre a data da pesquisa e a publicação | Variação relevante não incorporada, deixando o teto abaixo do custo | Variação pequena ou já incorporada |
| Prova do custo atual | INT-PESQUISA (item 3); INT-EDITAL (seção 7) | EXT-MERC-DECLARACOES, EXT-MERC-COTACOES, EXT-LEI14133-ART5, EXT-LEI14133-ART11 (III), EXT-LEI14133-ART59 (III) | Declarações e cotações recentes de fabricantes acima do teto | Custo de fábrica acima do teto (licitação deserta ou proposta inexequível) | Teto acima do custo atual |

---

## 13. Vício 5: fuga dos bancos de dados públicos

Base: `Analise - Pesquisa de Precos.md`, vício 5; checklist, pergunta 6.

Pergunta-chave: "O órgão consultou as bases públicas ou foi direto a cotações locais, sem justificar?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Cesta só de cotações diretas | INT-PESQUISA (item 1, parâmetros I, II e IV) | EXT-LEI14133-ART23 (caput e § 1º, I e II), EXT-IN65-ART5 (§ 1º; só União), EXT-REG-ENTE, EXT-TCU-AC1445-2015 | Fontes do mapa e justificativa para não usar as bases públicas | Pesquisa só com cotações de fornecedores, sem justificativa, quando há registros nas bases (na União, contra a prioridade do regulamento) | Bases consultadas, ou ausência de registros demonstrada |
| Registros ignorados nas bases | INT-PESQUISA (item 1) | EXT-BASE-PESQPRECOS, EXT-BASE-PNCP, EXT-BASE-CATMAT | Consulta pelo código CATMAT/CATSER: contratações recentes, valores e datas | Registros recentes do mesmo item com valores bem menores | Sem registros comparáveis |

---

## Matriz resumo

✓ = cruzamento usado na seção. Na coluna `INT-EDITAL`, o número indica a seção do edital (numeração de `Edital/Estrutura - Edital.md`); na coluna `INT-TR`, a seção do TR; na coluna `INT-ETP`, o inciso do ETP; na coluna `INT-PLANILHA`, o módulo; na coluna `INT-PESQUISA`, o item da própria Estrutura (1: parâmetros; 2: validade; 3: tratamento e mapa). `INT-RERI` vale para todas as seções (ver "Como usar").

| Seção | INT-EDITAL | INT-TR | INT-ETP | INT-PLANILHA | INT-PESQUISA | INT-MINUTA | INT-RERI | Externas principais |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1. Parâmetro I | 7 | III | — | ✓ | 1, 3 | — | — | EXT-BASE-PESQPRECOS, EXT-IN65-ART6, EXT-BASE-SINAPI |
| 2. Parâmetro II | — | I, IV | VI | — | 1, 2 | — | — | EXT-LEI14133-ART23, EXT-BASE-PNCP, EXT-IN65-ART5 |
| 3. Parâmetro III | — | — | — | — | 1 | — | — | EXT-MERC-SITES, EXT-BASE-FIPE, EXT-BASE-ANP |
| 4. Parâmetro IV | 1 | — | — | — | 1, 2 | — | — | EXT-LEI14133-ART23, EXT-MERC-COTACOES |
| 5. Parâmetro V | — | — | — | — | 1 | — | — | EXT-BASE-NFE |
| 6. Requisitos de validade | — | I, III | VI | — | 2 | — | — | EXT-LEI14133-ART23, EXT-TCU-SUM177 |
| 7. Tratamento matemático | — | — | — | — | 3 | — | — | EXT-IN65-ART6, EXT-REG-ENTE |
| 8. Pesquisa no processo | 3, 4, 7, 13 | IX | VI, VIII | 1 a 6 | 1, 3 | — | — | EXT-LEI14133-ART23, EXT-LEI14133-ART24, EXT-LC123-ART48 |
| 9. Cotações de cobertura | — | I | — | — | 1, 3 | — | — | EXT-BASE-CNPJ, EXT-TCU-AC1798-2024, EXT-TCU-AC1616-2023 |
| 10. Economia de escala | — | I | — | — | 1 | — | — | EXT-BASE-PESQPRECOS, EXT-TCU-AC2637-2015 |
| 11. Expurgo de discrepantes | — | — | — | — | 3 | — | — | EXT-IN65-ART6 |
| 12. Teto defasado | 7 | — | — | — | 2, 3 | — | — | EXT-BASE-IBGE, EXT-MERC-DECLARACOES |
| 13. Fuga das bases públicas | — | — | — | — | 1 | — | — | EXT-IN65-ART5, EXT-TCU-AC1445-2015, EXT-BASE-PESQPRECOS |
