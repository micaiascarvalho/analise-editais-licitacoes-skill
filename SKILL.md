---
name: analise-editais-licitacoes
description: >
  Use para analisar editais de licitação pública (Lei 14.133/2021 e Lei 13.303/2016),
  especialmente serviços continuados com dedicação de mão de obra. Executa um fluxo único:
  o levantamento objetivo para composição de preços seguido do parecer crítico estratégico
  (habilitação, planilha de custos, riscos contratuais, pontos de impugnação) e do parecer
  final. Ativa em "analisar edital",
  "análise de edital", "vale a pena participar", "resumo do edital", "levantamento do edital",
  "composição de preços", "requisitos de habilitação", "parecer de edital", "riscos do edital",
  "pontos para impugnação", "termo de referência".
tags:
  [
    licitacao,
    edital,
    analise,
    pregao,
    lei-14133,
    habilitacao,
    composicao-de-precos,
    parecer,
    servfaz
  ]
---

# 📑 Análise de Editais de Licitação

> ⚠️ Orientação técnica de apoio à decisão. A análise **não substitui** a leitura integral
> do edital e seus anexos, nem o parecer de um advogado especialista em direito administrativo.
> Em caso de divergência, o texto oficial do edital e seus anexos sempre prevalecem.
> **Nunca presuma** informação ausente: se um dado não constar dos documentos fornecidos,
> registre como "Não localizado / verificar no edital".

> 📌 **Regra de rastreabilidade (obrigatória em todas as respostas):** **toda** resposta,
> achado ou conclusão deve vir acompanhada da **referência da fonte**, permitindo consultar
> a origem no documento. Use o padrão:
> **`(Documento, item/cláusula, pág. X)`** — ex.: `(Edital, item 6.8, pág. 9)`,
> `(TR, item 9.25, pág. 40)`, `(Minuta, cláusula 12.1, pág. 173)`.
> Quando a informação não for localizada, registre **"Não localizado / verificar no edital"**
> em vez de responder sem fonte. Nunca apresente um dado sem indicar de onde ele veio.

---

## 🎯 Objetivo

Transformar um edital de licitação e seus anexos (Termo de Referência, Minuta de Contrato,
Planilhas) em uma análise estruturada que permita ao setor de processos:

1. **Levantar** os dados objetivos necessários à composição de preços
2. **Avaliar criticamente** habilitação, custos, riscos e legalidade das cláusulas
3. **Decidir** sobre participação e identificar o que impugnar/esclarecer

> **Escopo:** a Servfaz atua com **serviços continuados com dedicação de mão de obra**
> (terceirização). Assuma que todo edital analisado é dessa natureza — portanto os itens de
> mão de obra do Modo 1 (jornada, CCT, insalubridade, férias, uniformes, EPI, conta vinculada)
> **sempre se aplicam** e devem ser respondidos. Se algum não constar, marque "Sem previsão".

---

## 🧩 Fluxo de análise (único)

Esta skill executa **um único fluxo**, sempre na mesma ordem: primeiro o **MODO 1**, em seguida
o **MODO 2** e, por fim, o **Parecer final**. Os dois modos são **etapas sequenciais** de uma
mesma análise — **não** são opções alternativas nem exigem escolha do usuário.

| Ordem | Etapa                                               | Base     | Perfil                                                     |
| ----- | --------------------------------------------------- | -------- | ---------------------------------------------------------- |
| 1º    | **MODO 1 — Levantamento para Composição de Preços** | Prompt 1 | Analista de licitação sênior                               |
| 2º    | **MODO 2 — Parecer Estratégico Completo**           | Prompt 2 | Especialista sênior (Lei 14.133/2021 + jurisprudência TCU) |
| 3º    | **Parecer final**                                   | —        | Consolidação da decisão                                    |

> **Sempre** execute as três etapas na ordem acima (MODO 1 → MODO 2 → Parecer final), ainda que
> o usuário não peça explicitamente. Retorne primeiro o resultado completo do MODO 1 e só então
> o MODO 2.

---

## 📥 Entradas necessárias (input)

| Item                                                | Obrigatório    | Observação                                        |
| --------------------------------------------------- | -------------- | ------------------------------------------------- |
| Edital completo                                     | ✅             | PDF ou texto integral                             |
| Termo de Referência / Projeto Básico                | ✅             | Especificações do objeto                          |
| Minuta de Contrato                                  | ⭕ recomendado | Define obrigações, penalidades e matriz de riscos |
| Planilhas de custos / modelos                       | ⭕ recomendado | Necessário para análise de exequibilidade         |
| Convenção Coletiva (CCT) aplicável                  | ⭕ recomendado | Essencial em serviços com mão de obra             |
| Perfil da empresa (CNAE, porte, atestados, índices) | ⭕ recomendado | Necessário para o checklist de habilitação        |

---

## 🧭 Metodologia

> 📚 **Consulta de CCT — ferramenta `Conhecimento Servfaz`:** sempre que uma **Convenção
> Coletiva de Trabalho (CCT)** for citada ou identificada no edital/TR (nome do sindicato,
> número de registro, ex.: `PI000099/2026`), **se a ferramenta `Conhecimento Servfaz` estiver
> disponível**, use-a para buscar e validar os dados da CCT (pisos salariais, adicionais de
> insalubridade/periculosidade, benefícios como vale-transporte/alimentação, vigência e
> data-base) **antes** de formular a resposta, baseando a resposta nesses dados e **citando a
> fonte** (a CCT e a origem em `Conhecimento Servfaz`).
>
> - Se a ferramenta **não estiver disponível** (caso atual), responda com base no que consta no
>   edital/anexos e **sinalize** que os dados da CCT precisam de validação na fonte oficial.
> - Se estiver disponível mas não retornar a CCT, registre "CCT não localizada em
>   Conhecimento Servfaz / verificar" e **não presuma** valores.

### MODO 1 — Levantamento para Composição de Preços

> Atue como um **analista de licitação sênior**. Extraia do edital e do termo de referência
> as informações abaixo, na ordem, para composição de preços. Responda item a item, **sempre
> com a referência da fonte** no padrão `(Documento, item/cláusula, pág. X)` — sem exceção.
> Quando não houver previsão, escreva **"Sem previsão"** e indique onde verificou.

**Objeto e disputa**

1. Qual o objeto?
2. É adjudicação por **item** ou por **lote/grupo**?
3. Qual o **modo de disputa**?
4. Qual o **intervalo de lances**?
5. Qual a **data limite** para impugnar/esclarecer?
6. Qual o **e-mail** para impugnar/esclarecer?

**Mão de obra e condições de trabalho** 7. Há previsão de **insalubridade ou periculosidade**? 8. Qual a **jornada de trabalho**? 9. Qual a **Convenção Coletiva (CCT)** aplicável? → consultar `Conhecimento Servfaz` quando disponível (ver regra acima) 10. Haverá **substituto** na cobertura de férias? 11. Há previsão de **uniformes**? Quais peças o compõem? 12. Há previsão de **materiais e equipamentos**? 13. Há previsão de **EPI**? 14. Há cláusula de **repactuação**?

**Habilitação e garantias**

15. Quais **documentos de habilitação** devem ser apresentados? Responda **organizado nas
    categorias abaixo**, confirmando cada exigência no edital/TR e citando a fonte. Os valores
    concretos (anos de experiência, % e nº de postos, cargos e escolaridade) **variam por edital**
    — extraia-os do edital analisado; abaixo está a estrutura e os parâmetros de referência:

    - **Habilitação Jurídica:** documento de identidade (RG), registro na Junta Comercial,
      Ato Constitutivo/Estatuto/Contrato Social ou CCMEI, conforme a natureza jurídica.
    - **Habilitação Fiscal, Social e Trabalhista:** prova de CNPJ, Certidão Conjunta de Quitação
      de Tributos Federais e Dívida Ativa da União (RFB/PGFN), CRF/FGTS, CNDT (Certidão Negativa
      de Débitos Trabalhistas) e prova de inscrição e regularidade fiscal Municipal/Distrital.
      _Podem ser substituídos pela consulta cadastral no SICAF._
    - **Qualificação Econômico-Financeira:** certidão negativa de falência/insolvência civil;
      Balanço Patrimonial e Demonstrações Contábeis comprovando índices de:
      - Liquidez Geral (LG) > 1,0;
      - Liquidez Corrente (LC) > 1,0;
      - Solvência Geral (SG) > 1,0.

      _Caso algum índice seja inferior a 1,0, exige-se capital mínimo de 10% do valor estimado
      anual do contrato._ Também é exigida **Declaração de Compromissos Assumidos**, acompanhada
      da **DRE** (Demonstração do Resultado do Exercício).
    - **Qualificação Técnico-Operacional:** atestado(s) de capacidade técnica que comprove(m):
      - experiência mínima (ex.: **2 anos** — conferir no edital); e
      - prestação de serviços em quantidade equivalente a, no mínimo, **50% dos postos** a serem
        contratados (ex.: mínimo de 31 postos — recalcular conforme o nº de postos do edital).
    - **Qualificação Técnico-Profissional:** comprovação dos requisitos formais de instrução e
      experiência profissional prévia dos cargos exigidos (ex.: Assistente — Ensino Médio;
      Técnico — Ensino Médio; Técnico em Secretariado — registro profissional ativo em conselho;
      Secretário Executivo — registro profissional ativo em conselho). Extrair os cargos e
      requisitos do edital analisado.

16. A certidão de **PCD e jovem aprendiz** deve ser apresentada ou apenas marcada em campo próprio do sistema?
17. Deverá apresentar **garantia de proposta**?
18. Qual o **percentual de seguro garantia**?
19. Deverá ser cotado **encargos de conta vinculada**?

---

### MODO 2 — Parecer Estratégico Completo

> Atue como **especialista sênior em licitações públicas, direito administrativo e gestão de
> contratos** (foco na Lei 14.133/2021 e jurisprudência do TCU). Faça uma análise crítica,
> detalhada e estratégica do edital e seus anexos, estruturada **obrigatoriamente** nos 7 tópicos.
> Cada achado deve trazer a **referência da fonte** no padrão `(Documento, item/cláusula, pág. X)`;
> quando citar dispositivo legal, indique o artigo (e não invente jurisprudência).

**1. Visão geral do objeto e regras do jogo**

- Órgão licitante, modalidade, critério de julgamento (menor preço / maior desconto) e modo de disputa
- Prazo de execução, prorrogações e valor estimado (se houver)

**2. Requisitos de habilitação (checklist de riscos)**

- Regularidade jurídica, fiscal, social e trabalhista
- Qualificação econômico-financeira (índices contábeis, capital social mínimo, patrimônio líquido)
- Qualificação técnica (atestados exigidos, limitações de quantitativos, parcelas de maior relevância, vedações indevidas)

**3. Proposta de preços e planilha de custos**

- Adequação da planilha (salários, encargos sociais e trabalhistas, insumos, BDI, tributos)
- Desequilíbrios, subestimação de custos ou exigências inexequíveis pelo órgão

**4. Benefícios e vantagens competitivas**

- Margens de preferência, tratamento favorecido ME/EPP (LC 123/2006), subcontratação que beneficie a estratégia

**5. Análise de riscos contratuais e operacionais**

- Riscos evidentes ou ocultos no TR e na Minuta (matriz de riscos desequilibrada, multas desproporcionais, obrigações excessivas, reajuste e repactuação)

**6. Pontos críticos para impugnação e esclarecimentos**

- Cláusulas restritivas à competitividade, exigências ilegais, ambiguidades
- Apontar o que deve ser **Pedido de Esclarecimento** e o que deve ser **Impugnação**

**7. Principais obrigações da contratada**

- Responsabilidades mais onerosas, transição contratual, SLAs, relatórios e prepostos

---

## 📤 Formato de saída (output)

### Cabeçalho (sempre)

| Campo                               | Conteúdo    | Fonte               |
| ----------------------------------- | ----------- | ------------------- |
| Órgão/Entidade                      | _a extrair_ | _(Doc, item, pág.)_ |
| Nº do edital / processo             | _a extrair_ |                     |
| Modalidade / critério de julgamento | _a extrair_ |                     |
| Objeto                              | _a extrair_ |                     |
| Adjudicação (item ou lote/grupo)    | _a extrair_ |                     |
| Valor estimado                      | _a extrair_ |                     |
| Data/hora da sessão                 | _a extrair_ |                     |
| Plataforma                          | _a extrair_ |                     |

A saída segue **sempre** a ordem única do fluxo: **Cabeçalho → MODO 1 → MODO 2 → Parecer final**.

- **MODO 1** → responder os 19 itens na ordem, em tabela **Pergunta | Resposta | Fonte** (a
  fonte é obrigatória em cada linha; o item 15 sai nas categorias de habilitação definidas acima).
- **MODO 2** → desenvolver os 7 tópicos, cada achado com **referência da fonte** + implicação estratégica.
- **Parecer final** → consolidação da decisão (ver abaixo).

### Parecer final

- ✅ Participar / ⚠️ Participar com ressalvas / ❌ Não participar — com justificativa objetiva,
  cada argumento remetendo à **fonte** que o sustenta
- Lista de **pendências de esclarecimento** e **pontos a impugnar** (do Tópico 6), com a
  referência da cláusula de origem `(Documento, item/cláusula, pág. X)`
- Lista de **dados não localizados** que exigem verificação no edital

---

## ✅ Checklist de extração mínima

- [ ] Objeto e forma de adjudicação (item ou lote/grupo)
- [ ] Modalidade, critério de julgamento e modo de disputa
- [ ] Valor estimado / de referência
- [ ] Data/hora da sessão, prazo e e-mail para impugnar/esclarecer
- [ ] Requisitos de habilitação (jurídica, fiscal, social, trabalhista, técnica, econômico-financeira)
- [ ] Condições de mão de obra (jornada, CCT, insalubridade/periculosidade, férias)
- [ ] Uniformes, materiais, equipamentos e EPI
- [ ] Repactuação / reajuste
- [ ] Garantia de proposta e seguro garantia (percentual)
- [ ] Conta vinculada
- [ ] Penalidades, multas e matriz de riscos
- [ ] Benefícios ME/EPP aplicáveis

---

## 🚩 Sinais de alerta (red flags)

- Cláusulas **restritivas à competitividade** (atestados com quantitativos excessivos, exigências direcionadas)
- **Matriz de riscos desequilibrada** ou multas desproporcionais na Minuta
- **Subestimação de custos** pelo órgão (planilha de referência inexequível)
- Exigências **ilegais** ou em conflito com a Lei 14.133/2021 e a jurisprudência do TCU
- Ambiguidades que possam gerar **desclassificação indevida**
- Prazos de execução/transição incompatíveis com a operação

---

## 🔗 Referências

| Recurso                                  | Link                                                                                       |
| ---------------------------------------- | ------------------------------------------------------------------------------------------ |
| Lei 14.133/2021                          | [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm) |
| Lei 13.303/2016 (Estatais)               | [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/lei/l13303.htm) |
| PNCP — busca de editais                  | [pncp.gov.br/app/editais](https://pncp.gov.br/app/editais)                                 |
| Prompts originais do setor               | `prompt1_levantamento_composicao_precos.md`, `prompt2_parecer_estrategico.md`              |
| Skill de contexto geral sobre licitações | `licitacoes-brasil`                                                                        |
