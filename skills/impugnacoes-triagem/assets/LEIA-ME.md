# Modelos da peça final

Esta pasta guarda os modelos da peça de impugnação e da peça de esclarecimento. **Hoje ela não tem modelo**: os modelos e a geração do PDF ficam para uma fase futura do projeto. Este arquivo é o contrato que eles vão seguir, para que a skill, os modelos e o script de PDF possam ser feitos em momentos diferentes sem se desencontrar.

"Fase futura", aqui, é uma etapa do projeto (modelos e PDF). Não confunda com a Fase 5 do `SKILL.md`, que é o passo da peça final dentro de cada triagem e já existe: é nele que a skill para enquanto não houver modelo.

## Enquanto não houver modelo: a skill para no passo da peça

Quando todas as minutas selecionadas estiverem aprovadas ou descartadas, a skill:

1. roda `estado.py peca --pasta <pasta> --acao verificar` e lista ao analista as minutas aprovadas por tipo (ID e versão);
2. lembra os itens em "avaliar depois", com o prazo, e pergunta se ele quer decidir algum agora;
3. informa o analista de que não há modelo em `assets/` e de que a peça final será montada quando ele existir;
4. para aí, sem perguntar o formato da peça, que só faz sentido com modelo.

O `estado.py peca --acao confirmar` recusa a confirmação enquanto não houver modelo, antes mesmo de conferir a frase do analista. Ele procura o modelo só nesta pasta, sem opção para apontar outra. A skill não contorna a recusa: não gera PDF, DOCX nem uma "peça consolidada" improvisada e não cria nem altera arquivos nesta pasta. Uma peça montada sem o modelo revisado sairia sem a qualificação, o endereçamento e o fecho conferidos, e poderia ser protocolada assim por engano. As minutas aprovadas em `minutas/` são a entrega desta etapa.

## Nomes dos arquivos

| Arquivo | Uso |
| :-- | :-- |
| `modelo-impugnacao.<ext>` | Peça de impugnação |
| `modelo-esclarecimento.<ext>` | Peça de pedido de esclarecimento |

O `estado.py peca` só reconhece, nesta pasta, o nome exato `modelo-<tipo>.<extensão>`, com uma extensão só e arquivo não vazio. Cópia de editor (`modelo-impugnacao.md~`, `.bak`, `.swp`), arquivo oculto ou com sufixo a mais não conta como modelo: não é o arquivo revisado. A extensão se decide na fase futura, junto com o formato de montagem. Mantenha um arquivo por tipo: se houver mais de um, o script usa o primeiro em ordem alfabética.

## O que o modelo traz

O modelo é o texto fixo da peça, revisado pelo analista. A skill não escreve nem altera essas partes:

- **Endereçamento:** a autoridade a quem a peça se dirige, com os marcadores do certame.
- **Qualificação da impugnante:** os dados de cada empresa do grupo (razão social, CNPJ, endereço), um bloco por empresa. O analista escolhe qual empresa apresenta a peça.
- **Tempestividade e cabimento:** o parágrafo sobre o prazo do art. 164 (`EXT-LEI14133-ART164`), com as datas preenchidas. As minutas não repetem esse parágrafo: a de impugnação não trata da tempestividade, e a de esclarecimento cita o art. 164 em "Do fundamento" só como base da pergunta, em uma linha e sem datas (`references/minuta-por-ponto.md`, seção 4).
- **Fecho:** local, data e o bloco de assinatura.

Dados de pessoa física, como o nome, o CPF e o cargo do representante que assina, **não entram no git**. Eles ficam num arquivo local, fora do controle de versão, que a fase futura define. O modelo só traz o marcador. Mesmo com esses dados, a skill não assina, não protocola e não envia a peça.

Citação de norma no texto fixo segue as regras da skill: ID do catálogo e status, nada citado de memória.

## Campos que a skill preenche

Proposta de marcadores (a fase futura pode ajustar os nomes; o que importa é a origem de cada um):

| Marcador | O que vai | De onde vem |
| :-- | :-- | :-- |
| `{{ORGAO}}` | Órgão licitante | `estado.json` (certame, `orgao`) |
| `{{CERTAME}}` | Modalidade, número e ano | `estado.json` (certame) |
| `{{PROCESSO}}` | Número do processo administrativo, se o edital o informar | `documentos.md`, linha "Processo administrativo" (tirada do preâmbulo do edital) |
| `{{DATA_ABERTURA}}` | Data da sessão pública | `estado.json` (prazo, `abertura`) |
| `{{DATA_LIMITE}}` | Data-limite do art. 164 | `estado.json` (prazo, `data_limite`) |
| `{{EMPRESA}}` | Qual empresa do grupo apresenta a peça | Escolha do analista |
| `{{PONTOS}}` | Corpo de cada minuta aprovada (ver abaixo) | `minutas/<ID>.md`, versão aprovada |
| `{{PEDIDOS}}` | Impugnação: pedidos principais e subsidiários. Esclarecimento: perguntas numeradas | Seções "Do pedido" ou "Da pergunta" das minutas aprovadas |
| `{{ANEXOS}}` | Rol de provas e anexos | Seções "Provas e anexos indicados" das minutas aprovadas |
| `{{DATA_PECA}}` | Data da peça | Dia da montagem |
| `{{REPRESENTANTE}}` | Bloco de assinatura | Arquivo local fora do git; nunca a skill |

O que vai para `{{PONTOS}}`:

- da minuta de impugnação: "Dos fatos" e "Da fundamentação";
- da minuta de esclarecimento: "Da dúvida" e "Do fundamento".

Ficam de fora o cabeçalho e as "Pendências de conferência". Os marcadores de fonte `[ID · status]` são retirados ou convertidos no estilo de citação do modelo. A montagem renumera os parágrafos. A estrutura das minutas está em `references/minuta-por-ponto.md`.

## Os dois formatos

O analista escolhe o formato separadamente para impugnação e para esclarecimento, digitando uma frase que traz o tipo e o formato: "confirmo a peça de impugnação em formato único" (ou "de esclarecimento", "em formato por ponto"). A skill registra a frase como veio, com `estado.py peca --pasta <pasta> --acao confirmar --evidencia '<frase do analista>'`, e o script tira dela o tipo e o formato (`unico` ou `por_ponto` no `estado.json`). Resposta fora do formato não confirma nada: a skill mostra a frase exata e espera que ele a digite.

- **Peça única (`unico`):** uma peça por tipo, com todos os pontos aprovados daquele tipo na ordem dos IDs e os pedidos consolidados e numerados no fim.
- **Uma peça por ponto (`por_ponto`):** uma peça para cada minuta aprovada, cada uma com o seu pedido.

Nos dois formatos, só entram as versões aprovadas, conferidas pelo sha256 registrado. Se uma minuta mudou depois de aprovada, o `estado.py peca --acao verificar` aponta a pendência e a montagem não segue.

## Geração do PDF (fase futura)

Um script modular, em duas etapas separadas:

1. **Montagem:** preenche o modelo com as minutas aprovadas e os campos acima e gera um documento intermediário. O texto das minutas entra como foi aprovado, sem reescrita.
2. **Renderização:** transforma o documento montado em PDF, com backend trocável e configuração de timbre, fontes e margens.

A separação permite trocar o visual ou o backend sem mexer na regra de quais minutas entram, e conferir o documento montado antes de gerar o PDF. Nenhuma das etapas assina, protocola ou envia.

## Para quem criar um modelo

Esta seção é para quem mantém a skill, fora de uma triagem. A skill em execução não cria nem altera modelo, mesmo que o analista peça: um modelo improvisado para destravar a peça contornaria a revisão que o portão exige.

1. Nomeie o arquivo exatamente como na tabela de nomes (`modelo-<tipo>.<extensão>`), um por tipo e não vazio.
2. Use os marcadores da tabela de campos; não escreva no modelo texto que dependa do certame.
3. Deixe de fora qualquer dado de pessoa física.
4. Rode `estado.py peca --pasta <pasta> --acao verificar` numa triagem de teste e confira que o campo `modelos` mostra o arquivo.
5. Atualize este LEIA-ME e o passo da peça no `SKILL.md`.
