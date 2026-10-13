Para realizar uma análise técnica ou uma impugnação contábil de alto nível, você precisa conhecer a **anatomia exata de cada linha (rubrica)** da planilha.

No serviço público brasileiro, o padrão mais rigoroso e utilizado pelos órgãos é o modelo federal (instituído pela **IN SEGES/MPDG nº 05/2017** e atualizado pela **IN SEGES/MGI nº 98/2022**). Esse padrão desdobra a planilha em **6 Módulos com submódulos matemáticos detalhados**.

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
  - Súmula nº 172 do TST: Adicionais noturnos e horas extras habituais geram reflexo obrigatório no pagamento dos domingos e feriados (DSR).
- **1.6. Gratificações e Adicionais Convencionais:**
  - Previsões específicas da CCT, como: adicional de função (líder de equipe), triênio, biênio, assiduidade.

---

### Módulo 2: Benefícios Mensais e Diários + Encargos Previdenciários (GPS)

Este módulo divide-se em duas grandes vertentes: o que vai direto para o trabalhador no dia a dia e o que vai para o Governo (tributos sobre a folha).

#### Submódulo 2.1: Benefícios Mensais e Diários (Custo Direto do Trabalhador)

- **Vale-Transporte (VT):**
  - Cálculo: $(Tarifa \times 2 \text{ viagens} \times Dias Trabalhados) - Desconto Legal$.
  - _O Detalhe Oculto:_ O empregador tem o direito por lei (Lei nº 7.418/85) de descontar até **6% do salário-base** do empregado. O que entra na planilha é apenas a diferença que a empresa paga do próprio bolso.
- **Vale-Alimentação / Vale-Refeição (VA/VR):**
  - Valor fixado na CCT por dia trabalhado (ex.: R$ 25,00/dia).
- **Assistência Médica e Odontológica:**
  - Valor mensal per capita, caso seja cláusula obrigatória da CCT da categoria.
- **Seguro de Vida em Grupo:**
  - Apólice obrigatória exigida na quase totalidade das CCTs de vigilância e limpeza (geralmente entre R$ 5,00 e R$ 15,00 por funcionário/mês).

#### Submódulo 2.2: Encargos Previdenciários (GPS), FGTS e Contribuições Sociais

São as alíquotas incidentes sobre a folha de pagamento:

- **INSS Patronal:** **20,00%** (contribuição previdenciária da cota patronal);
- **FGTS:** **8,00%**;
- **Salário-Educação:** **2,50%**;
- **INCRA:** **0,20%**;
- **Sistema "S" (SESI/SENAI, SESC/SENAC, SEST/SENAT):** Varia entre **3,10% e 3,30%** conforme o código FPAS da atividade;
- **SEBRAE:** **0,60%**;
- **RAT/SAT ajustado pelo FAP:**
  - RAT (Risco Ambiental do Trabalho): alíquota base de **1%, 2% ou 3%** conforme o risco da atividade.
  - FAP (Fator Acidentário de Prevenção): multiplicador que varia de **0,5 a 2,0**.
  - _O RAT Final:_ Pode variar de **0,5% até 6,0%**. A planilha do órgão normalmente adota FAP neutro (1,0).

---

### Módulo 3: Provisão para Rescisão Contratual

A Administração retém ou provisiona esses valores todo mês para garantir que, quando o contrato terminar (após 1, 2 ou 5 anos), a empresa tenha fundos para demitir a equipe sem dar calote trabalhista.

- **3.1. Aviso Prévio Trabalhado:**
  - Percentual mensal guardado para pagar o salário do último mês em que o trabalhador cumpre o aviso.
- **3.2. Aviso Prévio Indenizado (Lei nº 12.506/2011):**
  - Para contratos que duram mais de 1 ano, o trabalhador ganha **3 dias a mais por ano de serviço** até o teto de 90 dias. A planilha precisa conter uma fração atuarial para essa indenização.
- **3.3. Multa Rescisória do FGTS (40%):**
  - Cálculo da indenização compensatória de 40% sobre todos os depósitos de FGTS feitos durante a vigência contratual.
  - _Ponto crítico histórico:_ A Lei Complementar nº 110/2001 previa mais 10% (totalizando 50%). A Lei nº 13.932/2019 **extinguiu os 10% adicionais**. Se a planilha do órgão ainda cobrar 50%, há erro de cálculo a ser impugnado.
- **3.4. Reflexos Rescisórios no 13º Salário e Férias:**
  - O período do aviso prévio (mesmo indenizado) projeta 1 mês a mais no cálculo do 13º salário e das férias proporcionais com 1/3.

---

### Módulo 4: Custo de Reposição do Profissional Ausente

A Administração Pública não contrata um "indivíduo"; ela contrata um **"posto de serviço ininterrupto"** (ex.: a portaria não pode ficar vazia nenhum dia útil do ano). Quando o titular falta, tira férias ou adoece, a empresa precisa colocar um substituto. Este módulo precifica esse substituto.

- **4.1. Cobertura de Férias do Titular:**
  - Todo trabalhador tem direito a 30 dias de férias após 12 meses.
  - O substituto trabalhará esses 30 dias e receberá salário + encargos + benefícios.
  - Fração atuarial padrão: aproximadamente **8,33%** a **11%** (dependendo da escala de trabalho: 44h semanais vs. escala 12x36).
- **4.2. Ausências Legais (Art. 473 da CLT):**
  - Dias remunerados em que o titular falta por direito da lei: casamento (3 dias), falecimento de parente próximo (2 dias), doação de sangue (1 dia), nascimento de filho (licença paternidade de 5 a 20 dias), convocação da Justiça Eleitoral.
  - O percentual varia de **0,28% a 0,56%** da remuneração.
- **4.3. Licença Paternidade e Acidentes de Trabalho:**
  - A empresa cobre os primeiros **15 dias de atestado médico** antes de o funcionário entrar no benefício previdenciário do INSS.

---

### Módulo 5: Insumos Diversos (Materiais, Uniformes e Equipamentos)

É onde se quantifica tudo o que é físico e perecível.

- **5.1. Uniformes e EPIs (Equipamentos de Proteção Individual):**
  - Não se joga um valor arbitrário. A fórmula obrigatória é a **depreciação mensal por vida útil**:
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
  - Varia geralmente entre **1,5% e 5,0%** sobre o custo total da operação.
- **6.2. Lucro da Empresa:**
  - A remuneração líquida do empresário pelo risco da operação (geralmente entre **4% e 10%**).
- **6.3. Tributos Incidentes sobre o Faturamento (Impostos Diretos):**
  - **ISS:** Imposto Sobre Serviços (Municipal, entre **2,00% e 5,00%** conforme o local da prestação);
  - **PIS:** Alíquota federal (**0,65%** no lucro presumido/cumulativo ou **1,65%** no lucro real/não cumulativo);
  - **COFINS:** Alíquota federal (**3,00%** no lucro presumido ou **7,60%** no lucro real);
  - _CPRB (Desoneração da Folha - Lei nº 12.546/2011):_ Se a atividade estiver no regime de desoneração, o INSS Patronal de 20% do Módulo 2 **desaparece** e entra aqui no Módulo 6 uma alíquota de **1,0% a 4,5% sobre a receita bruta**.
- **O Segredo do Cálculo Matemático ("Preço por Dentro / Gross-Up"):**
  - Os impostos incidem sobre a própria Nota Fiscal emitida. Por isso, a fórmula matemática não é simplesmente somar a porcentagem, mas aplicar a fórmula de divisão:
    $$\text{Preço Final} = \frac{\text{Custo Total} + \text{Custos Indiretos} + \text{Lucro}}{1 - (\text{ISS} + \text{PIS} + \text{COFINS})}$$
- **A Grande Vedação Legal (Súmula nº 254 do TCU):**
  - **IRPJ** (Imposto de Renda da Pessoa Jurídica) e **CSLL** (Contribuição Social sobre o Lucro Líquido) **são impostos diretos sobre o lucro da empresa e JAMAIS podem constar na planilha pública como repasse ao Estado**. Se o órgão incluir IRPJ e CSLL na planilha, a cláusula é nula de pleno direito.

---

### Resumo dos 6 Módulos em um Fluxograma Lógico

```
[MÓDULO 1] Remuneração Direta (Salário CCT + Periculosidade + Insalubridade + Noturno)
    │
    ▼ (Gera a base de cálculo para)
[MÓDULO 2] Benefícios (VT, VR, Saúde) + Encargos de Folha (INSS, FGTS, RAT/FAP)
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
