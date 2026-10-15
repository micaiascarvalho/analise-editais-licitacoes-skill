Este documento descreve a **anatomia de cada linha (rubrica)** da planilha de custos e formação de preços.

No serviço público brasileiro, o padrão mais rigoroso e utilizado pelos órgãos é o modelo federal instituído pela **IN SEGES/MPDG nº 05/2017**. A **IN SEGES/ME nº 98/2022** não alterou o modelo: ela autoriza a aplicação da IN 5/2017, no que couber, às contratações regidas pela Lei nº 14.133/2021. Esse padrão desdobra a planilha em **6 Módulos com submódulos matemáticos detalhados**.

> **Nota sobre a esfera:** a IN SEGES/MPDG nº 05/2017 e o seu modelo de planilha são normas **federais**. Estados e municípios podem ter modelo próprio ou adotar o federal; confira o regulamento do ente que publicou o edital.

Abaixo está o detalhamento completo de cada módulo, suas subdivisões, fórmulas e segredos práticos:

---

### Módulo 1: Composição da Remuneração Direta

Este módulo apura quanto custa a remuneração direta do trabalhador por mês. Ele é a **base de cálculo de quase todos os percentuais dos módulos seguintes**. Se errar aqui, todo o resto da planilha desmorona.

- **1.1. Salário-Base:**
  - O que é: O piso salarial obrigatório da categoria.
  - Onde checar: **Convenção Coletiva de Trabalho (CCT)** registrada no Ministério do Trabalho e Emprego (MTE).
  - _Ponto crítico:_ Checar a **data-base**. Se a CCT venceu e já houve reajuste em mesa de negociação com efeito retroativo, e o órgão usou a tabela do ano anterior, o salário-base está defasado.
- **1.2. Adicional de Periculosidade:**
  - Regra legal: **30% fixo** calculado estritamente sobre o salário-base (art. 193 da CLT).
  - Quem recebe: Vigilantes armados, eletricistas de alta tensão, frentistas, motoboys.
- **1.3. Adicional de Insalubridade:**
  - Regra legal: Percentuais de **10% (grau mínimo), 20% (grau médio) ou 40% (grau máximo)**.
  - _Base de cálculo:_ Pelo art. 192 da CLT e Súmula Vinculante nº 4 do STF, a base é o **Salário Mínimo Nacional**, a menos que a CCT da categoria estipule expressamente o cálculo sobre o piso da categoria.
- **1.4. Adicional Noturno e Hora Noturna Reduzida:**
  - Horário: Trabalho executado entre as **22h00 e as 05h00**.
  - Percentual: **20%** sobre o valor da hora normal (para trabalhadores urbanos).
  - _O Detalhe Oculto (Hora Ficta):_ A hora noturna não tem 60 minutos, mas **52 minutos e 30 segundos** (art. 73, § 1º da CLT). Isso exige aplicar um fator multiplicador de **1,1428** sobre o cálculo da hora normal.
- **1.5. Descanso Semanal Remunerado (DSR) sobre os Adicionais:**
  - Adicionais noturnos e horas extras habituais geram reflexo no pagamento dos domingos e feriados (DSR). A Súmula nº 172 do TST trata das horas extras habituais no DSR; a integração do adicional noturno pago com habitualidade é da Súmula nº 60 do TST (item I; o item II estende o adicional às horas prorrogadas após a jornada noturna).
- **1.6. Gratificações e Adicionais Convencionais:**
  - Previsões específicas da CCT, como: adicional de função (líder de equipe), triênio, biênio, assiduidade.

---

### Módulo 2: Encargos e Benefícios Anuais, Mensais e Diários

_Correspondência com o modelo da IN 5/2017, alterada pela IN 7/2018: (a conferir no Anexo VII-D da IN 5/2017)._

Este módulo divide-se em três vertentes: as provisões anuais do trabalhador (13º e férias), o que vai para o Governo (tributos sobre a folha) e o que vai direto para o trabalhador no dia a dia (benefícios).

#### Submódulo 2.1: 13º Salário, Férias e Adicional de Férias

- **13º Salário:** provisão mensal de 1/12 da remuneração = **8,33%** (a conferir).
- **Férias e Adicional de Férias (1/3 constitucional):** provisão mensal das férias do titular acrescidas do terço (percentual a conferir).
  - _Atenção:_ esta provisão e o substituto de férias do Submódulo 4.1-A **não devem ser somados quando cobrem o mesmo custo** (ver a Análise, item 4).

#### Submódulo 2.2: GPS, FGTS e Outras Contribuições

São as alíquotas incidentes sobre a folha de pagamento:

- **INSS Patronal:** **20,00%** (contribuição previdenciária da cota patronal). Se a empresa estiver na desoneração (CPRB), veja a transição da Lei nº 14.973/2024 no Módulo 6;
- **FGTS:** **8,00%**;
- **Salário-Educação:** **2,50%**;
- **INCRA:** **0,20%**;
- **Sistema "S" (SESI/SENAI, SESC/SENAC, SEST/SENAT):** desdobrar por entidade conforme o código FPAS da atividade. SESC+SENAC (FPAS 515, limpeza e conservação) ou SESI+SENAI (FPAS 507) somam **2,5%**; o percentual usual de **3,10%** já inclui o SEBRAE (0,6%), conforme a tabela FPAS (IN RFB 2.110/2022, Anexo III; Tabela 04 do eSocial). Conferir o código FPAS da atividade;
- **SEBRAE:** **0,60%** (não somar de novo se já estiver incluído no percentual do Sistema "S");
- **RAT/SAT ajustado pelo FAP:**
  - RAT (Risco Ambiental do Trabalho): alíquota base de **1%, 2% ou 3%** conforme o risco da atividade.
  - FAP (Fator Acidentário de Prevenção): multiplicador que varia de **0,5 a 2,0**.
  - _O RAT Final:_ Pode variar de **0,5% até 6,0%**. A planilha do órgão normalmente adota FAP neutro (1,0).

#### Submódulo 2.3: Benefícios Mensais e Diários (Custo Direto do Trabalhador)

- **Vale-Transporte (VT):**
  - Cálculo: $(Tarifa \times 2 \text{ viagens} \times Dias Trabalhados) - Desconto Legal$.
  - _O Detalhe Oculto:_ O empregador tem o direito por lei (Lei nº 7.418/85) de descontar até **6% do salário-base** do empregado. O que entra na planilha é apenas a diferença que a empresa paga do próprio bolso.
- **Vale-Alimentação / Vale-Refeição (VA/VR):**
  - Valor fixado na CCT por dia trabalhado (ex.: R$ 25,00/dia).
- **Assistência Médica e Odontológica:**
  - Valor mensal per capita, caso seja cláusula obrigatória da CCT da categoria.
- **Seguro de Vida em Grupo:**
  - Apólice obrigatória exigida na quase totalidade das CCTs de vigilância e limpeza (parâmetro prático, sem fonte: geralmente entre R$ 5,00 e R$ 15,00 por funcionário/mês).

---

### Módulo 3: Provisão para Rescisão Contratual

A Administração retém ou provisiona esses valores todo mês para garantir que, quando o contrato terminar (após 1, 2 ou 5 anos), a empresa tenha fundos para demitir a equipe sem dar calote trabalhista.

- **3.1. Aviso Prévio Trabalhado:**
  - Percentual mensal guardado para pagar o salário do último mês em que o trabalhador cumpre o aviso.
  - _Parâmetros:_ o Acórdão 1186/2017-Plenário fixa até **1,94%** no 1º ano de contrato e até **0,194%** a cada ano de prorrogação. Na esfera federal, a Nota Técnica SEI 35883/2026/MGI (Orientação 46 do Portal de Compras, agosto de 2026), a partir do Acórdão 58/2026-Plenário, recomenda **1,94%** no 1º ano e **0,83%** a cada prorrogação em que o empregado permanecer alocado, avaliados os custos não renováveis já amortizados. Em estados e municípios, conferir se o ente segue a nota técnica, o acórdão de 2017 ou regra própria.
- **3.2. Aviso Prévio Indenizado e Aviso Prévio Proporcional:**
  - _Indenizado:_ o trabalhador é dispensado de cumprir o período e a empresa paga o valor correspondente.
  - _Proporcional (Lei nº 12.506/2011):_ para contratos que duram mais de 1 ano, o trabalhador ganha **3 dias a mais por ano de serviço** até o teto de 90 dias. A planilha precisa conter uma fração atuarial para esse acréscimo.
- **3.3. Multa Rescisória do FGTS (40%):**
  - Cálculo da indenização compensatória de 40% sobre todos os depósitos de FGTS feitos durante a vigência contratual.
  - _Ponto crítico histórico:_ A Lei Complementar nº 110/2001 previa mais 10% (totalizando 50%). A Lei nº 13.932/2019 **extinguiu os 10% adicionais**. Se a planilha do órgão ainda cobrar 50%, há erro de cálculo a ser impugnado.
- **3.4. Reflexos Rescisórios no 13º Salário e Férias:**
  - O período do aviso prévio (mesmo indenizado) projeta 1 mês a mais no cálculo do 13º salário e das férias proporcionais com 1/3.

---

### Módulo 4: Custo de Reposição do Profissional Ausente

A Administração Pública não contrata um "indivíduo"; ela contrata um **"posto de serviço ininterrupto"** (ex.: a portaria não pode ficar vazia nenhum dia útil do ano). Quando o titular falta, tira férias ou adoece, a empresa precisa colocar um substituto. Este módulo precifica esse substituto.

_Correspondência com o modelo: (a conferir no Anexo VII-D da IN 5/2017)._

- **4.1. Substituto nas Ausências Legais:**
  - **A. Férias:**
    - Todo trabalhador tem direito a 30 dias de férias após 12 meses.
    - O substituto trabalhará esses 30 dias e receberá salário + encargos + benefícios.
    - Fração atuarial (parâmetro prático, sem fonte normativa): aproximadamente **8,33%** a **11%** (dependendo da escala de trabalho: 44h semanais vs. escala 12x36).
    - _Atenção:_ não somar com a provisão de férias do Submódulo 2.1 quando ambas cobrem o mesmo custo.
  - **B. Ausências Legais (Art. 473 da CLT):**
    - Dias remunerados em que o titular falta por direito da lei: casamento (3 dias), falecimento de parente próximo (2 dias), doação de sangue (1 dia), convocação da Justiça Eleitoral.
    - Parâmetro prático (sem fonte normativa): o percentual varia de **0,28% a 0,56%** da remuneração.
  - **C. Licença-Paternidade:**
    - Nascimento de filho (licença-paternidade de 5 a 20 dias).
  - **D. Ausência por Acidente de Trabalho:**
    - A empresa paga o salário dos primeiros **15 dias** de afastamento antes de o empregado entrar no benefício previdenciário do INSS (Lei nº 8.213/1991, art. 60, § 3º).
  - **E. Afastamento Maternidade:**
    - Cobertura do posto durante a licença-maternidade de 120 dias da titular (CLT, art. 392); o custo na planilha é o do substituto (percentual a conferir).
  - **F. Outras Ausências:**
    - Demais ausências previstas no modelo ou na CCT (conferir no modelo da IN 5/2017 e na CCT da categoria).
- **4.2. Substituto na Intrajornada:**
  - Cobertura do intervalo para repouso e alimentação do titular quando o posto não pode ficar vazio (a conferir).

---

### Módulo 5: Insumos Diversos (Materiais, Uniformes e Equipamentos)

É onde se quantifica tudo o que é físico e perecível.

- **5.1. Uniformes e EPIs (Equipamentos de Proteção Individual):**
  - Não se joga um valor arbitrário. A fórmula usual é a **depreciação mensal por vida útil**:
    $$\text{Custo Mensal} = \frac{\text{Quantidade de Peças} \times \text{Preço Unitário de Mercado}}{\text{Vida Útil em Meses}}$$
  - _Exemplo:_ Se o trabalhador precisa de 2 pares de botas por ano (vida útil de 6 meses cada par) a R$ 120,00 o par: $\frac{1 \times 120}{6} = \text{R\$ 20,00/mês}$.
- **5.2. Materiais de Consumo:**
  - Itens que se gastam na operação: sacos de lixo, panos de chão, desinfetantes, bobinas de crachá, combustível de roçadeira.
  - Devem ser orçados por quantidade consumida estimada por posto ou por metro quadrado ($m^2$).
- **5.3. Máquinas e Equipamentos:**
  - Itens de longa duração: lavadoras de alta pressão, andaimes, computadores.
  - Podem entrar pelo **custo de locação mensal de mercado** ou pelo cálculo de **depreciação contábil do bem** $+$ **taxa mensal de manutenção preventiva**.

---

### Módulo 6: Custos Indiretos, Lucro e Tributos (O BDI do Serviço)

É a conclusão da planilha, onde as despesas corporativas e os impostos são adicionados sobre o custo da operação.

- **6.1. Custos Indiretos (Administração Central):**
  - Rateio das despesas da sede da empresa para manter aquele contrato funcionando (salário do departamento financeiro, advogados, contadores, sistemas de TI, aluguel da sede).
  - Parâmetro prático (sem fonte normativa): varia geralmente entre **1,5% e 5,0%** sobre o custo total da operação.
- **6.2. Lucro da Empresa:**
  - A remuneração líquida do empresário pelo risco da operação (parâmetro prático, sem fonte normativa: geralmente entre **4% e 10%**).
- **6.3. Tributos Incidentes sobre o Faturamento (Impostos Diretos):**
  - **ISS:** Imposto Sobre Serviços (Municipal, entre **2,00% e 5,00%** conforme o local da prestação);
  - **PIS:** Alíquota federal (**0,65%** no lucro presumido/cumulativo ou **1,65%** no lucro real/não cumulativo);
  - **COFINS:** Alíquota federal (**3,00%** no lucro presumido ou **7,60%** no lucro real);
  - _Nota sobre o regime não cumulativo:_ 1,65% e 7,60% são alíquotas nominais. Como o regime não cumulativo gera créditos, na planilha usa-se a **alíquota efetiva** de PIS/Cofins (média recolhida após os créditos), e não a nominal (a conferir).
  - _CPRB (Desoneração da Folha - Lei nº 12.546/2011) — situação em outubro de 2026:_ A desoneração está em transição pela **Lei nº 14.973/2024** (texto conferido no Planalto):
    - **2025:** CPRB a 80% da alíquota + 5% de INSS sobre a folha;
    - **2026:** CPRB a 60% da alíquota + 10% de INSS sobre a folha;
    - **2027:** CPRB a 40% da alíquota + 15% de INSS sobre a folha;
    - **2028:** fim da CPRB; INSS Patronal integral de 20% sobre a folha.
    - Portanto, o INSS Patronal do Submódulo 2.2 **não desaparece**: em 2026 a planilha deve trazer a CPRB reduzida aqui no Módulo 6 (alíquota base de **1,0% a 4,5% sobre a receita bruta**) e a parcela de 10% sobre a folha no Módulo 2.
  - _Transição da Reforma Tributária (LC nº 214/2025) — situação em outubro de 2026:_ 2026 é ano-teste, com **CBS de 0,9%** e **IBS de 0,1%**, compensáveis com PIS/Cofins ou dispensados para quem cumpre as obrigações acessórias (art. 348, §1º). Em 2027 a CBS substitui o PIS e a Cofins (a conferir).
- **O Segredo do Cálculo Matemático ("Preço por Dentro / Gross-Up"):**
  - Os impostos incidem sobre a própria Nota Fiscal emitida. Por isso, a fórmula matemática não é simplesmente somar a porcentagem, mas aplicar a fórmula de divisão:
    $$\text{Preço Final} = \frac{\text{Custo Total} + \text{Custos Indiretos} + \text{Lucro}}{1 - (\text{ISS} + \text{PIS} + \text{COFINS})}$$
- **IRPJ e CSLL no orçamento-base (Súmula nº 254 do TCU):**
  - Pela Súmula 254, o **IRPJ** (Imposto de Renda da Pessoa Jurídica) e a **CSLL** (Contribuição Social sobre o Lucro Líquido) não são despesas indiretas passíveis de inclusão no BDI do orçamento-base, por serem tributos diretos e personalísticos (paráfrase do enunciado oficial, conferido).
  - A súmula trata do **orçamento-base** do órgão: não fala em nulidade nem proíbe o licitante de cobrir esses tributos com o seu lucro. Se o órgão incluir IRPJ e CSLL no BDI da planilha de referência, o pedido cabível é a retificação.

---

### Resumo dos 6 Módulos em um Fluxograma Lógico

```
[MÓDULO 1] Remuneração Direta (Salário CCT + Periculosidade + Insalubridade + Noturno)
    │
    ▼ (Gera a base de cálculo para)
[MÓDULO 2] 13º/Férias + Encargos de Folha (INSS, FGTS, RAT/FAP) + Benefícios (VT, VR, Saúde)
    │
    ▼ (Acrescenta-se o risco de saída)
[MÓDULO 3] Provisão para Demissão (Aviso Prévio + Multa 40% FGTS)
    │
    ▼ (Acrescenta-se a reposição de ausências)
[MÓDULO 4] Cobertura de Faltas e Férias (Substituto do Titular)
    │
    ▼ (Soma-se os insumos de trabalho)
[MÓDULO 5] Uniformes + EPIs + Materiais de Limpeza + Depreciação de Máquinas
    │
    ▼ (TOTAL DO CUSTO DIRETO OPERACIONAL)
    │
[MÓDULO 6] Aplica-se: Administração Central (%) + Lucro (%) + Impostos "por dentro" (ISS + PIS + COFINS)
    │
    ▼
=========================================
 PREÇO FINAL UNITÁRIO DO POSTO / SERVIÇO
=========================================
```
