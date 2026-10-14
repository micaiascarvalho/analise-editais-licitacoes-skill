# Auditoria das afirmações do `briefing/Mapeamento_Analise/` (antes do mapeamento de fontes)

## Contexto
Antes de montar o mapeamento de fontes internas/externas, você pediu uma verificação de consistência e veracidade de cada afirmação nos 14 arquivos (Estrutura + Análise do Edital e dos 6 anexos). Abaixo está o resultado: cada ponto tem ID, o problema, a justificativa (com a fonte usada) e uma sugestão. **Você decide ponto a ponto**; depois disso aplico as correções aceitas e só então faço o mapeamento de fontes (plano anterior, mantido no final).

### Como foi verificado
- **Lei 14.133/2021:** texto vigente baixado do Planalto e conferido artigo por artigo (arts. 11, 17, 18, 23, 25, 40, 41, 47, 55, 57, 59, 60, 63, 67, 69, 92, 94, 96, 103, 121, 135, 137, 138, 141, 143, 150, 156, 162, 164, 165, 183). Marcado **[Lei conferida]**.
- **Súmulas e acórdãos:** busca na web; quase sempre fonte secundária (tribunal estadual, órgão federal, doutrina). Marcado **[fonte secundária]** ou **[não localizado]**. Nada aqui substitui a consulta ao portal do TCU/STF antes de usar em peça.
- **Conhecimento próprio, não conferido nesta sessão:** marcado **[a conferir]**.

### Legenda de gravidade
- **Alta:** citação errada ou inexistente, ou regra contrária à lei. Usada numa impugnação, derruba o argumento.
- **Média:** imprecisa, desatualizada, incompleta ou exagerada; precisa de ajuste.
- **Baixa:** forma, terminologia, números sem fonte.
- **Melhoria:** não é erro; é lacuna que vale preencher.

---

## 0. Pontos transversais (valem para vários arquivos)

| ID | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- |
| X-01 (Média) | Os mesmos erros de citação se repetem em arquivos diferentes (Súmula 263, art. 40 §1º I, garantia com 3 modalidades, data-base do reajuste). | Prova de que o texto foi gerado sem conferência central. | Resolver com o catálogo único de fontes com status `conferido / a conferir` (plano de mapeamento). |
| X-02 (Média) | Normas federais tratadas como universais: IN SEGES 65/2021, 73/2022, 5/2017, Lei 9.784/1999. | Valem para a União; estados e municípios podem ter regulamento próprio ou adotar o federal. | Incluir campo **esfera** (federal/estadual/municipal) em cada fonte e checar o regulamento do ente do edital. |
| X-03 (Baixa) | Números de mercado apresentados como regra (lucro 4–10%, CI 1,5–5%, "60% dos direcionamentos", "inflado 40–60%", "20 a 30 minutos" para intenção de recurso). | Nenhum tem fonte. | Rotular como **parâmetro prático** e separar de exigência legal. |
| X-04 (Baixa) | Resíduos de conversa de chat ("Excelente!", "Perfeito!", "Sua percepção é cirúrgica", quadro de status no topo do ETP). | Não é conteúdo de referência. | Remover aberturas e o quadro de status. |
| X-05 (Melhoria) | Foco da Servfaz (serviços com dedicação exclusiva de mão de obra) está sub-representado. | Faltam: art. 25 §8º II e art. 135 (repactuação), art. 63 §1º (declaração de custos trabalhistas e CCT), art. 121 §3º (conta vinculada, pagamento direto de verbas), Acórdão 58/2026-Plenário (aviso prévio). **[Lei conferida]** | Acrescentar esses pontos nos arquivos da Planilha, TR e Minuta. |
| X-06 (Média) | Conteúdo tributário desatualizado para 2026. | Reoneração da folha (Lei 14.973/2024: em 2026, CPRB a 60% e 10% sobre a folha; regime pleno em 2028) e ano-teste de CBS 0,9% / IBS 0,1% (LC 214/2025, art. 348 §1º). **[fonte secundária]** | Atualizar Módulos 2 e 6 da Planilha e registrar a data de referência. |

---

## 1. Edital

### 1.1 `Estrutura - Edital.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| ED-E1 (Alta) | Seção 6: desempate por "preferência ME/EPP, bens sustentáveis, sorteio". | Não são os critérios da Lei 14.133. | Art. 60: disputa final, desempenho contratual prévio, equidade de gênero, programa de integridade; §1º preferências (empresa do estado, brasileira, P&D, mitigação); §2º ressalva o art. 44 da LC 123. Sorteio era da Lei 8.666. **[Lei conferida]** | Reescrever com a ordem do art. 60 e o empate ficto da LC 123 à parte. |
| ED-E2 (Média) | Seção 3: dotação prévia com base no "art. 18, VIII". | Inciso errado. | Art. 18 VIII trata de modalidade, critério e modo de disputa. A exigência de crédito orçamentário está no art. 150 (sob pena de nulidade) e no caput do art. 18 (compatibilizar com as leis orçamentárias). **[Lei conferida]** | Trocar por art. 150 + caput do art. 18. |
| ED-E3 (Média) | Seção 4: "itens exclusivos até R$ 80 mil ou cotas reservadas de até 25%". | Incompleto. | Cota de 25% é para **bens de natureza divisível** (LC 123 art. 48 III); há exceções do art. 49 da LC 123 e limites do art. 4º da Lei 14.133. **[a conferir]** | Incluir a restrição a bens e as exceções. |
| ED-E4 (Baixa) | Resumo visual com 8 etapas. | Não corresponde às 13 seções descritas. | Inconsistência interna. | Alinhar o diagrama às 13 seções. |

### 1.2 `Analise - Edital.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| ED-A1 (Alta) | Súmula 275 do TCU proíbe exigir tempo mínimo de existência da empresa. | Súmula com conteúdo errado. | A Súmula 275 trata de capital social, patrimônio líquido **ou** garantias, de forma não cumulativa. **[fonte secundária]** Além disso, o art. 67 §5º **permite** exigir até 3 anos de experiência em serviços contínuos. **[Lei conferida]** | Separar "tempo de existência da empresa" de "tempo de experiência"; fundamentar o primeiro em outra fonte (a localizar) e registrar o limite de 3 anos do §5º. |
| ED-A2 (Alta) | Súmula 263 veda limitação de tempo, local e atestado único. | Súmula com conteúdo errado. | A Súmula 263 **admite** quantitativos mínimos proporcionais nas parcelas relevantes. A vedação de tempo e local está no art. 67 §2º **[Lei conferida]**; a vedação de limitar o somatório de atestados vem de acórdão (ex.: 1101/2020-P) **[fonte secundária]**. | Citar o art. 67 §§1º–2º e o acórdão sobre somatório; reposicionar a Súmula 263 como fundamento do que **é** permitido. |
| ED-A3 (Alta) | Acórdão 1.214/2013-Plenário trata de BDI e custos diretos. | Tema errado. | O 1.214/2013 é o marco de terceirização (habilitação e fiscalização, IN 2/2008). **[fonte secundária]** | Trocar por acórdão de BDI verificado ou retirar. O 1.214/2013 serve melhor ao TR e à Planilha de serviços terceirizados. |
| ED-A4 (Alta) | Lei 9.784/1999 garante prazos em dias úteis. | Falso. | A Lei 9.784 (art. 66) conta prazos em dias contínuos. Dias úteis vêm da Lei 14.133 (art. 183 III) quando o prazo é expresso assim. **[Lei 14.133 conferida; Lei 9.784 a conferir]** | Fundamentar dias úteis no art. 183 III e nos artigos que fixam prazos em dias úteis (164, 165). |
| ED-A5 (Média) | Súmula 262: prazo para justificar a exequibilidade. | Baseada na Lei 8.666 (art. 48). | Na Lei 14.133 o tema está no art. 59 §§2º–4º. **[Lei conferida]** A continuidade da presunção relativa precisa de acórdão atual. **[a conferir]** | Citar art. 59 §2º + Súmula 262 como precedente, com acórdão pós-2021. |
| ED-A6 (Média) | Degrau de lance (8%) comparado à margem de lucro (5%). | Comparação frágil. | O intervalo mínimo (art. 57) incide sobre cada lance, não sobre a redução total. Uma margem de 5% não impede lances de 8% em relação a uma proposta inicial alta. **[Lei conferida]** | Reformular: impugnável quando o intervalo é desproporcional ao valor do item ou impede a cobertura da melhor oferta (art. 57 + razoabilidade). Também corrigir "IN SEGES/MGI 73/2022" para **SEGES/ME**. |
| ED-A7 (Melhoria) | Vistoria: "acórdãos sobre vistoria técnica". | Fundamento vago. | A própria lei exige aceitar declaração substitutiva (art. 63 §§2º–3º). **[Lei conferida]** | Citar a lei, que é mais forte que acórdão genérico. |
| ED-A8 (Média) | Índices acima de 1,00 sem justificativa geram impugnação. | Incompleto. | O art. 69 exige índices "devidamente justificados" e o §5º veda índices não usuais **[Lei conferida]**. O TCU (informativo de 2026) admite cumular índices acima de 1 com PL de até 10%. **[fonte secundária]** | O teste é a justificativa no processo, não o número em si. |
| ED-A9 (Média) | LC 123: lote até R$ 80 mil ou objeto divisível sem cota. | Sem as exceções. | Mesmo problema de ED-E3. | Incluir art. 49 da LC 123 e art. 4º da Lei 14.133. |
| ED-A10 (Melhoria) | Recuperação judicial: Súmula 50 do TCE-SP. | Correta, mas só para SP. | Súmula confirmada **[fonte secundária]**. Fundamento nacional: art. 69 II só pede certidão de **falência** **[Lei conferida]**; TCU, Acórdão 1201/2020 **[fonte secundária]**. | Usar a lei + TCU como base; TCE-SP como reforço quando o órgão for paulista. |
| ED-A11 (Baixa) | "Cadastro Nacional da Pessoa Jurídica (CNAE)". | Confunde CNPJ com CNAE. | CNAE é a classificação; a contagem é feita na base do CNPJ por CNAE. Contar empresas por CNAE é prova fraca (CNAE secundário infla o número). | Complementar com histórico de participantes em licitações iguais no PNCP. |
| ED-A12 (Baixa) | Teto abaixo da própria pesquisa é "inexequível". | Termo inadequado. | Inexequível qualifica proposta; no orçamento o vício é subestimação (art. 23 caput). | Ajustar o termo. |
| ED-A13 (Média) | Intenção de recurso em menos de 10 minutos gera impugnação; 20–30 minutos é aceitável. | Parâmetros sem base legal. | A lei diz só "imediatamente" (art. 165 §1º I). **[Lei conferida]** | Apresentar como parâmetro prático e fundamentar em razoabilidade. |
| ED-A14 (Baixa) | SV 21 do STF veda "taxa de expediente". | Extensão por analogia. | A SV 21 trata de depósito ou arrolamento prévio. | Dizer que se trata de aplicação por analogia. |
| ED-A15 (Melhoria) | A análise cobre só 5 das 13 seções. | Lacuna. | Faltam: objeto/parcelamento, orçamento sigiloso (art. 24), prazos mínimos (art. 55), declaração de custos trabalhistas (art. 63 §1º), garantia, sanções. | Cobrir as 13 seções, marcando as derivadas da Estrutura. |

---

## 2. Termo de Referência

### 2.1 `Estrutura - Termo de Refencia.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| TR-E1 (Média) | 8 "seções obrigatórias" do art. 6º XXIII. | Não batem com as alíneas da lei. | O art. 6º XXIII tem alíneas a–j; faltam "estimativa do valor" (i) e "adequação orçamentária" (j), e "Obrigações" não é alínea. Para compras, o art. 40 §1º acrescenta especificação, local de entrega e garantia. **[art. 40 conferido; art. 6º a conferir]** | Reestruturar pelas alíneas a–j e marcar o que vem de modelo da AGU. |
| TR-E2 (Baixa) | Projeto básico serve a "obras de engenharia". | Incompleto. | Também serve a serviços de engenharia. | Ajustar. |
| TR-E3 (Média) | "Prazo legal de pagamento: 10 ou 30 dias úteis". | Não está na lei. | A lei remete ao contrato (art. 92 V); prazos vêm de regulamento (federal: IN SEGES 77/2022 **[a conferir]**). | Apresentar como prazo de regulamento ou contrato. |
| TR-E4 (Baixa) | "12 meses, prorrogável até 5 ou 10 anos". | Mistura de lógica antiga. | Vigência inicial pode chegar a 5 anos (art. 106) e prorrogações a 10 (art. 107). **[a conferir]** | Ajustar a redação. |

### 2.2 `Analise - Termo de Referencia.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| TR-A1 (Alta) | Parcelamento no "art. 40, §1º, I". | Dispositivo errado. | O art. 40 §1º I trata da especificação do produto no TR. Parcelamento está no art. 40 V "b" e §§2º–3º (compras) e no art. 47 II e §1º (serviços). **[Lei conferida]** | Corrigir. O mesmo erro aparece no ETP (ETP-A7). |
| TR-A2 (Alta) | Citar marca "seria proibido pelo art. 41". | Inverte a lei. | O art. 41 I **permite** indicar marca excepcionalmente, com justificativa, em 4 hipóteses. O vício é indicar ou direcionar sem justificativa (art. 9º I "a"). **[Lei conferida]** | Reescrever: impugnável quando não há justificativa enquadrada no art. 41 I. |
| TR-A3 (Média) | Amostra "jamais para todos". | Exceção ignorada. | O art. 41 II admite amostra na pré-qualificação permanente; o parágrafo único restringe ao provisoriamente vencedor só na fase de julgamento; art. 17 §3º. **[Lei conferida]** | Incluir a exceção. |
| TR-A4 (Alta) | O "art. 67 §5º veda atestados emitidos exclusivamente por órgão público". | Dispositivo com outro conteúdo. | O §5º permite exigir experiência de até 3 anos em serviços contínuos. **[Lei conferida]** A vedação de exigir só atestado público vem da jurisprudência. **[a localizar]** | Corrigir a citação e buscar o acórdão. |
| TR-A5 (Alta) | Súmula 263 veda tempo e local. | Mesmo erro de ED-A2. | Ver ED-A2. | Citar o art. 67 §2º. |
| TR-A6 (Média) | Arts. 141 e 143 fixam "prazos estritos" de pagamento. | Conteúdo diferente. | O art. 141 trata da ordem cronológica; o art. 143 manda pagar a **parcela incontroversa** no prazo. **[Lei conferida]** | Usar o art. 143 contra glosas e retenções totais, o que fortalece a tese. |
| TR-A7 (Média) | Cláusula "guarda-chuva" viola o art. 23. | Fundamento fraco. | O art. 23 trata do valor estimado. Melhor base: art. 18 IV (orçamento com composições), art. 6º XXIII "i" e julgamento objetivo (art. 5º). | Trocar o fundamento. |
| TR-A8 (Baixa) | "Cerca de 60% dos direcionamentos". | Estatística sem fonte. | — | Retirar. |
| TR-A9 (Baixa) | Prazo curto é "indicativo clássico" de estoque pronto. | É indício, não prova. | — | Exigir declarações de fabricantes como prova. |
| TR-A10 (Melhoria) | Checklist sem itens de mão de obra. | Lacuna para a Servfaz. | Faltam: CCT indicada, posto vs. produtividade, IMR para serviço contínuo, art. 63 §1º. | Acrescentar. |

---

## 3. Estudo Técnico Preliminar

### 3.1 `Estrutura - ETP.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| ETP-E1 (Alta) | Marca "Levantamento de Mercado" como obrigatório (6 elementos obrigatórios). | Contraria a lei. | O art. 18 §2º exige pelo menos os incisos I, IV, VI, VIII e XIII (necessidade, quantidades, valor, parcelamento, conclusão). Os demais podem faltar **com justificativa**. **[Lei conferida]** | 5 obrigatórios; levantamento de mercado vira "obrigatório ou justificar a ausência". |
| ETP-E2 (Média) | Numeração 1–13 fora da ordem da lei. | Induz a citar o inciso errado. | Lei: IV quantidades, V levantamento, VI valor, VII solução, VIII parcelamento, IX resultados, X providências, XI correlatas. **[Lei conferida]** | Usar os números dos incisos da lei. |
| ETP-E3 (Baixa) | Quadro de status "Próximo da fila" no topo. | Resíduo de chat. | — | Remover. |

### 3.2 `Analise - Estudo tecnico Preliminar.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| ETP-A1 (Alta) | ETP viciado gera "nulidade absoluta" (art. 11, parágrafo único). | Dispositivo errado e exagero. | O parágrafo único do art. 11 trata de governança. O regime de nulidade está nos arts. 147–150, e o art. 147 exige ponderar o interesse público antes de anular. | Corrigir e moderar: o pedido realista é saneamento ou retificação. |
| ETP-A2 (Alta) | Incisos: levantamento = IV, quantidades = VI, valor = VII, providências = XI. | Todos trocados. | Correto: levantamento V, quantidades IV, valor VI, providências X. **[Lei conferida]** | Corrigir. |
| ETP-A3 (Alta) | Checklist: "6 itens obrigatórios (… alternativas … viabilidade)". | Mesmo erro de ETP-E1. | Art. 18 §2º. **[Lei conferida]** | 5 itens + justificativa dos ausentes. |
| ETP-A4 (Alta) | "ETP não público nos autos → processo nulo". | Falso. | O art. 54 §3º permite publicar no PNCP **após a homologação** os documentos da fase preparatória que não integraram o edital. **[Lei conferida; memória do projeto]** O Acórdão 232/2022-P trata do ETP com orçamento sigiloso. | O caminho é pedido de esclarecimento ou acesso (LAI), não nulidade automática. |
| ETP-A5 (Média) | "Matriz de riscos" como elemento do ETP. | Não é elemento do art. 18 §1º. | A análise de riscos é da fase preparatória (art. 18 X); a matriz de riscos é cláusula contratual (art. 103). **[Lei conferida]** | Renomear para "Análise de riscos (art. 18 X)" e ligar à Minuta. |
| ETP-A6 (Média) | Súmula 247 trata não parcelar como "causa de nulidade". | Exagero. | A súmula impõe admitir a adjudicação por item quando o objeto é divisível. | Moderar. |
| ETP-A7 (Alta) | Parcelamento no "art. 40, §1º, I". | Mesmo erro de TR-A1. | — | Art. 40 V "b", §§2º–3º; art. 47. |
| ETP-A8 (Melhoria) | Quantidades. | Falta base para compras. | Art. 40 III (técnicas quantitativas). **[Lei conferida]** | Acrescentar. |
| ETP-A9 (Melhoria) | Valor do ETP vs. pesquisa. | Falta o caso do sigilo. | O valor pode estar em anexo classificado (art. 18 §1º VI; art. 24). **[Lei conferida]** | Prever o cenário de orçamento sigiloso. |

---

## 4. Planilha de Custos

### 4.1 `Estrutura - Planilha de Custos.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| PL-E1 (Alta) | Módulo 2: 2.1 = benefícios, 2.2 = encargos. | Não segue o modelo e contradiz a Análise. | No modelo da IN 5/2017 (alterada pela IN 7/2018): 2.1 = 13º, férias e adicional; 2.2 = GPS, FGTS e outras; 2.3 = benefícios. A Estrutura omite 13º e férias, e a Análise fala em "2.1 vs 4.1" como férias. **[fonte secundária: esclarecimento do MEC 2024]** | Refazer o Módulo 2 com 2.1/2.2/2.3. |
| PL-E2 (Média) | Módulo 4: 4.1 férias, 4.2 ausências, 4.3 paternidade e acidente. | Difere do modelo. | Modelo: 4.1 substituto nas ausências legais (A férias … E maternidade, F outros) e 4.2 intrajornada. Faltam intrajornada e maternidade. **[a conferir no Anexo VII-D]** | Ajustar ao modelo. |
| PL-E3 (Média) | Sistema S de "3,10% a 3,30%" listado ao lado do SEBRAE (0,60%). | Possível dupla contagem. | SESC+SENAC (ou SESI+SENAI) = 2,5%; 3,1% parece já incluir o SEBRAE. **[a conferir na tabela FPAS]** | Desdobrar por entidade e FPAS. |
| PL-E4 (Alta) | CPRB: o INSS de 20% "desaparece". | Desatualizado. | Lei 14.973/2024: em 2026, CPRB a 60% e 10% sobre a folha; folha cheia em 2028. **[fonte secundária]** | Reescrever com a tabela de transição. |
| PL-E5 (Média) | Módulo 6 sem a reforma tributária. | Lacuna em 2026. | CBS 0,9% e IBS 0,1% em teste, compensáveis com PIS/Cofins ou dispensados (LC 214/2025, art. 348 §1º); em 2027 a CBS substitui PIS/Cofins. **[fonte secundária]** | Incluir a seção de transição com data de referência. |
| PL-E6 (Média) | Súmula 254: IRPJ/CSLL "JAMAIS", cláusula "nula de pleno direito". | Exagero. | A súmula trata de não incluir no **BDI do orçamento-base**; não fala em nulidade nem proíbe o licitante de cobrir esses tributos com o lucro. **[fonte secundária]** | Moderar. |
| PL-E7 (Média) | Aviso prévio trabalhado sem regra de prorrogação; "indenizado (Lei 12.506)". | Lacuna e confusão de conceitos. | TCU: 1,94% no 1º ano (Acórdão 1186/2017); o Acórdão 58/2026-P e a Nota Técnica SEI 35883/2026/MGI mudam a regra das prorrogações. **[fonte secundária]** A Lei 12.506 trata do aviso **proporcional**. | Incluir os acórdãos e separar indenizado de proporcional. |
| PL-E8 (Baixa) | Súmula 172 do TST para adicional noturno no DSR. | Súmula sobre horas extras. | A integração do adicional noturno é da Súmula 60. **[a conferir]** | Corrigir. |
| PL-E9 (Baixa) | "IN SEGES/MGI 98/2022 atualizou o modelo". | Órgão e natureza errados. | É SEGES/ME; ela manda aplicar a IN 5/2017 à Lei 14.133, não altera o modelo. | Corrigir. |
| PL-E10 (Baixa) | "Fórmula obrigatória" de depreciação de uniformes; percentuais de 8,33–11%, 0,28–0,56%, CI e lucro. | Sem fonte normativa. | — | Rotular como parâmetro prático (X-03). |
| PL-E11 (Baixa) | PIS/Cofins do lucro real a 1,65% e 7,6%. | Alíquota nominal. | No regime não cumulativo, a jurisprudência usa a alíquota efetiva. **[a conferir]** | Registrar a nuance. |

### 4.2 `Analise - Planilha de Custos.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| PL-A1 (Alta) | Citação entre aspas da Súmula 254: "vedada a inclusão … nas propostas dos licitantes". | Texto inventado. | O enunciado real fala que IRPJ e CSLL não são despesa indireta do BDI do orçamento-base, e não menciona as propostas. **[fonte secundária]** | Substituir pela redação oficial. Citar texto entre aspas só depois de conferir. |
| PL-A2 (Média) | Duplicidade 2.1 × 4.1 com base no Acórdão 1.182/2020-P. | Acórdão não localizado. | A tese procede: o modelo tem duas provisões de férias, que devem ser alternativas (esclarecimento do MEC 2024). Mas o acórdão não foi encontrado. **[não localizado]** | Manter a tese, trocar ou confirmar o acórdão e alinhar com PL-E1. |
| PL-A3 (Média) | Nota Técnica SEI 2.012/2020/ME. | Não localizada. | O fim dos 10% (Lei 13.932/2019, art. 12) está confirmado; o STF (Tema 846) declarou a contribuição constitucional antes da extinção. **[fonte secundária]** | Citar a lei e retirar a nota técnica até confirmá-la. |
| PL-A4 (Média) | VT sem desconto gera "superfaturamento". | Termo errado. | Vício no orçamento é **sobrepreço**; superfaturamento ocorre na execução (a distinção aparece no art. 11 III). **[Lei conferida]** | Trocar o termo (também na Pesquisa). |
| PL-A5 (Baixa) | Art. 59 III como fundamento do piso defasado. | O dispositivo trata da desclassificação de propostas. | O vício do orçamento é art. 23 caput + art. 18 IV; o art. 59 III é a consequência. **[Lei conferida]** | Reordenar o fundamento. |
| PL-A6 (Média) | ISS é sempre do município da prestação. | Generalização. | LC 116, art. 3º: a regra é o estabelecimento prestador, com exceções por item da lista (limpeza e vigilância caem nas exceções). **[a conferir]** | Exigir checagem do item da lista de serviços. |
| PL-A7 (Melhoria) | — | Faltam fundamentos de mão de obra. | Art. 63 §1º (declaração de custos da CCT), art. 25 §8º II e art. 135 (repactuação). **[Lei conferida]** | Acrescentar. |

---

## 5. Pesquisa de Preços

### 5.1 `Estrutura - Pesquisa de Precos.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| PP-E1 (Alta) | A lei estabeleceu "ordem rigorosa de fontes". | Contraria a lei e o próprio texto, que fala em "combinação". | Art. 23 §1º: parâmetros "adotados de forma combinada ou não". Ordem obrigatória só existe para obras (§2º). A prioridade para bens e serviços vem da IN 65/2021 (art. 5º §1º), federal. **[Lei conferida; IN a conferir]** | Corrigir. |
| PP-E2 (Alta) | Os 5 parâmetros (Painel, similares, mídia/tabelas, sites, fornecedores). | Lista diferente da lei. | Lei: I painel/banco de saúde (mediana); II contratações similares (1 ano); III mídia, tabela oficial e sites (um só inciso); IV mínimo de 3 fornecedores, com justificativa da escolha, orçamentos de até 6 meses; V **notas fiscais eletrônicas**. SINAPI e SICRO pertencem ao §2º (obras). **[Lei conferida]** | Reescrever pela lei. |
| PP-E3 (Média) | Cotações de fornecedores: "recomenda-se 90 ou 180 dias". | A lei fixa o limite. | Art. 23 §1º IV: até 6 meses antes da divulgação do edital. **[Lei conferida]** | Corrigir. |
| PP-E4 (Média) | "A lei autoriza média, mediana ou menor"; IN 65 prefere mediana. | Fonte errada e preferência inexistente. | Os métodos estão na IN 65, art. 6º, que não prefere a mediana. A mediana só limita o preço quando há uma única fonte do Painel (§6º). **[fonte secundária]** | Corrigir. |
| PP-E5 (Baixa) | "Preços com mais de 1 ano" valem para tudo. | O limite de 1 ano é das contratações similares. | Art. 23 §1º II. **[Lei conferida]** | Ajustar. |
| PP-E6 (Média) | IN 65 tratada como norma geral. | Só vale na esfera federal. | Ver X-02. | Prever o regulamento do ente. |

### 5.2 `Analise - Pesquisa de Precos.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| PP-A1 (Alta) | Art. 23 §1º põe os bancos públicos como prioritários. | Mesmo erro de PP-E1. | — | Fundamentar na IN 65 (federal) + Acórdão 1.445/2015 (prioridade a Comprasnet e contratações similares, ainda sob a IN 5/2014). **[fonte secundária]** |
| PP-A2 (Média) | Economia de escala com Súmula 177 e Acórdão 2.637/2015. | Fundamentos desalinhados. | A Súmula 177 trata da definição do objeto. Pela fonte secundária, o 2.637/2015 trata de pesquisa restrita a poucos fornecedores, não de varejo × atacado. O argumento mais forte é a própria lei: o art. 23 caput manda observar "a potencial economia de escala". **[Lei conferida]** | Usar o art. 23 caput como fundamento principal. |
| PP-A3 (Baixa) | IN 65, "art. 6º §4º", para descartar valores elevados. | Parágrafo provavelmente errado. | O descarte está no caput do art. 6º; o §4º trata de análise crítica. **[fonte secundária]** | Citar o caput. |
| PP-A4 (Baixa) | Art. 11 III como "combate a fraudes". | Conteúdo diferente. | O art. 11 III trata de evitar sobrepreço, inexequibilidade e superfaturamento. **[Lei conferida]** | Ajustar a descrição. |
| PP-A5 (Baixa) | "Painel de Preços do Governo Federal (PNCP)". | São sistemas diferentes. | — | Separar. |
| PP-A6 (Média) | Consulta ao QSA (sócios, parentesco). | Envolve dados pessoais. | A política da organização proíbe PII nas respostas. | O resultado deve registrar só o vínculo encontrado (sim/não, tipo), sem nomes nem CPFs. |
| PP-A7 (Baixa) | "Inflado em 40% a 60%"; "30% a 50% menor". | Sem fonte. | — | Rotular como exemplo (X-03). |

---

## 6. Minuta Contratual

### 6.1 `Estrutura - Minuta Contratual.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| MC-E1 (Alta) | Data-base do reajuste: orçamento estimado **ou** apresentação da proposta. | A lei só admite o orçamento. | Art. 25 §7º e art. 92 §3º: data-base vinculada à data do orçamento estimado. A "proposta" aparece na repactuação (art. 135 I, custos de mercado). **[Lei conferida]** | Corrigir e separar reajuste de repactuação. |
| MC-E2 (Alta) | Garantia: 3 modalidades. | Desatualizado. | O art. 96 §1º tem inciso IV: título de capitalização. **[Lei conferida]** | Incluir a 4ª modalidade (também na Análise). |
| MC-E3 (Média) | Repactuação como "direito potestativo". | Qualificação sem base. | Art. 25 §8º II: repactuação é o critério **obrigatório** com dedicação exclusiva; art. 135: datas da proposta (mercado) e da CCT (mão de obra). **[Lei conferida]** | Reescrever com esses dispositivos. |
| MC-E4 (Média) | Art. 138 §2º: indenização quando a extinção é por interesse público. | Hipótese diferente. | O §2º fala em culpa **exclusiva da Administração**. **[Lei conferida]** | Corrigir. Verificar à parte o regime da extinção por interesse público. |
| MC-E5 (Média) | Matriz de riscos dá "direito imediato … sem discussões". | Exagero. | O art. 103 §5º considera o equilíbrio mantido quando a matriz é cumprida e lista exceções. **[Lei conferida]** A obrigatoriedade da matriz depende do porte e do regime (art. 22). **[a conferir]** | Moderar e incluir quando a matriz é obrigatória. |
| MC-E6 (Baixa) | Art. 94: atraso na publicação suspende a contagem dos prazos de execução. | Não está na lei. | A lei diz que a divulgação é condição de eficácia (20 dias úteis para licitação). **[Lei conferida]** | Ajustar. |
| MC-E7 (Baixa) | "Art. 92, XI" como cláusula de equilíbrio. | Impreciso. | O inciso XI trata do prazo de resposta ao reequilíbrio; o X, do prazo da repactuação. **[Lei conferida]** | Detalhar. |
| MC-E8 (Baixa) | Prazos de recebimento (15/30 dias) e de pagamento (10/30 dias úteis); "improbidade" por quebra da ordem cronológica. | Não estão na lei. | Os prazos vêm de regulamento; a lei fala em apuração de responsabilidade. **[a conferir]** | Marcar como parâmetro de regulamento. |
| MC-E9 (Baixa) | Resumo com 5 blocos. | Não corresponde às 9 cláusulas. | — | Alinhar. |

### 6.2 `Analise - Minuta Contratual.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| MC-A1 (Alta) | Súmula 451 do STF sobre reajuste. | Súmula sem relação. | A Súmula 451 trata de foro por prerrogativa de função. **[fonte secundária]** | Retirar. |
| MC-A2 (Alta) | Pedido: inserir índice (IPCA) e data-base da proposta. | Errado para mão de obra e na data. | Com dedicação exclusiva o mecanismo é a repactuação (art. 25 §8º II, art. 135), não índice; a data-base do reajuste é a do orçamento (MC-E1). **[Lei conferida]** | Dividir em dois pedidos: reajuste (bens e serviços sem mão de obra) e repactuação (terceirização). |
| MC-A3 (Alta) | Retenção total é ilegal (STJ, REsp 1.733.688/SC). | Precedente não localizado e tese sem nuance. | O REsp não foi encontrado **[não localizado]**. O art. 121 §3º permite condicionar o pagamento à quitação trabalhista e pagar verbas diretamente. **[Lei conferida]** | Reformular: retenção além da parcela controvertida viola o art. 143; retenção ligada a verbas trabalhistas do próprio contrato é lícita. Buscar precedente do STJ verificado. |
| MC-A4 (Média) | Dotação é pré-requisito pelo "art. 18, VIII". | Mesmo erro de ED-E2. | Art. 150. **[Lei conferida]** | Corrigir. |
| MC-A5 (Alta) | Garantia: 3 modalidades. | Mesmo erro de MC-E2. | — | Incluir o título de capitalização. |
| MC-A6 (Média) | Multa moratória deve incidir só sobre a parcela inadimplida; 0,2–0,5% ao dia. | É tese, não regra. | O art. 162 remete a multa de mora ao edital ou contrato; o art. 156 §3º (mínimo 0,5%, máximo 30%) trata da multa sancionatória. **[Lei conferida]** | Apresentar como tese de proporcionalidade, com o limite de 30% como teto objetivo. |
| MC-A7 (Melhoria) | Pagamento: arts. 141 e 143. | Uso incompleto do art. 143. | A parcela incontroversa deve ser paga no prazo. **[Lei conferida]** | Usar o art. 143 como base da tese contra retenção total. |

---

## 7. Retificações, Esclarecimentos e Respostas (RERI)

### 7.1 `Estrutura - RERI.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| RR-E1 (Alta) | A resposta ao esclarecimento "integra formalmente o edital". | Contradiz o Checkpoint 1 da Análise ("resposta não tem força de alteração"). | Inconsistência interna. Leitura harmonizada: a resposta vincula a **interpretação**, mas a mudança de regra exige retificação formal e o art. 55 §1º. **[Lei conferida; jurisprudência a localizar]** | Uniformizar a tese nos dois arquivos. |
| RR-E2 (Baixa) | Resposta "no chat oficial". | Canal errado. | Respostas são divulgadas em sítio eletrônico oficial (art. 164, parágrafo único); o chat é da sessão. **[Lei conferida]** | Corrigir. |
| RR-E3 (Baixa) | Reabertura de "8 dias úteis do zero". | Simplificação. | O art. 55 §1º manda cumprir "os mesmos prazos dos atos originais". O TCU (Acórdão 930/2008) usa o prazo do edital original, não o mínimo legal. **[Lei conferida; acórdão fonte secundária]** | Ajustar. |

### 7.2 `Analise - RERI.md`

| ID | Afirmação | Problema | Justificativa | Sugestão |
| :-- | :-- | :-- | :-- | :-- |
| RR-A1 (Alta) | Acórdão 1.445/2015 sobre reabertura de prazo. | Acórdão de outro tema. | O 1.445/2015 trata de pesquisa de preços. **[fonte secundária]** | Trocar por art. 55 §1º + Acórdãos 2.032/2021 e 2.078/2014-P. **[fonte secundária; conferir]** |
| RR-A2 (Alta) | Acórdão 2.380/2013-P. | Não localizado. | **[não localizado]** | Retirar até confirmar. |
| RR-A3 (Alta) | Checkpoint 5: resposta publicada às 23h45 da véspera descumpre o art. 164, parágrafo único. | Falso. | O prazo vai até o último dia útil anterior à abertura; a véspera está dentro dele. **[Lei conferida]** | A tese passa a ser: (a) se a resposta altera regra, art. 55 §1º; (b) falta de motivação. |
| RR-A4 (Média) | Pedido de "suspensão liminar" na impugnação. | Expectativa irreal. | A impugnação não tem efeito suspensivo automático; o pedido cabe, e as vias externas são a representação ao tribunal de contas (art. 170 §4º) e o mandado de segurança. | Ajustar a ação do loop. |
| RR-A5 (Baixa) | Lei 9.784, art. 50 (motivação). | Válido só na esfera federal. | Ver X-02. | Indicar a lei do ente e o art. 5º da Lei 14.133. |
| RR-A6 (Melhoria) | Loop sem o prazo de impugnação reaberto. | Lacuna. | Se a retificação reabre prazos, o prazo de 3 dias úteis para impugnar (art. 164) também volta a contar. | Incluir no Checkpoint 2. |

---

## Resumo numérico
- **Alta:** 31 · **Média:** 38 · **Baixa:** 28 · **Melhoria:** 10 (107 pontos)
- Citações **não localizadas:** Acórdão 1.182/2020, Acórdão 2.380/2013, REsp 1.733.688/SC, Nota Técnica SEI 2.012/2020.
- Citações **com tema errado:** Súmulas 263 e 275 do TCU, Súmula 451 do STF, Acórdão 1.214/2013 (como BDI), Acórdão 1.445/2015 (como reabertura de prazo).
- **Contradições internas:** PL-E1 × PL-A2 (numeração do Módulo 2) · RR-E1 × Checkpoint 1 do RERI · PP-E1 (ordem × combinação).

## Próximos passos (após sua decisão)
1. Você marca cada ID como **aceito**, **rejeitado** ou **ajustar**.
2. Eu aplico só os aceitos nos 14 arquivos, sem alterar o restante.
3. Confirmo no portal do TCU/STF o que ficou como [fonte secundária] ou [não localizado] e uso nas peças só o que for confirmado.
4. Executo o plano de mapeamento de fontes já aprovado em formato: um `Fontes - {Documento}.md` por pasta + `01 - Catalogo de Fontes.md` com IDs e status `conferido / a conferir`, já partindo da base corrigida.

## Fontes externas consultadas
- Lei 14.133/2021 (Planalto): https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm
- Súmulas 263/275 TCU: https://www.migalhas.com.br/depeso/369406/os-limites-para-a-exigencia-de-capacidade-tecnica-operacional · https://observatorionllc.tc.df.gov.br/wp-content/uploads/2026/05/idSisdoc_33144190v2-69-LC_PUBLICACAO_526_2026_5_19-1.pdf
- Súmula 254 TCU: https://jus.com.br/artigos/23192/consideracoes-sobre-o-calculo-do-bdi-segundo-a-jurisprudencia-do-tribunal-de-contas-da-uniao
- Acórdão 1.214/2013: https://revista.tcu.gov.br/ojs/index.php/RTCU/article/download/1783/1871
- Súmula 451 STF: https://juris.damasio.com.br/sumulas/stf/451
- Acórdão 1.445/2015 e 2.637/2015: https://jus.com.br/artigos/55378/provavel-erro-no-orcamento-estimativo-em-razao-de-acentuadas-discrepancias-entre-o-valor-orcado-e-o-valor-efetivamente-licitado · https://tce.rn.gov.br/as/EscolaContas/ArquivosCurso/127/1._Orçamento_Estimativo_e_Pesquisa_de_Preço.pdf
- Aviso prévio (Acórdãos 1186/2017 e 58/2026): https://www.gov.br/compras/pt-br/agente-publico/orientacoes-e-procedimentos/orientacao-46-nota_tecnica_35883.pdf · https://goias.gov.br/controladoria/wp-content/uploads/sites/31/2026/03/Despacho-no-1857_2024.pdf
- Súmula 50 TCE-SP: https://tce.sp.gov.br/legislacao/resolucao/resolucao-052019/sumula-50
- Reabertura de prazo (Acórdãos 930/2008, 2078/2014, 2032/2021): https://zenite.blog.br/o-novo-prazo-de-publicidade-em-caso-de-modificacao-do-ato-convocatorio-no-pregao/ · https://goias.gov.br/inovacao/wp-content/uploads/sites/26/2016/04/resposta-a-impugnacao-fbe.pdf
- IN 65/2021 art. 6º: https://licitacoesecontratos.tcu.gov.br/4-3-9-3-definicao-e-execucao-da-forma-de-calculo-do-valor-estimado-da-contratacao/
- FGTS 10% (Lei 13.932/2019): https://www.tre-se.jus.br/transparencia-e-prestacao-de-contas/licitacoes-e-contratos/licitacoes/pregoes/pregoes-2021-1/arquivos-pregoes-2021/tre-se-pregao-eletronico-5-2021-pedido-de-esclarecimento-2
- Férias 2.1 × 4.1: https://www.gov.br/mec/pt-br/licitacoes/licitacoes-2024/arquivos-1/1109-esclarecimento-09_.pdf
- Reoneração e reforma tributária 2026: https://www.migalhas.com.br/depeso/447519/reoneracao-da-folha-de-salarios--2026 · https://www.reformatributaria.com/empresas-do-simples-nacional-nao-estao-obrigados-as-aliquotas-teste-de-ibs-cbs-em-2026/
