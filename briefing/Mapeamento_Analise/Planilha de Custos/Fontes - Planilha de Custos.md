# Fontes - Planilha de Custos

Este mapa diz, para cada módulo e submódulo de `Estrutura - Planilha de Custos.md`, **onde buscar a prova e o fundamento** antes de decidir se uma rubrica da planilha de custos e formação de preços é impugnável. Cada linha cruza a planilha com outro documento do processo (fontes `INT-*`, com a seção a abrir), aponta as fontes externas pelo ID do `01 - Catalogo de Fontes.md` (o texto, a esfera e o status ficam lá) e fecha com o critério de decisão. Os módulos 1 a 6 seguem os 6 grupos de vícios de `Analise - Planilha de Custos.md` (grupo 1 → Módulo 1; grupo 2 → Módulo 2; grupo 3 → Módulo 3; grupo 4 → Submódulos 2.1 e 4.1; grupo 5 → Módulo 5; grupo 6 → Módulo 6); o que vem só da Estrutura está marcado **[derivada da Estrutura]**, e a seção 7 reúne os cruzamentos da planilha como um todo (quantitativos, publicidade e preço final), que voltam dos mapas do Edital, do TR e do ETP. O foco da Servfaz são os serviços com dedicação exclusiva de mão de obra: CCT vigente, declaração de custos trabalhistas, repactuação, conta vinculada, aviso prévio após o 1º ano, duplicidade entre os Submódulos 2.1 e 4.1-A e a tributação do ano do orçamento (reoneração da folha e reforma tributária). Antes de citar uma fonte `a conferir` em peça, confira-a no catálogo; as fontes só históricas (`EXT-LC110-GERAL`) servem para datar a regra, não para fundamentar.

**Como usar:** leia a pergunta-chave, abra a planilha no módulo indicado e as fontes internas na seção indicada, e extraia o que a coluna "Prova" pede. Anote sempre a **data-base do orçamento** (mês de referência da planilha, `EXT-LEI14133-ART25`, § 7º): a CCT, a alíquota da contribuição sobre a folha e o regime de tributos sobre o faturamento são os vigentes nessa data, e a mudança posterior se resolve por repactuação, não por impugnação. Para toda seção, confira também `INT-RERI`: uma errata pode ter trocado a planilha. O modelo de 6 módulos é o federal (`EXT-IN5-2017`, com `EXT-IN7-2018`), que `EXT-IN98-2022` **autoriza** aplicar às contratações do regime atual no que couber; estados e municípios podem ter modelo próprio (`EXT-REG-ENTE`). Erro na planilha de referência pede **retificação e reabertura do prazo** (`EXT-LEI14133-ART55`, § 1º); a impugnação vai contra o edital, de que a planilha é anexo, até 3 dias úteis antes da abertura (`EXT-LEI14133-ART164`, `EXT-LEI14133-ART183`; ver `Fontes - Edital.md`, seção 9).

---

## 1. Módulo 1: Composição da Remuneração Direta

Base: `Analise - Planilha de Custos.md`, grupo 1.

Pergunta-chave: "O salário-base e os adicionais do Módulo 1 seguem a CCT vigente na data-base do orçamento e as condições do posto descritas no TR?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Salário-base: CCT vigente e categoria certa (1.1) | INT-PLANILHA (Módulo 1; submódulo 1.1; data-base do orçamento); INT-TR (seção IV, categoria e local); INT-EDITAL (seções 5 e 7) | EXT-NORMA-CCT, EXT-BASE-MEDIADOR, EXT-LEI14133-ART23, EXT-LEI14133-ART18 (caput, IV), EXT-LEI14133-ART59 (III) | CCT registrada no Mediador para a categoria e a base territorial do local de execução, com vigência, data-base e piso, ao lado do piso usado na planilha e da data-base do orçamento | Piso de CCT vencida quando a nova já estava registrada na data-base do orçamento, ou CCT de outra categoria ou base territorial: propostas que cobrem o piso certo ficam acima do teto (EXT-LEI14133-ART59, III) | Piso igual ao da CCT vigente na data-base; nova CCT registrada depois dessa data (caso de repactuação, ver linha abaixo) |
| CCT nova depois do orçamento: repactuação | INT-PLANILHA (Módulo 1; data-base do orçamento); INT-MINUTA (cl. 3) | EXT-LEI14133-ART25 (§ 8º, II), EXT-LEI14133-ART135 (I e II), EXT-LEI14133-ART92 (X), EXT-NORMA-CCT | Data de registro da CCT nova; cláusula de repactuação da Minuta com a data-base vinculada à convenção | Minuta sem repactuação em dedicação exclusiva, ou com data-base diferente da do instrumento coletivo (detalhe em `Fontes - Minuta Contratual.md`, cl. 3) | Repactuação prevista com data-base da CCT; a defasagem posterior se resolve na execução |
| Declaração de custos trabalhistas x piso defasado | INT-EDITAL (seção 5); INT-PLANILHA (Módulo 1); INT-TR (seção IV) | EXT-LEI14133-ART63 (§ 1º), EXT-NORMA-CCT | Modelo de declaração exigido no edital ao lado do piso da planilha | A declaração exige cobrir a CCT, mas o teto da planilha só comporta o piso antigo (declaração inviável; ver `Fontes - Edital.md`, seção 5) | Teto compatível com a CCT vigente |
| Adicional de periculosidade (1.2) | INT-PLANILHA (Módulo 1; submódulo 1.2); INT-TR (seção IV, condições do posto) | EXT-CLT-ART193, EXT-MTE-NR16 (Anexo III, segurança patrimonial), EXT-NORMA-CCT | Atividade descrita no TR (vigilância armada, eletricidade, motocicleta) ao lado do valor do 1.2; base de cálculo usada | TR descreve atividade perigosa e o 1.2 está zerado, ou 30% calculado sobre base diferente do salário-base | Atividade sem enquadramento em EXT-MTE-NR16, ou adicional correto |
| Adicional de insalubridade e base de cálculo (1.3) | INT-PLANILHA (Módulo 1; submódulo 1.3); INT-TR (seção IV, local e tarefas) | EXT-CLT-ART192, EXT-MTE-NR15 (Anexo 14), EXT-TST-SUM448, EXT-STF-SV4, EXT-NORMA-CCT | Tarefas do TR (sanitários de uso público ou coletivo de grande circulação, coleta de lixo, áreas hospitalares) ao lado do grau e da base do 1.3; cláusula da CCT sobre a base | TR com limpeza de sanitários de grande circulação ou coleta de lixo e 1.3 zerado ou em grau inferior ao de EXT-MTE-NR15 e EXT-TST-SUM448; base no piso quando a CCT não manda, ou no salário mínimo quando a CCT manda o piso | Grau e base coerentes com EXT-MTE-NR15, EXT-TST-SUM448 e a CCT |
| Adicional noturno e hora reduzida (1.4) [derivada da Estrutura no detalhe da hora ficta] | INT-PLANILHA (Módulo 1; submódulo 1.4); INT-TR (seção IV, escala e horário) | EXT-CLT-ART73 (caput e § 1º), EXT-TST-SUM60, EXT-NORMA-CCT | Horário do posto no TR; cálculo do 1.4 (20% e fator de 52min30s) e, se a jornada noturna se prorroga, o adicional nas horas prorrogadas | Posto noturno sem adicional, adicional sem o fator da hora reduzida, ou percentual abaixo do da CCT | Cálculo com 20% (ou o da CCT) e hora reduzida |
| DSR sobre adicionais e horas extras habituais (1.5) | INT-PLANILHA (Módulo 1; submódulo 1.5) | EXT-TST-SUM172, EXT-TST-SUM60 (I) | Se há reflexo em DSR para o adicional noturno habitual e as horas extras habituais da escala | Escala com noturno ou extra habitual e sem reflexo em DSR | Escala sem noturno nem extra habitual, ou reflexo calculado |
| Gratificações e adicionais convencionais (1.6) | INT-PLANILHA (Módulo 1; submódulo 1.6); INT-TR (seções IV e V, líder ou encarregado) | EXT-NORMA-CCT, EXT-BASE-MEDIADOR | Cláusulas econômicas da CCT (função, assiduidade, triênio) ao lado das linhas do 1.6; posto de líder exigido no TR | Adicional obrigatório da CCT omitido, ou TR exige encarregado e a planilha não tem a gratificação de função | Planilha traz todos os adicionais obrigatórios da CCT para os postos do TR |

---

## 2. Módulo 2: Encargos e Benefícios Anuais, Mensais e Diários

Base: `Analise - Planilha de Custos.md`, grupos 2 e 4.

Pergunta-chave: "As provisões, os encargos sobre a folha e os benefícios do Módulo 2 seguem a lei, o código FPAS da atividade, o regime de contribuição do ano da data-base e as cláusulas sociais da CCT?"

### 2.1 Submódulo 2.1: 13º salário, férias e adicional de férias

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Provisão de 13º e férias com 1/3 [derivada da Estrutura nos percentuais] | INT-PLANILHA (Módulo 2; submódulo 2.1) | EXT-IN5-2017 (Anexo VII-D), EXT-REG-ENTE | Percentuais do 2.1 e base de incidência (Módulo 1) | Percentual abaixo do devido ou base sem os adicionais do Módulo 1 | Percentuais do modelo, sobre a remuneração do Módulo 1 |
| Duplicidade 2.1 x 4.1-A (férias) | INT-PLANILHA (Módulo 2, submódulo 2.1; Módulo 4, submódulo 4.1, alínea A); INT-PLANILHA (vigência: 1º ano ou prorrogação) | EXT-ADM-MEC-2024, EXT-IN5-2017 (Anexo VII-D), EXT-LEI14133-ART5, EXT-LEI14133-ART11 (III) | Fórmulas do 2.1 e do 4.1-A lado a lado e o ano de contrato a que a planilha se refere; valor da duplicidade por posto e no total | As duas rubricas cobrem o mesmo custo (no 1º ano, férias no 2.1 e substituto de férias também cheio no 4.1-A), inflando o teto | Uma das duas provisões zerada ou reduzida conforme o ano de contrato, na lógica de EXT-ADM-MEC-2024 |

### 2.2 Submódulo 2.2: GPS, FGTS e outras contribuições

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Terceiros conforme o FPAS da atividade | INT-PLANILHA (Módulo 2; submódulo 2.2); INT-TR (seção I, atividade) | EXT-BASE-FPAS, EXT-BASE-CNAE, EXT-LEI14133-ART5 | Código FPAS da atividade (limpeza e conservação: 515) e total de terceiros da tabela ao lado das linhas de Salário-Educação, INCRA, Sistema S e SEBRAE | Alíquotas de outro FPAS (indústria em vez de serviços), ou SEBRAE somado duas vezes | Total de terceiros igual ao da tabela do FPAS correto |
| Contribuição patronal no ano da data-base (reoneração) | INT-PLANILHA (Módulo 2, submódulo 2.2; Módulo 6, submódulo 6.3; data-base) | EXT-LEI14973-GERAL, EXT-LEI12546-GERAL, EXT-LEI14133-ART25 (§ 7º) | Ano da data-base do orçamento; se a atividade está entre as desoneradas; alíquota sobre a folha no 2.2 e CPRB no 6.3 | Planilha de atividade desonerada que zera a contribuição sobre a folha em 2025-2027 (a transição exige 5%, 10% e 15%), ou que aplica 20% cheio com CPRB ao mesmo tempo | Alíquotas coerentes com o ano da data-base (em 2026: 10% sobre a folha e CPRB a 60%), ou atividade fora da desoneração com 20% |
| FGTS, RAT e FAP | INT-PLANILHA (Módulo 2; submódulo 2.2) | EXT-BASE-FPAS, EXT-REG-ENTE | FGTS de 8%; RAT da atividade e FAP adotado (neutro 1,0 no orçamento) | FGTS diferente de 8%, ou RAT de outra atividade sem justificativa | Percentuais legais e RAT da atividade |

### 2.3 Submódulo 2.3: Benefícios mensais e diários

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Vale-transporte sem o desconto legal | INT-PLANILHA (Módulo 2; submódulo 2.3); INT-TR (seção IV, local e dias trabalhados) | EXT-LEI7418-GERAL, EXT-LEI14133-ART11 (III) | Tarifa, viagens e dias na memória do 2.3 e se o desconto de 6% do salário-base foi abatido | Valor integral das passagens sem o desconto (sobrepreço) | Só a diferença paga pelo empregador |
| Benefícios obrigatórios da CCT omitidos | INT-PLANILHA (Módulo 2; submódulo 2.3); INT-EDITAL (seção 7) | EXT-NORMA-CCT, EXT-BASE-MEDIADOR, EXT-LEI14133-ART5, EXT-LEI14133-ART63 (§ 1º) | Cláusulas sociais da CCT (alimentação, saúde, odontológico, seguro de vida) ao lado das linhas do 2.3 | Benefício obrigatório da CCT ausente ou abaixo do valor convencional: propostas deixam de ser comparáveis e o teto não comporta o custo (ver `Fontes - Edital.md`, seção 7, CCT) | Todos os benefícios obrigatórios da CCT presentes |

---

## 3. Módulo 3: Provisão para Rescisão

Base: `Analise - Planilha de Custos.md`, grupo 3.

Pergunta-chave: "A provisão de rescisão usa só o que a lei manda hoje, trata o aviso prévio conforme o ano de contrato e conversa com a conta vinculada da Minuta?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Multa do FGTS com os 10% extintos (3.3) | INT-PLANILHA (Módulo 3; submódulo 3.3) | EXT-LEI13932-ART12, EXT-LC110-GERAL (histórica), EXT-STF-TEMA846 | Fórmula da célula da multa: 40% ou 50% sobre os depósitos | Provisão calculada sobre 50% em orçamento com data-base a partir de 2020 (sobrepreço) | Provisão sobre 40% |
| Aviso prévio trabalhado após o 1º ano (3.1) | INT-PLANILHA (Módulo 3; submódulo 3.1; ano de contrato da planilha); INT-MINUTA (cl. 1, prorrogação) | EXT-TCU-AC1186-2017 (itens 9.1.1 e 9.2) | Percentual do aviso trabalhado na planilha do 1º ano e a regra prevista para as prorrogações | Planilha ou regra contratual que mantém o aviso prévio trabalhado cheio nas prorrogações (sobrepreço a partir do 2º ano) | Aviso trabalhado só no 1º ano (1,94% como parâmetro prático), com a regra de exclusão ou redução nas prorrogações |
| Aviso prévio indenizado e proporcional (3.2) | INT-PLANILHA (Módulo 3; submódulo 3.2); INT-TR (seção I, vigência) | EXT-LEI12506-GERAL | Fração para os 3 dias por ano de serviço em contrato com vigência ou prorrogação acima de 1 ano | Contrato plurianual sem a fração proporcional (subdimensionamento) | Fração prevista, ou contrato de até 1 ano |
| Reflexos do aviso em 13º e férias (3.4) [derivada da Estrutura] | INT-PLANILHA (Módulo 3; submódulo 3.4) | EXT-IN5-2017 (Anexo VII-D), EXT-REG-ENTE | Linha de reflexos do aviso indenizado | Reflexo omitido no modelo que o prevê | Reflexo calculado |
| Provisões x conta vinculada e pagamento direto | INT-PLANILHA (Módulos 2 e 3); INT-MINUTA (cl. 2); INT-TR (seção VI) | EXT-LEI14133-ART121 (§ 3º) | Rubricas provisionadas (13º, férias, multa do FGTS) ao lado da previsão de conta vinculada ou pagamento direto na Minuta | Minuta de dedicação exclusiva que retém valores além das provisões da planilha, ou sem o mecanismo e sem justificativa (detalhe em `Fontes - Minuta Contratual.md`, cl. 2) | Retenção limitada às provisões, com regra de liberação |

---

## 4. Módulo 4: Custo de Reposição do Profissional Ausente

Base: `Analise - Planilha de Custos.md`, grupo 4 (duplicidade e escala 12x36); as alíneas B a F e o Submódulo 4.2 vêm da Estrutura.

Pergunta-chave: "A reposição cobre só as ausências reais do posto, sem repetir custo do Submódulo 2.1, e segue a escala de trabalho do TR?"

### 4.1 Submódulo 4.1: Substituto nas ausências legais

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Substituto de férias (4.1-A) x provisão do 2.1 | INT-PLANILHA (Módulo 4, submódulo 4.1, alínea A; Módulo 2, submódulo 2.1) | EXT-ADM-MEC-2024, EXT-IN5-2017 (Anexo VII-D) | Ver Submódulo 2.1, linha "Duplicidade 2.1 x 4.1-A" | Ver Submódulo 2.1 | Ver Submódulo 2.1 |
| Escala 12x36 x fórmula de 44 horas | INT-PLANILHA (Módulo 4; submódulo 4.1); INT-TR (seção IV, escala) | EXT-NORMA-CCT, EXT-LEI14133-ART5 | Escala do TR ao lado dos dias de ausência usados nas alíneas B a F | Posto 12x36 com reposição calculada como jornada de 44 horas semanais (superestima substitutos) | Fórmula ajustada à escala do posto |
| Ausências legais, paternidade e outras (4.1-B, C e F) [derivada da Estrutura] | INT-PLANILHA (Módulo 4; submódulo 4.1, alíneas B, C e F) | EXT-CLT-ART473, EXT-NORMA-CCT | Dias de ausência remunerada na lei e na CCT ao lado dos percentuais | Ausência obrigatória da CCT sem cobertura, ou percentual sem memória de cálculo | Percentuais com memória, coerentes com a lei e a CCT |
| Acidente de trabalho e maternidade (4.1-D e E) [derivada da Estrutura] | INT-PLANILHA (Módulo 4; submódulo 4.1, alíneas D e E) | EXT-IN5-2017 (Anexo VII-D) | Percentuais e memória de cálculo | — (sem fonte própria no catálogo; percentual sem memória pede esclarecimento) | Memória de cálculo apresentada |
| Prazo de substituição do empregado ausente | INT-TR (seções IV e VII); INT-PLANILHA (Módulo 4) | EXT-LEI14133-ART18 (caput, IV) | Prazo de reposição exigido no TR ao lado da cobertura do Módulo 4 | TR exige reposição imediata e o Módulo 4 não prevê substituto para a ausência (ver `Fontes - Termo de Referencia.md`, seção IV) | Módulo 4 cobre as ausências que o TR manda repor |

### 4.2 Submódulo 4.2: Substituto na intrajornada [derivada da Estrutura]

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Cobertura do intervalo do posto ininterrupto | INT-PLANILHA (Módulo 4; submódulo 4.2); INT-TR (seção IV, posto que não pode ficar vazio) | EXT-IN5-2017 (Anexo VII-D, Módulo 4, 4.2), EXT-NORMA-CCT | Se o TR exige posto ininterrupto e se o 4.2 tem valor | TR exige cobertura contínua e o 4.2 está zerado (custo do TR sem planilha) | Posto pode parar no intervalo, ou 4.2 calculado |

---

## 5. Módulo 5: Insumos Diversos

Base: `Analise - Planilha de Custos.md`, grupo 5.

Pergunta-chave: "Todo uniforme, EPI, material e equipamento exigido no TR tem linha e custo no Módulo 5?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Obrigação do TR sem custo na planilha | INT-TR (seções III, IV e VII); INT-PLANILHA (Módulo 5; submódulos 5.1 a 5.3; Módulo 4, substitutos) | EXT-LEI14133-ART6 (XXIII, "i"), EXT-LEI14133-ART23, EXT-LEI14133-ART18 (caput, IV) | Lista de equipamentos, veículos e materiais do TR lado a lado com as linhas do Módulo 5 | Item exigido no TR com custo zero ou ausente (ver `Fontes - Termo de Referencia.md`, seção VII) | Todo item do TR tem linha e custo |
| Uniformes e EPIs por vida útil (5.1) [derivada da Estrutura na fórmula] | INT-PLANILHA (Módulo 5; submódulo 5.1); INT-TR (seção IV) | EXT-NORMA-CCT, EXT-MTE-NR15, EXT-MTE-NR16, EXT-MERC-COTACOES | Quantidade, preço e vida útil por peça; EPI exigido pelo risco do posto e pela CCT | Valor arbitrário sem memória, ou EPI do risco descrito no TR ausente | Memória por vida útil com todos os itens |
| Materiais de consumo e frete (5.2) | INT-PLANILHA (Módulo 5; submódulo 5.2); INT-TR (seção IV, locais, rotas e área) | EXT-MERC-COTACOES, EXT-BASE-PESQPRECOS | Consumo estimado por posto ou por m², frete e diárias para os polos do TR | Consumo sem memória, ou locais do TR sem custo de deslocamento | Consumo e deslocamento com memória |
| Máquinas e equipamentos (5.3) | INT-PLANILHA (Módulo 5; submódulo 5.3); INT-TR (seção III) | EXT-MERC-COTACOES, EXT-MERC-FICHAS | Locação de mercado ou depreciação + manutenção para cada equipamento do TR | Equipamento do TR sem depreciação ou locação | Custo mensal calculado |
| Cláusula "guarda-chuva" (lista aberta) | INT-TR (seção VII); INT-PLANILHA (Módulo 5) | EXT-LEI14133-ART18 (caput, IV), EXT-LEI14133-ART6 (XXIII) | Obrigação genérica do TR ("todos os materiais necessários") ao lado do que o Módulo 5 precifica | Lista aberta no TR sem correspondência quantificada no Módulo 5 (ver `Fontes - Termo de Referencia.md`, seção VII) | Lista fechada e precificada |
| Posto x produtividade e produtividade de referência | INT-TR (seções IV e VI); INT-PLANILHA (Módulos 1, 4 e 5; quantidade de postos); INT-ETP (incisos IV e VII) | EXT-IN5-2017 (Anexo VI-B, item 3; Anexo VII-A, item 7.3) | Área ou volume do TR, produtividade adotada e número de postos da planilha | Número de postos incoerente com a produtividade de referência, sem justificativa (ver `Fontes - Termo de Referencia.md`, seção IV) | Postos calculados pela produtividade, ou diferença justificada |

---

## 6. Módulo 6: Custos Indiretos, Lucro e Tributos

Base: `Analise - Planilha de Custos.md`, grupo 6; os percentuais de custos indiretos e lucro e o desdobramento da reforma tributária vêm da Estrutura.

Pergunta-chave: "O Módulo 6 aplica só tributos devidos, no regime do ano da data-base, calculados por dentro, sem IRPJ e CSLL no orçamento-base?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| IRPJ e CSLL no orçamento-base (6.3) | INT-PLANILHA (Módulo 6; submódulo 6.3) | EXT-TCU-SUM254 | Linhas tributárias do Módulo 6 | IRPJ ou CSLL incluídos no BDI do orçamento-base (pedido: retificação; EXT-TCU-SUM254 não proíbe o licitante de cobri-los com o lucro) | Só tributos sobre o faturamento |
| ISS do município competente (6.3) | INT-PLANILHA (Módulo 6; submódulo 6.3); INT-TR (seção IV, local da prestação) | EXT-LC116-ART3, EXT-ISS-MUNICIPAL | Item da lista de serviços (limpeza 7.10, vigilância 11.02), município competente e alíquota da lei municipal | Alíquota de outro município ou de outro item da lista | Alíquota do município competente para o item |
| PIS e Cofins: regime e alíquota efetiva (6.3) [derivada da Estrutura na alíquota efetiva] | INT-PLANILHA (Módulo 6; submódulo 6.3) | EXT-REG-ENTE, EXT-LEI14133-ART5 | Regime adotado (cumulativo ou não) e se o não cumulativo usa alíquota efetiva | Alíquota nominal do não cumulativo sem créditos, ou regime que impede a comparação das propostas | Regime declarado e alíquota coerente |
| Reforma tributária no ano da data-base | INT-PLANILHA (Módulo 6, submódulo 6.3; data-base); INT-MINUTA (cl. 3) | EXT-LC214-ART348, EXT-LEI14133-ART25 (§ 7º), EXT-LEI14133-ART124 (II, "d") | Ano da data-base; se a planilha de 2026 inclui CBS e IBS e se trata como compensáveis ou dispensados | Em 2026, CBS e IBS somados aos tributos sem compensação (sobrepreço), ou Minuta sem regra para a troca de tributos nos anos seguintes | Tratamento do ano da data-base coerente; mudança posterior por reequilíbrio (EXT-LEI14133-ART124, II, "d") |
| CPRB e contribuição sobre a folha | INT-PLANILHA (Módulo 6, submódulo 6.3; Módulo 2, submódulo 2.2) | EXT-LEI14973-GERAL, EXT-LEI12546-GERAL | Ver Submódulo 2.2, "Contribuição patronal no ano da data-base" | Ver Submódulo 2.2 | Ver Submódulo 2.2 |
| Cálculo por dentro (gross-up) | INT-PLANILHA (Módulo 6; preço final) | EXT-LEI14133-ART59 (§§ 2º a 4º) | Fórmula: custo + indiretos + lucro dividido por (1 − tributos) | Tributos somados por fora: o preço final não cobre os tributos da nota e o teto fica subdimensionado | Cálculo por dentro |
| Custos indiretos e lucro (6.1 e 6.2) [derivada da Estrutura] | INT-PLANILHA (Módulo 6; submódulos 6.1 e 6.2); INT-EDITAL (seção 7) | EXT-TCU-AC2460-2022, EXT-TCU-AC465-2024, EXT-TCU-AC214-2025 | Percentuais do órgão; se o edital desclassifica por percentual de BDI ou só pelo preço final | Edital desclassifica proposta só porque o percentual de indiretos ou lucro excede o da planilha (ver `Fontes - Edital.md`, seção 7, BDI) | Análise pelo preço final, com chance de demonstrar a exequibilidade |
| Preposto como custo indireto ou posto | INT-TR (seção V); INT-PLANILHA (Módulo 1 ou submódulo 6.1) | EXT-LEI14133-ART118 | Onde a planilha precifica o preposto exigido no TR | TR exige preposto exclusivo e fixo e a planilha não o precifica, nem como posto nem nos indiretos (ver `Fontes - Termo de Referencia.md`, seção V) | Preposto precificado coerente com o TR |

---

## 7. A planilha como um todo: quantitativos, publicidade e preço final [derivada da Estrutura]

Base: fluxograma de `Estrutura - Planilha de Custos.md` e roteiro final de `Analise - Planilha de Custos.md` (pedido de retificação e reabertura); linhas de volta dos mapas do Edital, do TR e do ETP.

Pergunta-chave: "A planilha foi publicada com o edital, seus quantitativos e seu preço final batem com o Edital, o TR, o ETP e a Pesquisa, e o teto comporta as obrigações?"

| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Quantitativos de postos ou itens | INT-PLANILHA (quantidade de postos; o Módulo 6 dá só o preço unitário); INT-EDITAL (seção 2); INT-TR (seções I e IV); INT-ETP (inciso IV) | EXT-TCU-SUM177, EXT-LEI14133-ART18 (§ 1º, IV) | Tabela lado a lado: postos ou itens em cada documento | Quantidade da planilha diferente do Edital, do TR ou da memória do ETP (ver `Fontes - ETP.md`, inciso IV) | Quantitativos idênticos |
| Preço final x teto, pesquisa e ETP | INT-PLANILHA (Módulo 6, preço final); INT-EDITAL (seção 7); INT-TR (seção IX); INT-ETP (inciso VI); INT-PESQUISA (item 3, mapa de preços) | EXT-LEI14133-ART23, EXT-LEI14133-ART59 (III) | Preço final unitário e global da planilha ao lado do teto do edital, do valor do TR e do ETP e do mapa de preços | Teto do edital diferente do preço final da planilha sem explicação, ou abaixo do custo da própria planilha | Valores coerentes (o do ETP é preliminar) |
| Memória de cálculo e documento da estimativa | INT-PLANILHA (Módulos 1 a 6); INT-TR (seção IX); INT-PESQUISA (item 3, tratamento dos dados) | EXT-LEI14133-ART6 (XXIII, "i"), EXT-LEI14133-ART18 (caput, IV), EXT-LEI14133-ART54, EXT-LEI12527-GERAL | Se há planilha com composição de custos ou só valor global | Estimativa de serviço com mão de obra sem composição de custos no processo, com a ausência demonstrada; se classificada, pedir antes esclarecimento ou acesso | Planilha completa, no edital ou em documento acessível |
| Valor x obrigações do TR e CCT | INT-PLANILHA (Módulos 1 a 6); INT-TR (seções IV e VII) | EXT-LEI14133-ART11 (III), EXT-LEI14133-ART23, EXT-NORMA-CCT, EXT-BASE-MEDIADOR | Soma do custo das obrigações do TR e da CCT vigente ao lado do valor estimado | Valor que não cobre as obrigações ou a CCT, induzindo preço inexequível (ver `Fontes - Termo de Referencia.md`, seção IX) | Valor cobre tudo |
| Orçamento sigiloso | INT-EDITAL (seção 3); INT-TR (seção IX); INT-PLANILHA (Módulos 1 a 6) | EXT-LEI14133-ART24, EXT-LEI12527-GERAL | Justificativa do sigilo; se quantitativos e dados necessários à proposta (CCT, escala, insumos) foram divulgados | Sigilo sem justificativa ou que oculta os dados para montar a planilha da proposta | Sigilo motivado com os dados da proposta públicos |
| Planilha não divulgada com o edital | INT-EDITAL (seção 13); INT-PLANILHA | EXT-LEI14133-ART25 (§ 3º), EXT-BASE-PNCP, EXT-BASE-COMPRASGOV | Rol de anexos ao lado dos arquivos no PNCP, com data | Planilha prevista e ausente, publicada depois ou só com cadastro (ver `Fontes - Edital.md`, seção 13) | Publicada no mesmo dia, sem cadastro |
| Modelo de planilha do ente | INT-PLANILHA; INT-EDITAL (seção 5, modelo de proposta) | EXT-IN5-2017, EXT-IN7-2018, EXT-IN98-2022, EXT-REG-ENTE | Qual modelo o edital adota e se a planilha de referência o segue | Edital exige da proposta modelo diferente do da planilha de referência, ou mistura modelos | Modelo único e declarado |
| Valor por item e cota de ME/EPP | INT-EDITAL (seção 4); INT-PLANILHA (valor por item ou lote) | EXT-LC123-ART48 | Valor estimado de cada item ao lado do limite para item exclusivo | Item até o limite sem exclusividade e sem justificativa (ver `Fontes - Edital.md`, seção 4) | Item acima do limite, ou exceção justificada |
| Intervalo mínimo entre lances | INT-EDITAL (seção 6); INT-PLANILHA (valor do item) | EXT-LEI14133-ART57 | Intervalo do edital ao lado do valor estimado do item | Intervalo desproporcional ao valor do item (ver `Fontes - Edital.md`, seção 6) | Intervalo proporcional |
| Obras e serviços de engenharia | INT-EDITAL (seção 7); INT-PLANILHA | EXT-LEI14133-ART23 (§ 2º), EXT-BASE-SINAPI, EXT-BASE-SICRO | Se o objeto é de engenharia e se a planilha usa as tabelas oficiais | Engenharia orçada pelo modelo de 6 módulos ou sem SINAPI/SICRO (ver `Fontes - Edital.md`, seção 7) | Objeto não é de engenharia, ou tabelas oficiais usadas |
| IMR e glosa sobre o preço do posto | INT-TR (seções IV e VI); INT-PLANILHA (Módulo 6, preço final do posto) | EXT-LEI14133-ART143 | Glosas do IMR ao lado do preço do posto | Glosa que supera a fração do preço correspondente à falha (ver `Fontes - Termo de Referencia.md`, seção VI) | Glosa proporcional |

---

## Matriz resumo

✓ = cruzamento usado na seção. Na coluna `INT-EDITAL`, o número indica a seção do edital (numeração de `Edital/Estrutura - Edital.md`); na coluna `INT-TR`, o algarismo romano indica a seção do TR; na coluna `INT-ETP`, o inciso do ETP; na coluna `INT-PLANILHA`, outro módulo da própria planilha; na coluna `INT-PESQUISA`, o item de `Estrutura - Pesquisa de Precos.md`; na coluna `INT-MINUTA`, a cláusula. `INT-RERI` vale para todas as seções (ver "Como usar").

| Seção | INT-EDITAL | INT-TR | INT-ETP | INT-PLANILHA | INT-PESQUISA | INT-MINUTA | INT-RERI | Externas principais |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1. Módulo 1 | 5, 7 | IV, V | — | — | — | 3 | — | EXT-NORMA-CCT, EXT-BASE-MEDIADOR, EXT-TST-SUM448 |
| 2. Módulo 2 (2.1 a 2.3) | 7 | I, IV | — | 1, 4, 6 | — | — | — | EXT-ADM-MEC-2024, EXT-BASE-FPAS, EXT-LEI14973-GERAL |
| 3. Módulo 3 | — | I, VI | — | 2 | — | 1, 2 | — | EXT-LEI13932-ART12, EXT-TCU-AC1186-2017, EXT-LEI14133-ART121 |
| 4. Módulo 4 (4.1 e 4.2) | — | IV, VII | — | 2 | — | — | — | EXT-ADM-MEC-2024, EXT-CLT-ART473, EXT-IN5-2017 |
| 5. Módulo 5 | — | III, IV, VI, VII | IV, VII | 1, 4 | — | — | — | EXT-LEI14133-ART6, EXT-LEI14133-ART23, EXT-IN5-2017 |
| 6. Módulo 6 | 7 | IV, V | — | 1, 2 | — | 3 | — | EXT-TCU-SUM254, EXT-LC116-ART3, EXT-LC214-ART348 |
| 7. Planilha como um todo [derivada] | 2, 3, 4, 5, 6, 7, 13 | I, IV, VI, VII, IX | IV, VI | 1 a 6 | 3 | — | — | EXT-LEI14133-ART23, EXT-LEI14133-ART24, EXT-LEI14133-ART25 |
