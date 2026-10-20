# Auditoria da minuta

Este checklist acompanha **cada versão** de cada minuta: a v1 e cada versão nova depois de um ajuste. Preencha-o depois de `estado.py minuta --acao registrar` e antes de pedir a decisão (passo 5 de `minuta-por-ponto.md`).

A análise jurídica é do analista. O checklist mostra o que você conferiu, onde conferiu e o que ficou para ele, para que a aprovação recaia sobre um texto verificado e não sobre a sua palavra.

## Como preencher

- **✓**: conferido nesta versão, com a fonte aberta de novo. Diga em poucas palavras como ("trecho igual ao da página PDF 23"). Quando o item não tiver objeto, marque ✓ e diga por quê ("✓ não há dado de CCT").
- **✗**: há problema. Se você mesmo pode corrigir (trecho, localizador, status, marcador), corrija o arquivo, registre de novo e refaça a tabela antes de apresentar. Só chega ao analista o ✗ que depende dele, com a descrição do problema. As correções que você fez entram na lista "O que mudou" quando a versão não é a v1.
- **pendente**: depende de algo fora do seu alcance nesta sessão (regulamento do ente, CCT sem provedor, feriado local, página por leitura visual). Diga o que falta. Toda pendência também aparece na seção "Pendências de conferência" da minuta.

Não marque ✓ por memória do levantamento. A minuta pode ter mudado o trecho ou a página ao ser escrita, e o checklist só vale se reflete esta versão.

Para conferir um trecho, procure um fragmento curto com `grep -n -F` e leia a página inteira: o texto extraído de PDF quebra a linha no meio da frase, e a frase inteira raramente cabe numa linha só.

## Tabela

A coluna "Onde conferir" abaixo diz a você onde olhar. Na tabela que vai ao analista, troque-a pelo lugar em termos dele: o documento e a página ("edital, página PDF 23"), "catálogo de fontes do estudo", "fontes novas desta triagem". Caminhos internos da skill e hashes não ajudam quem audita o texto.

Copie a tabela, troque `<ID>` e `<N>` e preencha a última coluna.

| Item | O que conferir | Onde conferir | Resultado |
| :-- | :-- | :-- | :-- |
| 1. Trecho | O trecho entre aspas é idêntico ao texto da página indicada, com cortes marcados `[...]` | `<pasta>/texto/<arquivo>.txt`, no marcador `=== página PDF N ===`, `[¶N]`, `L<n>:` ou `=== texto ===` (TXT e MD); página sem texto ou com falha de extração, ou arquivo não extraído: Read com `pages` (anotar "leitura visual") | |
| 2. Localizador | Documento, item ou cláusula, página PDF e página impressa quando divergem; "página não verificada" em DOCX; aba e linha em XLSX | `<pasta>/texto/`, `<pasta>/documentos.md`, `<pasta>/mapa-secoes.md` | |
| 3. Cruzamento | Cada documento cruzado diz o que a minuta afirma, no localizador indicado | `<pasta>/texto/` (página de cada documento); item em `<pasta>/levantamento.md` | |
| 4. ID e status | Cada fonte externa tem marcador `[ID · status]` e o status bate com o índice | `<skill>/references/estudo/indice-fontes.md`; linha completa em `catalogo-fontes.md` | |
| 5. "a conferir" | Nenhuma fonte `a conferir` aparece como certa nem sustenta sozinha um pedido | Marcadores da minuta × coluna Status do índice | |
| 6. Não citáveis e só históricas | Nenhuma fonte `não (histórico)` (`EXT-PEND-*`) ou `não (citação errada)`; fonte "Uso só histórico" no índice, ou "(só histórico)" e "(histórica)" no mapa, aparece só para datar a regra, nunca como fundamento | Colunas Nome e Citável do índice; parêntese da fonte no mapa | |
| 7. Fonte nova | Cada `NOVA-NN` tem URL oficial (Planalto, Pesquisa de Jurisprudência do TCU, Portal de Compras), data da consulta e status "fonte nova — conferir" | `<pasta>/fontes-novas.md` | |
| 8. Transcrição | Dispositivo ou enunciado entre aspas só se aberto na fonte oficial nesta sessão (dizer onde e quando) ou trazido entre aspas como `conferido` no catálogo | Catálogo; registro da consulta nesta sessão | |
| 9. Esfera | Ente estadual, distrital ou municipal: toda fonte `federal (União)` leva "conferir no regulamento do ente". Fonte de um ente específico ("estadual (DF)", "estadual (SP)", "municipal") só fundamenta edital daquele ente | Esfera em `<pasta>/documentos.md` ou no status (`certame.esfera`); coluna Esfera do índice | |
| 10. CCT | Todo dado de CCT tem valor, cláusula, provedor e localizador, ou "conferir na CCT" com a identificação da convenção | Item em `<pasta>/levantamento.md`; `<skill>/references/consulta-cct.md` | |
| 11. Pedido | IMP: o pedido corrige a cláusula dos fatos, na medida do vício, e a redação retificadora corresponde a ele. ESC: as perguntas respondem à dúvida, sem tese embutida, e o "Do fundamento" cita o art. 164 em uma linha, sem datas | Seções "Dos fatos" e "Do pedido" (ou "Da dúvida", "Da pergunta" e "Do fundamento") | |
| 12. Contraponto | O contraponto registrado no levantamento está enunciado e respondido com fato ou fonte (ESC: não se aplica) | Item em `<pasta>/levantamento.md`; seção "Da fundamentação" | |
| 13. RERI | Nenhum fato ou fundamento vem de errata, aviso, retificação ou resposta, nem de páginas de ato da RERI dentro de outro arquivo | Atos da RERI listados em `<pasta>/documentos.md` | |
| 14. Dado pessoal | Sem nome de servidor, CPF, e-mail ou telefone pessoal; pessoas só pelo cargo | Minuta inteira | |
| 15. Impugnante | Sem dados da impugnante, endereçamento, fecho ou assinatura | Minuta inteira | |
| 16. Versão | O arquivo apresentado é o registrado: `minuta_em_revisao` com `registrada: true` e `versao` igual à do cabeçalho; nenhum alerta "minuta <ID> alterada depois do registro" em `alertas`; `proxima_acao` pedindo para apresentar a minuta. O status não mostra o sha256 da minuta em revisão; se quiser comparar, os 12 primeiros caracteres de `sha256sum minutas/<ID>.md` aparecem no evento `minuta_registrar` do `registro.md` | `estado.py status`; `registro.md` | |

## Como apresentar

Na mesma resposta, nesta ordem:

1. uma linha com o ID, a versão e o título;
2. a partir da v2, a lista "O que mudou desde a v<N>": o ajuste pedido e cada correção feita por você, inclusive as que o checklist apontou;
3. a minuta inteira, como está no arquivo;
4. a tabela preenchida, com a coluna "Onde conferir" em termos do analista;
5. as pendências que dependem do analista, se houver;
6. a pergunta, exatamente assim:

> Decida sobre a <ID> v<N>: aprovo / ajuste: <o que mudar> / descarto.

Lembre o analista, em uma linha, de que "ok", "segue", "pode seguir" ou "aprova todas" não valem como decisão: cada minuta precisa de "aprovo", "ajuste: ..." ou "descarto" sobre ela. Isso existe porque a aprovação é a autorização para a minuta entrar na peça, e uma resposta genérica não mostra que esta versão foi lida.

## Da resposta ao comando

Passe em `--evidencia` a frase literal do analista, inteira, sem tirar palavras, entre aspas simples (`estado-e-retomada.md`, seção 5). O script aceita algumas frases que não decidem a minuta; a coluna "Comando" vale mesmo quando o script aceitaria outro.

| Resposta do analista | Comando | O que acontece |
| :-- | :-- | :-- |
| "aprovo" (sobre esta minuta, sem pedir mudança) | `minuta --id <ID> --acao aprovar` | A versão fica aprovada; siga a `proxima_acao` |
| "ajuste: ..." | `minuta --id <ID> --acao ajustar` | A versão vai para `minutas/historico/<ID>.v<N>.md`. Escreva a v<N+1> a partir dela, registre e apresente com "O que mudou" e a tabela inteira de novo |
| Aprovação que também pede mudança, com ou sem "mas" ("aprovo, mas troque…", "aprovo, só troca…", "aprovo; ajusta o parágrafo 2", "aprovo com a troca de…") | `minuta --id <ID> --acao ajustar`, se a frase diz o que mudar; nenhum, se não diz | Aprovação com ressalva é ajuste. Se a frase diz o que mudar, registre-a como ajuste e avise o analista de que a minuta volta como nova versão; se não diz, pergunte o que mudar. Nunca registre como aprovação, mesmo que o script aceite |
| "descarto" (ou excluir, retirar, remover, não usar) | `minuta --id <ID> --acao descartar` | O arquivo vai para o histórico e o item sai da fila |
| "ok", "segue", "aprova todas" | nenhum | Repita a pergunta sobre a minuta em revisão |
| Frase que decide também outra minuta ("aprovo esta e a próxima", "aprovo, e a seguinte também") | nenhum | É aprovação em lote, mesmo que o script aceite. Diga que a próxima será decidida quando for apresentada e repita a pergunta só sobre a em revisão |
| Pergunta, dúvida ou pedido de explicação | nenhum | Responda e repita a pergunta de decisão |

Se o script recusar a frase, não a reescreva para ela passar. Mostre o motivo da recusa e repita a pergunta. Nunca use para esta minuta uma frase já registrada para outra.

## Exemplo preenchido

Para a minuta IMP-03 v1 do exemplo de `minuta-por-ponto.md` (certame fictício), como vai ao analista:

| Item | O que conferir | Onde conferi | Resultado |
| :-- | :-- | :-- | :-- |
| 1. Trecho | Trecho idêntico ao da página | Edital, página PDF 23 (texto extraído) | ✓ igual ao item 8.6.3 |
| 2. Localizador | Documento, item, páginas | Texto extraído e relação de documentos | ✓ página PDF 23, impressa 21; TR página PDF 52, impressa 18 |
| 3. Cruzamento | TR, ETP e minuta do contrato | TR, páginas PDF 49 e 52; ETP, páginas PDF 61 a 72; minuta do contrato, páginas PDF 90 e 91 | ✓ TR repete no 12.3; ETP sem menção a capital ou patrimônio; cláusulas nona e décima conferem |
| 4. ID e status | Marcadores × índice | Catálogo de fontes do estudo | ✓ 7 fontes, todas `conferido` |
| 5. "a conferir" | Nenhuma como certa | Catálogo de fontes do estudo | ✓ nenhuma fonte `a conferir` |
| 6. Não citáveis e só históricas | Nenhuma | Catálogo de fontes do estudo | ✓ nenhuma não citável nem só histórica |
| 7. Fonte nova | URL e data | Fontes novas desta triagem | ✓ não há fonte nova |
| 8. Transcrição | Só texto aberto ou entre aspas no catálogo | Catálogo de fontes do estudo | ✓ só o art. 55, § 1º, entre aspas no catálogo; art. 69 e Súmula 275 em paráfrase |
| 9. Esfera | Aviso nas fontes federais (União); fonte de outro ente | Relação de documentos (ente municipal); catálogo | ✓ nenhuma fonte `federal (União)` nem de outro ente citada |
| 10. CCT | Provedor de cada dado | Item IMP-03 do levantamento | ✓ não há dado de CCT |
| 11. Pedido | Pedido e redação × vício | Dos fatos, Do pedido | ✓ corrige só a cumulação; mantém o percentual |
| 12. Contraponto | Enunciado e respondido | Item IMP-03 do levantamento; Da fundamentação | ✓ risco trabalhista respondido com art. 121, § 3º, e art. 98 |
| 13. RERI | Nada de ato da RERI | Relação de documentos | ✓ nenhum ato da RERI no material |
| 14. Dado pessoal | Nenhum | Minuta | ✓ |
| 15. Impugnante | Nenhum dado | Minuta | ✓ |
| 16. Versão | Registrada e sem edição | Estado da triagem | ✓ registrada, v1, sem alerta de alteração |

Pendências para o analista: transcrever ou não o art. 69, § 4º, e a Súmula 275; preferência entre patrimônio líquido e capital social na redação sugerida.

> Decida sobre a IMP-03 v1: aprovo / ajuste: <o que mudar> / descarto.
