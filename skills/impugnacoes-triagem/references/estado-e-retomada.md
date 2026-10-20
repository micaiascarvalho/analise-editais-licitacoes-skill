# Estado e retomada

Guia do `estado.py` para a skill: o que cada fase espera, cada comando, como registrar a frase do analista, o que cada recusa e cada alerta significam e como retomar uma triagem em sessão nova. Aqui `estado.py` abrevia `<python> <skill>/scripts/estado.py`, e `<pasta>` é a pasta do edital.

Conteúdo:

1. Princípios
2. Arquivos da pasta do edital
3. Fases derivadas e o que destrava cada uma
4. Comandos
5. A frase do analista como evidência
6. Recusas e a resposta certa
7. Alertas do status
8. Retomada em sessão nova
9. Reabrir, itens novos, documentos que chegam depois
10. Validar antes de encerrar

## 1. Princípios

- **O `estado.json` é a fonte de verdade.** O `registro.md` é o resumo legível dele (certame, fase, itens e os últimos 20 eventos), regenerado a cada gravação. Só o `estado.py` escreve os dois. Editar à mão apaga o rastro das decisões e quebra os invariantes que o `validar` confere.
- **A fase não é gravada: é derivada dos dados.** Não existe comando para mudar de fase. A fase muda quando você registra o que a destrava.
- **Saída.** Os comandos que gravam devolvem um JSON com `mensagem` e o status completo; leia os dois. Uma recusa sai com código 1, escreve `erro: …` na saída de erro e não grava nada. Opção ou valor inválido (por exemplo, `--decisao incluido`) sai com código 2 e `usage: … error: …`: é erro de digitação no comando, não portão. Corrija e rode de novo.
- **O script é o mínimo.** Ele impõe a ordem das fases e recusa as frases vagas mais comuns, mas não lê a frase como uma pessoa. Uma frase aceita pode não decidir nada (seção 5).
- **Trava.** Cada pasta tem uma trava (`.estado.lock`): chamadas simultâneas esperam a vez. Mesmo assim, deixe as chamadas ao `estado.py` com quem conversa com o analista; subagentes do levantamento devolvem itens, não registram.
- **Caminhos.** O `estado.py` acha a pasta mesmo que você digite o nome em NFC e o disco esteja em NFD.

Campos do `status`:

| Campo | O que traz |
| :-- | :-- |
| `pasta` | O caminho da pasta do edital |
| `certame` | `slug`, `orgao`, `modalidade`, `numero`, `ano` e `esfera` (`null` se não informada) |
| `fase`, `proxima_acao` | A fase derivada e o que fazer agora, em texto |
| `documentos` | Presentes, faltas e a decisão de prosseguir (com a frase do analista), ou `null` |
| `prazo` | O JSON do `prazo.py` registrado, ou `null` |
| `itens` | `total` e as listas `pendentes`, `incluidos`, `descartados` e `avaliar_depois` |
| `fila_minutas` | Itens incluídos cuja minuta ainda não foi aprovada nem descartada, na ordem de abertura |
| `minuta_em_revisao` | `{id, versao, arquivo, registrada}` ou `null` (sem o sha256) |
| `aprovadas` | `{id, versao, sha256}` de cada minuta aprovada |
| `peca` | `{impugnacao, esclarecimento}`, cada um `null` ou a confirmação da peça daquele tipo |
| `estudo_sha256` | O hash do estudo no início da triagem |
| `alertas` | Avisos que vão ao analista (seção 7) |

## 2. Arquivos da pasta do edital

| Arquivo | Quem escreve | Quando |
| :-- | :-- | :-- |
| `estado.json`, `registro.md` | só o `estado.py` | a cada comando que grava |
| `texto/*.txt`, `texto/inventario.json` | `extrair_texto.py` | Fase 0, e quando chegar documento novo |
| `documentos.md` | a skill | Fase 0, atualizado no portão |
| `mapa-secoes.md` | a skill | início do levantamento |
| `levantamento.md`, `itens.json` | a skill | levantamento (e itens novos depois) |
| `fontes-novas.md` | a skill (quem conversa com o analista) | quando consultar fonte oficial fora do catálogo |
| `minutas/<ID>.md` | a skill | só depois de `minuta --acao abrir` |
| `minutas/historico/<ID>.v<N>.md` | o `estado.py` | ajuste, descarte e reabertura |

## 3. Fases derivadas e o que destrava cada uma

O script testa as condições nesta ordem; a primeira que vale é a fase.

| Fase | Quando o status a mostra | O que a destrava |
| :-- | :-- | :-- |
| `documentos` | Portão não registrado, ou registrado com faltas e sem decisão de prosseguir | `documentos` sem faltas, ou `prosseguir` com a frase do analista |
| `levantamento` | Portão aberto e itens nunca registrados | `itens` (uma lista vazia `[]` registra levantamento sem itens) |
| `selecao` | Algum item pendente | `decidir` até não sobrar pendente |
| `minutas` | Algum item incluído com minuta não aprovada nem descartada | `minuta` (abrir, registrar, decidir) até a fila esvaziar |
| `peca_final` | Há minuta aprovada de um tipo cuja peça não foi confirmada | `peca --acao confirmar`; sem modelo em `<skill>/assets/`, é recusado e a triagem para aqui |
| `concluido` | Nada pendente, ou nenhuma minuta aprovada | — |

Como a ordem é fixa, a fase pode voltar. Itens novos registrados durante as minutas levam a fase de volta a `selecao`, e a minuta em revisão continua esperando decisão. Um `documentos` registrado de novo com uma falta que o analista não autorizou volta a fase para `documentos`.

## 4. Comandos

| Comando | Quando usar | O que exige |
| :-- | :-- | :-- |
| `slug --orgao --modalidade --numero --ano` | Antes do `iniciar`, para saber o nome da pasta | Ano com 4 dígitos; órgão, modalidade e número com letras ou números. Em `--numero`, só o número (`1`, não `1/2026`) |
| `iniciar --raiz --orgao --modalidade --numero --ano [--esfera] [--slug]` | Triagem nova | Pasta inexistente, ou só com `texto/` e `minutas/`. Grava o hash do estudo do `MANIFEST.json` |
| `status --pasta` | Começo de todo turno | Pasta com `estado.json` |
| `documentos --pasta --presentes --faltas [--esfera]` | Portão documental, e de novo quando chegar documento | Os 6 códigos (EDITAL, TR, ETP, PLANILHA, PESQUISA, MINUTA), cada um em uma lista só. `RERI` é recusado |
| `prosseguir --pasta --evidencia` | O analista decidiu seguir sem o que falta | `documentos` registrado com faltas; frase que não seja genérica nem negativa. O script não confere se a frase nomeia cada falta: confira você (seção 5) |
| `prazo --pasta --dados ARQUIVO\|-` | Fase 0, assim que achar a data de abertura; de novo se a data, os feriados locais ou o dia mudarem | O JSON de `prazo.py --json` (campos `abertura`, `data_limite`, `alertas`). Funciona antes do portão |
| `itens --pasta --arquivo ARQUIVO\|-` | Fim do levantamento; depois, só para itens novos (seção 9) | Portão aberto; lista de `{"id", "classe", "titulo"}`; ID `IMP-NN` com classe `impugnacao` ou `ESC-NN` com `esclarecimento`; ID e número inéditos |
| `decidir --pasta --ids IDS\|PENDENTES --decisao incluir\|descartar\|avaliar_depois --evidencia` | Seleção | Portão aberto; itens registrados e sem minuta; frase literal |
| `minuta --pasta --acao abrir` | Fase `minutas`, sem minuta em revisão | Abre só a primeira da fila |
| `minuta --pasta --id ID --acao registrar` | Logo depois de escrever `minutas/<ID>.md` | Arquivo existente e não vazio; `ID` é a minuta em revisão |
| `minuta --pasta --id ID --acao aprovar\|ajustar\|descartar --evidencia` | Depois de apresentar a minuta registrada | Arquivo igual ao registrado; frase literal sobre essa minuta |
| `reabrir --pasta --ids --motivo` | O analista mudou de ideia sobre item que já tem minuta | Item não pendente, ou com minuta; motivo que não seja genérico |
| `peca --pasta --acao verificar` | Fase `peca_final` | Só lê; mostra `pronto` (sem pendências, haja modelo ou não), pendências, aprovadas por tipo e modelos |
| `peca --pasta --acao confirmar --tipo --formato --evidencia` | Peça final, quando houver modelo | Tudo decidido, minuta aprovada do tipo, `<skill>/assets/modelo-<tipo>.*` e a frase do analista |
| `validar --pasta` | Antes de encerrar o turno que gravou algo | Sai com 1 se algum invariante for violado (seção 10) |

A skill não passa `--assets` (no `peca`) nem `--manifesto` (em todos os comandos). Essas opções existem para os testes dos scripts: com elas, o `peca` aceitaria um modelo de outra pasta, que ninguém revisou, e o status deixaria de avisar que o estudo mudou.

**Prazo.** Rode sempre com a data do dia em `--hoje`, acrescente `--feriado-local AAAA-MM-DD:nome` para cada feriado local informado e encadeie:

```bash
<python> <skill>/scripts/prazo.py --abertura 2026-11-03 --hoje "$(date +%F)" --json \
  | estado.py prazo --pasta <pasta> --dados -
```

Se houver ato da RERI no material (em arquivo próprio ou em páginas de outro arquivo, conforme `documentos.md`), use sempre esta variante, também em todo recálculo, porque o registro novo substitui o anterior e o alerta da RERI só entra por ela:

```bash
<python> <skill>/scripts/prazo.py --abertura 2026-11-03 --hoje "$(date +%F)" --json \
  | <python> -c 'import json,sys; d=json.load(sys.stdin); d["alertas"].append("a data de abertura pode ter mudado: conferir no processo da RERI"); print(json.dumps(d, ensure_ascii=False))' \
  | estado.py prazo --pasta <pasta> --dados -
```

Registrar o prazo de novo substitui o anterior. Se o `prazo.py` falhar, o `estado.py prazo` recusa a entrada vazia: corrija o erro do primeiro comando e rode os dois de novo.

## 5. A frase do analista como evidência

A `--evidencia` é o registro de que o analista, e não a skill, tomou a decisão. Por isso ela é a frase dele, não uma paráfrase sua.

- **Copie as palavras dele como ele escreveu**, com abreviações e erros de digitação. Se a mensagem é longa, use a frase inteira em que ele decide, sem trocar, acrescentar nem tirar palavras: mantenha ressalvas, condições, negações e outros IDs da mesma frase. Tirar "todas" de "aprova todas" ou "mas troque o pedido" de uma aprovação faz a frase passar no script e inventa uma decisão que ele não tomou.
- **Não monte a frase.** "O analista aprovou a IMP-01" é um resumo seu e não vale. Também não acrescente "aprovo" nem o ID para a frase passar.
- **A lista do script é o mínimo.** Antes de registrar, confira você mesmo que a frase diz a decisão:
  - prosseguir: que ele segue sem os documentos, nomeando cada falta (por código ou nome), ou "eles" e "todos" quando responde ao relatório que as listou. "Segue com o que tiver" e "pode seguir sem o que faltar" não nomeiam nada. O script não confere: registra como autorizadas todas as faltas do portão;
  - decidir: os IDs, ou "todos", "o resto", "os demais", e um verbo que corresponda a `--decisao`. "Descarta a IMP-01" e "não quero a IMP-01" não registram um `incluir`, mesmo que o script aceite;
  - minuta: "aprovo", "ajuste: …" ou "descarto" sobre a minuta em revisão, e só sobre ela.
  - Respostas como "isso", "pode", "tá", "fechado", "bora", "vai", "sim, pode" ou "faz aí" não registram nada, mesmo que o script as aceite: repita a pergunta no formato que gera a decisão.
- **Pergunte de um jeito que a resposta seja a decisão.** Se você pergunta "posso aprovar?" e ele responde "sim", a evidência seria "sim", que é genérica e será recusada. Pergunte "aprovo / ajuste: … / descarto?". No portão, nomeie as faltas na pergunta ("prossegue sem o ETP e sem a pesquisa?").
- **Aprovação que pede mudança é ajuste.** Se a mensagem aprova e também pede qualquer mudança no texto, com ou sem "mas" ("aprovo, só troca o subsidiário", "aprovo; troque o pedido", "aprovo com a troca do pedido"), registre com `--acao ajustar` e a frase inteira, e avise o analista de que a minuta volta como nova versão. Se a ressalva não diz o que mudar, pergunte. O script só pega algumas ressalvas ("mas", "porém", "se", "quando" e parecidas).
- **Uma frase pode servir a mais de uma chamada na seleção.** "inclui IMP-01, IMP-03 e ESC-02, descarta o resto" registra o `incluir` dos três IDs e, depois, o `descartar` de `PENDENTES`, com a mesma frase. Nas minutas, não: a frase de aprovação vale só para a minuta em revisão. Nunca reaproveite para outra minuta uma frase já registrada (confira no `registro.md`).
- **Frase que decide também outra minuta é lote.** "Aprovo esta e a próxima", "aprovo essa e a seguinte" ou "aprovo, e a próxima também" passam no script, que só pega o lote no plural. Não registre: diga que cada minuta é decidida depois de lida e peça a decisão só sobre a em revisão.
- **A decisão vale depois que ele viu o objeto.** "Já inclui tudo" ou "já aprova tudo" no primeiro pedido não decide itens nem minutas que ainda não foram apresentados. A exceção é o `prosseguir`: uma frase anterior ao relatório vale se nomear cada falta encontrada.
- **Aspas no shell.** Use aspas simples e troque cada aspa simples da frase por `'\''`. Por exemplo, a frase `aprovo a IMP-01, a 'redação sugerida' ficou boa` vira `--evidencia 'aprovo a IMP-01, a '\''redação sugerida'\'' ficou boa'`. Aspas duplas não servem: dentro delas, o shell troca `$4` por vazio e "R$4.800,00" seria gravado como "R.800,00".

Exemplos que passam e decidem: "prossiga sem o ETP e sem a pesquisa"; "não tenho ETP nem pesquisa, pode seguir" (quando as faltas são só essas duas); "ESC-04 eu vejo depois"; "aprovo a IMP-01"; "tá bom, aprovo"; "ajuste: troque o pedido subsidiário pela suspensão do certame"; "descarto essa".

Exemplos que o script aceita, mas que não registram a decisão pedida: "pode"; "fechado"; "segue com o que tiver"; "pode incluir tudo que achar" (antes de ver os itens); "descarta a IMP-01" (para um `incluir`); "aprovo esta e a próxima"; "aprovo, só ajusta o parágrafo 2 dos fatos" (é ajuste, não aprovação).

## 6. Recusas e a resposta certa

Toda recusa diz o que falta. A resposta certa é explicar ao analista e pedir a decisão que falta; nunca contornar. A coluna da esquerda traz um trecho da mensagem do script, que pode vir depois de um ID ou de um caminho.

**Evidência**

| Trecho da mensagem | O que significa | O que dizer ao analista |
| :-- | :-- | :-- |
| `evidência vazia` | Você chamou o comando sem a frase | Nada: pegue a frase dele ou pergunte |
| `é genérico e não vale como decisão` | "ok", "sim", "segue", "pode seguir", "certo", "beleza", "perfeito", "valeu" e parecidas, sozinhas | Que a resposta precisa dizer a decisão (que ele segue sem quais documentos; quais itens incluir; aprovo / ajuste / descarto) |
| `nega ou recusa a ação` | "ainda não", "não prossiga", "não inclua" | Nada a registrar: confirme o que ele quer fazer em vez disso |
| `para aprovar, a frase do analista precisa dizer "aprovo"` | A frase não tem "aprov" | Pergunte se ele aprova a minuta em revisão ou quer ajuste |
| `a frase nega a aprovação` | "não aprovo", "desaprovo" | Pergunte o que ajustar ou se descarta |
| `aprovação em lote não é aceita` | "aprovo todas", "tudo", "as duas", "os demais", "em bloco" | Que cada minuta é decidida sozinha; apresente a em revisão e pergunte só sobre ela. O script não pega o lote no singular ("esta e a próxima"): trate-o igual (seção 5) |
| `a frase cita ESC-02, mas a minuta em revisão é IMP-01` | A frase fala de outro ID | Que a decisão agora é só sobre a IMP-01; o outro ponto vem na vez dele |
| `a frase traz condição, ressalva ou pergunta` | "aprovo, mas…", "aprovaria se…", "aprovo?" | Aprovação com ressalva é ajuste: se a frase diz o que mudar, registre-a com `--acao ajustar` e avise o analista; se não diz, pergunte o que mudar |
| `o ajuste precisa da instrução do analista` | Ajuste com menos de 10 caracteres | Pergunte o que ele quer mudar na minuta |
| `para descartar, a frase do analista precisa dizer "descarto"…` | Descarte sem verbo de descarte ("não vale a pena") | Pergunte se ele descarta a minuta |

**Fluxo e arquivos**

| Trecho da mensagem | O que significa | O que fazer |
| :-- | :-- | :-- |
| `o portão documental não foi resolvido` | Itens, decisão ou minuta antes do portão | Volte à Fase 1 |
| `o portão documental ainda não foi registrado` / `não há faltas no portão` | `prosseguir` fora de hora | Rode `documentos`; sem faltas, não há o que autorizar |
| `a RERI … está fora do escopo desta skill` | `RERI` em `--presentes` ou `--faltas` | Tire o código; registre o ato em `documentos.md` como encaminhado |
| `faltou classificar` / `não pode estar em --presentes e em --faltas` / `código de documento desconhecido` | Classificação incompleta ou errada | Corrija a lista e rode de novo |
| `fora do formato IMP-NN ou ESC-NN` / `incoerente com o ID` / `título vazio` | `itens.json` malformado | Corrija o arquivo |
| `já existe: os IDs são estáveis` / `repete o número de` | ID reaproveitado, ou o `itens.json` completo reenviado | Os IDs são estáveis: mande só os itens novos, com o próximo número livre (seção 9) |
| `nenhum item novo no arquivo` | `itens` repetido sem nada novo | Nada a registrar |
| `nenhum item registrado` | `decidir` ou `reabrir` antes do `itens` | Termine o levantamento e registre os itens |
| `não há itens pendentes` | `decidir --ids PENDENTES` sem pendentes | Nada a registrar: os itens já foram decididos |
| `IDs não registrados` | ID digitado errado ou item que não está no levantamento | Confira o ID com o analista |
| `já tem minuta aberta ou decidida: … use "reabrir"` | Mudança de decisão em item com minuta | Seção 9, a pedido do analista e com o motivo dele |
| `já está em revisão` | Tentativa de abrir a segunda | Apresente a em revisão e peça a decisão |
| `não há minuta a abrir na fase …` / `a próxima da fila é …` | Fora de fase ou fora de ordem | Siga a `proxima_acao`; a fila é IMP por número, depois ESC |
| `nenhuma minuta em revisão` | `registrar` ou decisão sem minuta aberta | Na fase `minutas`, abra a próxima com `minuta --acao abrir`; fora dela, siga a `proxima_acao` |
| `não existe: escreva a minuta antes de registrar` / `está vazio` | Registro antes de escrever | Escreva o arquivo e registre |
| `ainda não foi registrada` | Decisão sobre minuta não registrada | Registre e apresente antes de pedir a decisão |
| `mudou (ou sumiu) depois do registro` | O arquivo não é o que foi registrado | Registre de novo e apresente a versão atual: o analista decide sobre o texto que viu |
| `a minuta em revisão é …, não …` / `informe --id` | ID errado | Use o ID de `minuta_em_revisao` |
| `já está pendente: não há o que reabrir` | Reabertura sem necessidade | Peça a decisão com `decidir` |
| `a peça ainda não pode ser confirmada; pendências` | Algo não decidido | Resolva cada pendência na fase dela |
| `não há minuta de … aprovada` | Peça de um tipo sem aprovadas | Não há peça desse tipo |
| `não há modelo de … em …` | Falta o modelo em `<skill>/assets/` (é o caso hoje) | Informe que a peça final só sai com o modelo e pare; não gere a peça por outro meio, não crie modelo e não passe `--assets` |
| `informe --tipo impugnacao\|esclarecimento e --formato unico\|por_ponto` | `peca --acao confirmar` incompleto | Só se chega aqui com modelo; pergunte o formato ao analista |
| `entrada vazia` | O comando antes do pipe falhou (em geral o `prazo.py`) | Leia o erro do primeiro comando, corrija e rode os dois de novo |
| `já existe: retome com "status"` | `iniciar` numa triagem existente | Retome (seção 8) |
| `já existe sem estado.json e tem …` | Pasta ocupada por outros arquivos | Mostre ao analista; use outro `--slug` só se ele concordar |
| `existe, mas não tem estado.json` | `iniciar` interrompido | Rode o `iniciar` que a mensagem sugere, com os dados do certame |
| `não é JSON válido` / `campo ausente ou inválido` | `estado.json` corrompido ou editado à mão | Rode `validar` e mostre as violações ao analista. Mesmo que ele diga "corrija", não edite o `estado.json`: peça que ele decida entre restaurar uma cópia que tenha do arquivo ou começar uma pasta nova com outro `--slug` (a triagem recomeça do portão) |

## 7. Alertas do status

Leve os alertas ao analista no começo da resposta, uma vez por sessão para os que se repetem.

| Alerta | O que fazer |
| :-- | :-- |
| `o estudo mudou desde o início da triagem` | Avise. Para cada item ainda não aprovado, abra na cópia atual a linha do mapa citada em "regra do estudo" e confira se o critério continua igual. Anote o resultado nas pendências do `levantamento.md`. Item que deixou de valer: proponha descartar (ou `reabrir`, se já tem minuta); a decisão é do analista. Minuta aprovada que cita linha alterada: mostre e pergunte se ele quer reabrir. O alerta continua enquanto o hash for diferente; não há comando que o apague. |
| `o hash do estudo não foi registrado no início` / `MANIFEST.json do estudo não encontrado` | A cópia do estudo está incompleta ou foi movida. Avise; quem mantém o estudo roda `sync_estudo.py --check`. Não recrie o manifesto nem passe `--manifesto`. |
| `minuta X alterada ou removida depois de aprovada` | A versão aprovada não está mais em `minutas/`. Se você sabe exatamente o que mudou (por exemplo, uma edição sua nesta sessão), desfaça e confira com `validar`. Se não, conte ao analista e proponha `reabrir`; reabra só se ele concordar, com o motivo nas palavras dele. Não há "registrar" para minuta aprovada. |
| `minuta X alterada depois do registro` | A minuta em revisão mudou. Registre de novo e apresente a versão atual antes de pedir decisão. |
| `prazo de impugnação vencido em …` / `hoje é o último dia do prazo` | Conta feita com a data de hoje sobre o prazo registrado. Diga isso no início da resposta, numa linha, e siga a fase: o script só alerta, e decidir se ainda vale protocolar é do analista. Se a fase já pede uma decisão dele (portão, seleção, minuta), a pergunta sobre seguir vai junto, sem parar antes. |
| `prazo: ATENÇÃO: …` | Urgência calculada na data em que o `prazo.py` rodou ("data de referência"). Se a sessão é de outro dia, recalcule o prazo (seção 4; com ato da RERI, a variante com o alerta) antes de repetir o alerta. |
| `prazo: conferir o horário-limite no edital` | Procure no edital a hora-limite do protocolo e cite-a no relatório. |
| `prazo: feriados locais não informados` | Pergunte ao analista ou veja o calendário do órgão; recalcule com `--feriado-local`. Se ele confirmar que não há feriado local entre hoje e a abertura, anote isso no cabeçalho do `levantamento.md` e não pergunte de novo: o alerta continua no status, porque o script não tem como registrar "nenhum", e isso é esperado. |
| `prazo: feriados locais de ano fora da contagem (…) não alteraram o prazo` | Um feriado informado caiu fora do período da contagem, em geral por ano digitado errado. Confira a data com o analista e recalcule. |
| `prazo: a data-limite depende do expediente nos pontos facultativos` | Informe as duas datas; na dúvida, vale a mais cedo (`data_limite`). |
| `prazo: a abertura … cai em dia sem expediente` | Confira a data no edital. |
| `prazo: a data de abertura pode ter mudado: conferir no processo da RERI` | Há ato da RERI no material: diga que a data deve ser conferida no processo à parte. |

## 8. Retomada em sessão nova

A memória da conversa anterior não existe; o estado, sim.

1. **Ache a pasta.** Na raiz das triagens (`files/triagens/` ou a que o analista indicar), liste as pastas e compare com o certame. O slug depende de como o número foi digitado no `iniciar`, então não confie só em recalculá-lo. Se o analista der o caminho, use-o. Não crie pasta nova para um certame que já tem uma.
2. **Rode `status`** e leve os alertas ao analista.
3. **Leia o `registro.md`** para ver o que foi decidido e os últimos eventos.
4. **Leia o que a fase pede:**
   - `documentos`: `documentos.md`. Se o portão tem faltas sem decisão, apresente o relatório de novo e pergunte.
   - `levantamento`: `documentos.md`, `mapa-secoes.md` e o `levantamento.md` parcial, se houver. A seção "Progresso" dele diz quais documentos já foram examinados até o fim (`references/levantamento.md`, seção 12): continue do primeiro que não tem a linha "examinado". Documento sem essa linha é refeito, mesmo que haja rascunho dele. Só refaça um documento já examinado se o sha256 do arquivo no `texto/inventario.json` mudou.
   - `selecao`: os itens pendentes no `levantamento.md`. Apresente só esses e peça a decisão.
   - `minutas`: o item da minuta em revisão no `levantamento.md` e o arquivo `minutas/<ID>.md`. Se `registrada` é `false`, termine a minuta conforme `minuta-por-ponto.md` e registre. Se é `true`, apresente de novo com o checklist e peça a decisão. Se o analista disser que já tinha aprovado, explique que a aprovação não foi registrada e peça a frase de novo. Sem minuta em revisão, abra a próxima.
   - `peca_final` ou `concluido`: siga a Fase 5 do `SKILL.md` (primeiro `peca --acao verificar`, depois os itens em "avaliar depois").
5. **Recalcule o prazo** se a sessão anterior foi em outro dia (seção 4; com ato da RERI, a variante com o alerta).
6. **Diga ao analista** em que etapa a triagem está e o que você precisa dele.

Se uma sessão caiu no meio de um ajuste ou de um descarte, com o arquivo já no histórico e o estado ainda não gravado, o próximo comando que grava devolve o arquivo a `minutas/` sozinho e anota `minuta_restaurada` no registro.

## 9. Reabrir, itens novos, documentos que chegam depois

**Reabrir.** Use quando o analista muda de ideia sobre um item que já tem minuta, em revisão, aprovada ou descartada. Reabra só a pedido dele, ou depois que ele concordar com a sua proposta (por exemplo, quando uma minuta aprovada foi alterada e a versão aprovada não pode ser restaurada). Reabrir desfaz uma decisão dele, e o motivo registrado precisa ser dele.

```bash
estado.py reabrir --pasta <pasta> --ids IMP-01 --motivo 'mudei de ideia: o capital social está dentro do limite'
```

- O item volta a pendente e a minuta atual vai para `minutas/historico/<ID>.v<N>.md`. A versão não recomeça: a próxima abertura será a `v<N+1>`.
- A confirmação da peça do mesmo tipo, se houver, é desfeita.
- O motivo vai nas palavras do analista, entre aspas simples como na seção 5; motivo genérico é recusado.
- Depois, peça a nova decisão com `decidir`.
- Para item sem minuta, não precisa reabrir: `decidir` de novo basta.

**Itens novos.** Quando o analista pede para examinar outro ponto, ou quando surge um achado depois do levantamento:

1. Acrescente o item ao `levantamento.md` com o próximo número livre da classe. Nunca renumere nem reaproveite um ID.
2. Mande ao script só os itens novos, num arquivo à parte (`<pasta>/itens-novos.json`) ou pela entrada padrão (`--arquivo -`), e rode `itens`. Reenviar o `itens.json` completo é recusado inteiro ("já existe"), porque o script não pula os IDs já registrados.
3. Atualize `<pasta>/itens.json` com a lista completa, para que ele continue espelhando o `levantamento.md`.
4. A fase volta a `selecao`. Uma minuta em revisão continua esperando a decisão dela.

**Documentos que chegam depois.** Trate cada arquivo novo como na Fase 0 do `SKILL.md`. Antes de extrair, olhe o título e, se preciso, só a primeira página: é por aqui que um ato da RERI costuma chegar, porque retificações e respostas saem dias depois do edital. Ato da RERI não é extraído nem analisado: registre-o em `documentos.md` como "ato da RERI: encaminhado ao processo à parte", avise o analista e registre o prazo de novo com o alerta da RERI (seção 4). Os demais arquivos: extraia, confira os erros do `inventario.json`, atualize `documentos.md` e rode `documentos` com a classificação nova. Depois examine o documento novo como no levantamento e registre o que surgir como itens novos.

## 10. Validar antes de encerrar

Rode `estado.py validar --pasta <pasta>` antes de encerrar todo turno em que gravou algo, antes da peça final e ao concluir. Ele devolve `{"valido": true|false, "violacoes": [...]}` e sai com 1 se houver violação.

| Violação | O que fazer |
| :-- | :-- |
| `arquivo inesperado em minutas/` ou `minuta não aberta ou já descartada` | Arquivo escrito fora do fluxo, por exemplo uma minuta adiantada. Mova-o para fora de `minutas/` (sem apagar) e avise o analista; quando chegar a vez do item, abra a minuta pelo fluxo. |
| `o item … não está incluído` | Minuta de item que não foi incluído. Mova o arquivo para fora de `minutas/` (sem apagar) e confira a seleção com o analista. |
| `minuta aprovada alterada ou removida` | Ver o alerta correspondente (seção 7). |
| `… sem evidência` / `com evidência que não vale` / `sem a decisão correspondente no histórico` / `sem o evento de registro` / `mais de uma minuta em revisão` / `ID repetido` | O `estado.json` foi editado fora do `estado.py`. Não corrija à mão: mostre as violações ao analista e pare até ele decidir entre restaurar uma cópia ou começar uma pasta nova (seção 6, última linha). |
| `peça … confirmada com itens não decididos` ou `com versões que não batem` | A confirmação da peça não vale mais. Avise o analista. |

Um `validar` limpo não aprova nada nem prova que as decisões vieram do analista. Ele confere que o estado e os arquivos são coerentes entre si, mas não detecta uma edição à mão que abre o portão ou inclui um item com uma frase plausível. Por isso a regra é nunca editar o `estado.json`.
