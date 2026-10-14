# 02 - Plano do Mapeamento de Fontes

## 1. Objetivo

Para cada documento do processo (Edital e anexos), mapear as **fontes internas** (outros documentos do próprio processo) e as **fontes externas** (lei, normas, jurisprudência, bases de dados e prova de mercado) que precisam ser consultadas para decidir se um ponto é impugnável.

O mapeamento parte da base já auditada e corrigida (commits `c29449b`, `eb6431e` e `837df5f`). O trabalho é dividido em fases independentes, para que cada uma caiba em uma sessão e termine com um commit.

## 2. Decisões já tomadas

- **Um arquivo por pasta:** `Fontes - {Documento}.md`, ao lado de `Estrutura` e `Analise`.
- **Catálogo único:** `01 - Catalogo de Fontes.md` na raiz. As fontes externas são citadas nos mapas **só por ID**; o texto da norma e o status ficam no catálogo, que pode ser versionado quando a lei ou a jurisprudência mudar (ver `Minhas observacoes.md`).
- **Status de cada fonte:** `conferido` (texto conferido na fonte oficial) ou `a conferir` (fonte secundária, não localizada ou de memória). Os itens marcados "(a conferir)" nos arquivos de Análise entram como `a conferir`.
- **Campo esfera:** federal, estadual ou municipal. Normas federais (IN SEGES 5/2017, 65/2021, 73/2022, Lei 9.784/1999) devem indicar que o ente do edital pode ter regulamento próprio.
- **Sem dados pessoais** e grafia "Servfaz".

## 3. Formatos

### 3.1 Catálogo (`01 - Catalogo de Fontes.md`)

Fontes internas, ID `INT-*`: `INT-EDITAL`, `INT-TR`, `INT-ETP`, `INT-PLANILHA`, `INT-PESQUISA`, `INT-MINUTA`, `INT-RERI`, `INT-HIST-CONTRATO` (contrato anterior e consumo), `INT-DOTACAO`.

Fontes externas, ID `EXT-{GRUPO}-{CHAVE}` (ex.: `EXT-LEI14133-ART67`, `EXT-TCU-SUM247`, `EXT-BASE-PNCP`), agrupadas em: legislação, normas técnicas e regulatórias, jurisprudência, bases de dados e prova de mercado.

| ID | Nome | Tipo | Esfera | Onde consultar | Usado em | Status |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |

### 3.2 Mapa por documento (`Fontes - {Documento}.md`)

```
# Fontes - {Documento}
Objetivo e como usar (1 parágrafo).

## {N}. {Seção do documento}   ← seções do `Estrutura - {Documento}.md`
Pergunta-chave: "…?"
| Ponto a verificar | Fontes internas (ID + seção) | Fontes externas (IDs) | Prova (o que extrair ou demonstrar) | Gera impugnação se… | Descarta se… |

## Matriz resumo
| Seção | INT-EDITAL | INT-TR | INT-ETP | INT-PLANILHA | INT-PESQUISA | INT-MINUTA | INT-RERI | Externas principais |
```

A lógica segue `Minhas observacoes.md`: cruzamento, prova e fundamento jurídico.

## 4. Fases

Cada fase lê o que está indicado, produz os arquivos, verifica e termina com commit. Uma fase só depende das anteriores pelo catálogo.

| Fase | Entrega | Entradas | Pronto quando |
| :-- | :-- | :-- | :-- |
| **1. Catálogo** | `01 - Catalogo de Fontes.md` | Os 14 arquivos `Estrutura`/`Analise`; relatório da auditoria | Todas as normas, súmulas, acórdãos e bases citados nos 14 arquivos têm ID, esfera, onde consultar e status. Conferir com uma busca por "art.", "Lei", "Súmula", "Acórdão", "IN " nos arquivos. |
| **2. Edital** | `Edital/Fontes - Edital.md` | Estrutura e Análise do Edital; catálogo | As 13 seções da Estrutura aparecem; as seções 1–5 vêm da Análise e a 6 está marcada como derivada; todo ID usado existe no catálogo. |
| **3. TR e ETP** | `Fontes - Termo de Referencia.md`, `Fontes - ETP.md` | Estrutura e Análise de cada um; catálogo | TR com as 10 seções; ETP com os 13 incisos do art. 18 §1º (obrigatórios marcados); IDs existem no catálogo. |
| **4. Planilha e Pesquisa** | `Fontes - Planilha de Custos.md`, `Fontes - Pesquisa de Precos.md` | Estrutura e Análise de cada um; catálogo | Planilha com os 6 módulos; Pesquisa com os 5 parâmetros do art. 23 §1º e os vícios da Análise; IDs existem. |
| **5. Minuta e RERI** | `Fontes - Minuta Contratual.md`, `Fontes - RERI.md` | Estrutura e Análise de cada um; catálogo | Minuta com as 9 cláusulas; RERI com os 5 checkpoints e o modelo de tabela de controle; IDs existem. |
| **6. Consolidação** | Atualização de `00 - Objetivos_Organizacao.md` e do catálogo | Os 7 mapas e o catálogo | Ver seção 5. |

Se uma fase acrescentar fonte nova, ela entra primeiro no catálogo, no mesmo commit.

## 5. Verificação final (fase 6)

1. Todo ID `INT-*`/`EXT-*` usado nos 7 mapas existe no catálogo, e todo ID do catálogo é usado em algum mapa (sem órfãos).
2. Cada seção do `Estrutura` de cada documento aparece no respectivo `Fontes`.
3. A matriz é simétrica: se o documento A cruza com B, o mapa de B cruza com A.
4. Nenhum `Fontes - *` cita artigo, súmula ou acórdão por extenso fora do catálogo.
5. O `00 - Objetivos_Organizacao.md` passa a listar o terceiro arquivo de cada pasta, o catálogo e este plano.

## 6. Andamento

| Fase | Status | Commit |
| :-- | :-- | :-- |
| 1. Catálogo | concluída | este commit (`01 - Catalogo de Fontes.md`) |
| 2. Edital | pendente | — |
| 3. TR e ETP | pendente | — |
| 4. Planilha e Pesquisa | pendente | — |
| 5. Minuta e RERI | pendente | — |
| 6. Consolidação | pendente | — |

Ao concluir uma fase, atualize esta tabela no mesmo commit.
