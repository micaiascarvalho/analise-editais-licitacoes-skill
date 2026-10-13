# Plano de Otimização — Processo de Licitação (Comercial Privado)

**Base:** transcrição de reunião entre Comercial (Ana, Henrique) e TI/IA (Neemias e equipe), complementada pelo quadro de anotações do processo de licitação.

**Meta oficial:** implantar automação inteligente na célula de licitações até **31/12/2026**, automatizando **55%** dos processos operacionais repetitivos e elevando em **40%** a capacidade mensal de participação em licitações.

**Leitura operacional da meta (discutida em reunião):** reduzir de 11 para 6 processos majoritariamente manuais. As etapas priorizadas no item 2 abaixo já devem contribuir de forma decisiva para as duas metas.

---

## 1. Diagnóstico do processo atual

| #   | Etapa                                                | Ferramenta atual                                                                          | Tempo médio                                                        |
| --- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 1   | Prospecção e triagem                                 | Conlicitação + planilha Excel                                                             | 2–3h                                                               |
| 2   | Análise do edital                                    | Leitura manual + NotebookLM (free); precisa definir a IA e os critérios de uso            | ~2 dias (até 2,5 dias em editais grandes, ex. 204 páginas)         |
| 3   | Elaboração de esclarecimento ou impugnação           | Conlicitação, Dr. Licita                                                                  | ~1 dia                                                             |
| 4   | Cotação de insumos                                   | Conecta + planilha Excel (NotebookLM ainda não é usado nesta etapa)                       | ~3 dias                                                            |
| 5   | Elaboração de planilha de custos e formação de preço | Planilha Excel                                                                            | 4h a 3 dias                                                        |
| —   | Cadastro de proposta                                 | Direto na plataforma do pregão                                                            | — (fora de escopo)                                                 |
| —   | Lance                                                | Manual                                                                                    | — (fora de escopo)                                                 |
| 8   | Acompanhamento e análise da concorrência             | Acompanhamento: Conlicitação · Análise da concorrência: manual                            | Análise por empresa concorrente: ~2h (até 4h se muito documentada) |
| —   | Proposta ajustada                                    | Manual                                                                                    | — (fora de escopo)                                                 |
| 10  | Habilitação                                          | Seleção manual de arquivos digitais/digitalizados + elaboração de documentos Word e Excel | —                                                                  |
| 11  | Elaboração de recurso                                | Conlicitação                                                                              | ~1 dia por licitação (pode haver mais de um recurso por certame)   |

**Detalhe da etapa 4 (cotação de insumos), conforme anotações do time:**

- Extração das informações de insumos do edital: ~4h — candidata a automação via **API**.
- Prazo de resposta do Compras (card interno): ~2 dias (48h), fora do controle direto da equipe comercial.

**Referências de contexto:**

- Mediana de colocação da Servfaz em pregões: **14ª posição**.
- Já houve licitação que durou **1 ano** até a conclusão (o processo não tem prazo fixo uma vez iniciado).
- O Comercial já possui questionário e prompt próprios para análise de edital, usados hoje no NotebookLM.

---

## 2. Fluxo priorizado para automação

Sequência identificada como de maior impacto, sem ferramenta dedicada e/ou madura hoje:

**Etapa 2 → Etapa 3 → Etapa 8 → Etapa 11**
(Análise do edital → Esclarecimento/Impugnação → Acompanhamento e análise da concorrência → Elaboração de recurso)

- **Análise do edital (2)** — ~2 dias por edital; maior alavanca isolada de tempo do processo.
- **Esclarecimento/Impugnação (3)** — ~1 dia; depende diretamente da análise do edital.
- **Acompanhamento e análise da concorrência (8)** — hoje ~2h por empresa concorrente; **meta com automação: ~30min por empresa concorrente**. Em uma licitação com 13 concorrentes, isso representa cair de ~26h para ~6,5h de análise.
- **Elaboração de recurso (11)** — ~1 dia por licitação; decorre da análise da concorrência.

Essas quatro etapas formam a cadeia com maior potencial de ganho de tempo do processo inteiro.

---

## 3. Etapas fora de escopo (risco alto, não automatizar agora)

- **Cadastro de proposta e lance** — erro de precisão pode desclassificar a empresa; robôs de lance considerados caros para o retorno esperado.
- **Proposta ajustada** — etapa sensível, exige revisão humana antes do envio ao órgão.

---

## 4. Etapas com ferramenta existente (otimizar depois, não é prioridade agora)

- **Prospecção e triagem** — já usa a assinatura Conlicitação; existe um módulo de automação recente e pouco explorado que poderia reduzir o tempo atual.
- **Cotação de insumos / composição de preço** — NotebookLM já extrai insumos do PDF para Excel (com erros pontuais, ex. dois insumos numa mesma célula); a extração de insumos (~4h) é candidata a automação via API. Em paralelo, Compras/SI avalia uma base única de preços de insumos para evitar recotação de itens repetidos entre editais.
- **Habilitação** — hoje 100% manual (seleção de arquivos + montagem de documentos Word/Excel); sem tempo medido ainda, mas fica como candidata futura.

---

## 5. Plano de ação

1. **Definir e contratar a ferramenta de IA.** Comparar NotebookLM pago, ChatGPT e o hub interno GAIA (que já tem CCTs carregadas) como base do assistente de licitação. Decisão conjunta Comercial + TI.
2. **Consolidar o pipeline PDF → Markdown** antes de qualquer análise por IA — PDF (principalmente escaneado ou com tabelas) degrada muito a extração; conversão já iniciada pela equipe.
3. **Montar o assistente especializado em licitações de serviços terceirizados/mão de obra**, alimentado com:
   - questionário e prompt de análise de edital já existentes no Comercial;
   - impugnações anteriores da empresa (pastas Licitação/DAO);
   - prompts jurídico e contábil já em uso (Milena).
4. **Avaliar automação via API para a extração de insumos** (etapa 4, ~4h), reduzindo o trabalho manual de montagem da planilha enviada ao Compras.
5. **Definir critério de elegibilidade dos editais** para o fluxo automatizado — proposta inicial: editais de até R$ 2 milhões/ano, sem insumos, apenas mão de obra/apoio administrativo (menor risco).
6. **Abrir card de demanda formal**, reunindo: formulário do setor de Demanda, questionário/prompt já existentes, modelo de planilha de análise de concorrência, e o material de treinamento (impugnações anteriores).
7. **Refazer a cronoanálise por processo individual** (não por dia trabalhado), estimando sempre para cima e considerando interrupções reais — a cargo do setor de Processos.
8. **Avaliar com Compras/SI** a viabilidade de uma base única de insumos/preços, reaproveitando possivelmente solução já desenvolvida internamente.
9. **Prever ciclo de maturação do assistente de ~6 meses** de uso e alimentação contínua até atingir nível de especialista, com revisão periódica dos critérios de uso.

---

##
