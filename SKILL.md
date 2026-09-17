---
name: analise-editais-licitacoes
description: >
  Use para analisar editais de licitação pública (Lei 14.133/2021 e Lei 13.303/2016),
  especialmente serviços continuados com dedicação de mão de obra. Faz o levantamento
  objetivo para composição de preços e/ou o parecer crítico estratégico (habilitação,
  planilha de custos, riscos contratuais, pontos de impugnação). Ativa em "analisar edital",
  "análise de edital", "vale a pena participar", "resumo do edital", "levantamento do edital",
  "composição de preços", "requisitos de habilitação", "parecer de edital", "riscos do edital",
  "pontos para impugnação", "termo de referência".
tags: [licitacao, edital, analise, pregao, lei-14133, habilitacao, composicao-de-precos, parecer, servfaz]
---

# 📑 Análise de Editais de Licitação

> ⚠️ Orientação técnica de apoio à decisão. A análise **não substitui** a leitura integral
> do edital e seus anexos, nem o parecer de um advogado especialista em direito administrativo.
> Em caso de divergência, o texto oficial do edital e seus anexos sempre prevalecem.
> **Nunca presuma** informação ausente: se um dado não constar dos documentos fornecidos,
> registre como "Não localizado / verificar no edital".

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

## 🧩 Os dois modos de análise

Esta skill opera em dois modos, herdados das ferramentas atuais do setor. Podem ser usados
isolada ou conjuntamente.

| Modo | Base | Quando usar | Perfil |
|------|------|-------------|--------|
| **Modo 1 — Levantamento para Composição de Preços** | Prompt 1 | Triagem rápida e coleta de dados para precificar, sobretudo serviços com mão de obra | Analista de licitação sênior |
| **Modo 2 — Parecer Estratégico Completo** | Prompt 2 | Análise crítica jurídica e estratégica antes da decisão de participar/impugnar | Especialista sênior (Lei 14.133/2021 + jurisprudência TCU) |

> **Padrão:** se o usuário não especificar o modo, pergunte qual deseja — ou, havendo tempo/insumos,
> execute o **Modo 1 seguido do Modo 2** (levantamento → parecer), que é o fluxo completo.

---

## 📥 Entradas necessárias (input)

| Item | Obrigatório | Observação |
|------|-------------|------------|
| Edital completo | ✅ | PDF ou texto integral |
| Termo de Referência / Projeto Básico | ✅ | Especificações do objeto |
| Minuta de Contrato | ⭕ recomendado | Define obrigações, penalidades e matriz de riscos |
| Planilhas de custos / modelos | ⭕ recomendado | Necessário para análise de exequibilidade |
| Convenção Coletiva (CCT) aplicável | ⭕ recomendado | Essencial em serviços com mão de obra |
| Perfil da empresa (CNAE, porte, atestados, índices) | ⭕ recomendado | Necessário para o checklist de habilitação |

---

## 🧭 Metodologia

### MODO 1 — Levantamento para Composição de Preços
> Atue como um **analista de licitação sênior**. Extraia do edital e do termo de referência
> as informações abaixo, na ordem, para composição de preços. Responda item a item; quando não
> houver previsão, escreva **"Sem previsão"** e cite a fonte (item/página) quando possível.

**Objeto e disputa**
1. Qual o objeto?
2. É adjudicação por **item** ou por **lote/grupo**?
3. Qual o **modo de disputa**?
4. Qual o **intervalo de lances**?
5. Qual a **data limite** para impugnar/esclarecer?
6. Qual o **e-mail** para impugnar/esclarecer?

**Mão de obra e condições de trabalho**
7. Há previsão de **insalubridade ou periculosidade**?
8. Qual a **jornada de trabalho**?
9. Qual a **Convenção Coletiva (CCT)** aplicável?
10. Haverá **substituto** na cobertura de férias?
11. Há previsão de **uniformes**? Quais peças o compõem?
12. Há previsão de **materiais e equipamentos**?
13. Há previsão de **EPI**?
14. Há cláusula de **repactuação**?

**Habilitação e garantias**
15. Quais **documentos de habilitação** devem ser apresentados?
16. A certidão de **PCD e jovem aprendiz** deve ser apresentada ou apenas marcada em campo próprio do sistema?
17. Deverá apresentar **garantia de proposta**?
18. Qual o **percentual de seguro garantia**?
19. Deverá ser cotado **encargos de conta vinculada**?

---

### MODO 2 — Parecer Estratégico Completo
> Atue como **especialista sênior em licitações públicas, direito administrativo e gestão de
> contratos** (foco na Lei 14.133/2021 e jurisprudência do TCU). Faça uma análise crítica,
> detalhada e estratégica do edital e seus anexos, estruturada **obrigatoriamente** nos 7 tópicos:

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

| Campo | Conteúdo |
|-------|----------|
| Órgão/Entidade | _a extrair_ |
| Nº do edital / processo | _a extrair_ |
| Modalidade / critério de julgamento | _a extrair_ |
| Objeto | _a extrair_ |
| Adjudicação (item ou lote/grupo) | _a extrair_ |
| Valor estimado | _a extrair_ |
| Data/hora da sessão | _a extrair_ |
| Plataforma | _a extrair_ |

- **Modo 1** → responder os 19 itens na ordem, formato pergunta/resposta, com fonte quando possível.
- **Modo 2** → desenvolver os 7 tópicos, cada um com achados + implicação estratégica.
- **Fluxo completo** → Cabeçalho → Modo 1 → Modo 2 → **Parecer final**.

### Parecer final (quando solicitado)
- ✅ Participar / ⚠️ Participar com ressalvas / ❌ Não participar — com justificativa objetiva
- Lista de **pendências de esclarecimento** e **pontos a impugnar** (do Tópico 6)
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

| Recurso | Link |
|---------|------|
| Lei 14.133/2021 | [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm) |
| Lei 13.303/2016 (Estatais) | [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/lei/l13303.htm) |
| PNCP — busca de editais | [pncp.gov.br/app/editais](https://pncp.gov.br/app/editais) |
| Prompts originais do setor | `prompt1_levantamento_composicao_precos.md`, `prompt2_parecer_estrategico.md` |
| Skill de contexto geral sobre licitações | `licitacoes-brasil` |
