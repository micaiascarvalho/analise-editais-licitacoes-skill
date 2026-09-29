# Impugnação de editais TCU no Open WebUI

Pacote independente, criado a partir de `skills/impugnacao-editais-tcu`. A versão original permanece intacta. A skill orienta o raciocínio e as decisões; a Tool fornece extração, leitura e busca. Não inclui ferramenta para protocolar, gerar DOCX/PDF, pesquisar a web ou conferir automaticamente jurisprudência.

## Conteúdo

- `SKILL.md`: importar como Skill; autocontido, sem depender das referências locais do pacote original.
- `tools/impugnacao_tcu.py`: arquivo Python único para colar no editor de Tools. Não depende de instalar os scripts originais.
- `fixtures/edital-teste.txt` e `fixtures/tr-teste.txt`: anexos fictícios para teste.
- `tests/`: testes técnicos de desenvolvimento, não cadastrar como Tools.

## 1. Preparar o ambiente

Use uma instalação que tenha Workspace > Skills e Workspace > Tools, com permissão para criar ambos. Os nomes dos menus podem variar conforme versão e tradução. Este pacote foi desenvolvido contra a documentação e o código público consultados em 28/09/2026; não foi instalado em uma instância Open WebUI nesta sessão.

Escolha um modelo/provedor que suporte chamadas de ferramentas e habilite Function Calling em modo Native. Ter suporte nominal não garante boa seleção de ferramentas: o roteiro abaixo verifica o comportamento do modelo.

O backend precisa de Python compatível com Open WebUI, SQLite com FTS5 e `pypdf==6.10.0`. Pydantic já faz parte do Open WebUI. O cabeçalho da Tool declara a dependência pypdf; se sua instalação impedir a instalação de dependências de plugins, o administrador deverá instalá-la na imagem/ambiente do backend. Instalar no computador cliente não instala no contêiner.

Não é necessário Open Terminal, chave de API TCU nem banco vetorial.

## 2. Cadastrar a Tool

1. Entre em Workspace > Tools e crie uma ferramenta.
2. Abra `tools/impugnacao_tcu.py` em um editor e copie todo o conteúdo para o editor de código da ferramenta. O arquivo é Python, não um JSON de exportação do Open WebUI.
3. Use o nome `Impugnacao Editais TCU` e salve.
4. Nas configurações/Valves, mantenha inicialmente:
   - `DATA_DIR`: vazio. A Tool usa `<DATA_DIR do Open WebUI>/impugnacao_tcu`.
   - `MAX_FILE_MB`: 25.
   - `TCU_ENABLED`: verdadeiro.
5. Garanta que o diretório de dados do backend esteja em armazenamento persistente. Na instalação Docker padrão, confira o volume de `/app/backend/data`; não troque seu volume existente só para este teste. Para configuração personalizada, `DATA_DIR` deve ser um diretório acessível e gravável dentro do backend, não um caminho do computador cliente.

Métodos expostos: `listar_anexos`, `indexar_anexos`, `ler_documento`, `pesquisar_evidencias`, `consultar_status`, `coletar_acordaos_tcu`.

A Tool acessa apenas uploads pertencentes ao usuário autenticado, mesmo quando o usuário é administrador. Uploads compartilhados de terceiros e coleções Knowledge não são importados automaticamente. Para testar, anexe seus próprios arquivos ao chat.

## 3. Importar a Skill

Em Workspace > Skills, use a opção de importação ao lado de Create e selecione `SKILL.md`. Na documentação atual, a opção pode se chamar **Import JSON**, mas aceita também `.md`. Revise e salve o editor preenchido.

Se o importador da sua versão não aceitar Markdown, crie manualmente a skill:

- ID/nome: `impugnacao-editais-tcu-openwebui`.
- Descrição: `Analise editais e prepare impugnações fundamentadas.`
- Conteúdo: corpo de `SKILL.md`, a partir do título, sem o bloco YAML inicial.

Se não houver área Skills, verifique a versão e as permissões com o administrador. Como teste provisório, o corpo pode ser usado como instrução de sistema de um modelo personalizado; isso não testa o carregamento nativo de skills.

## 4. Habilitar no chat

Abra um chat novo com o modelo escolhido e habilite a Tool no menu de integrações/ferramentas. Digite `$` e selecione a skill importada para carregá-la explicitamente no primeiro teste. Também é possível associá-la ao modelo em Workspace > Models.

Para análises jurídicas reais, habilite adicionalmente ferramentas de pesquisa web e leitura de páginas oficiais. O pacote não configura provedor de busca. O teste documental abaixo pode rodar sem web; o modelo deve declarar a falta de verificação jurídica atual.

## 5. Teste documental controlado

Anexe os dois arquivos da pasta `fixtures`, aguarde o upload e envie, após selecionar a skill com `$`:

```text
Use o certame_id teste-001-v1. Liste os anexos e indexe os dois arquivos no corpus edital. Consulte o status e leia todos os trechos com ler_documento, avançando a paginação quando necessário. Compare os prazos e apresente uma matriz de achados com fontes e contrapontos. São documentos fictícios: não pesquise o órgão, não invente jurisprudência e não redija a peça antes de eu escolher os pontos.
```

Resultado esperado:

- Chamadas reais às ferramentas, visíveis no chat, com `ok: true`.
- Inventário com dois arquivos no corpus `edital`.
- Divergência entre 12 meses no edital e 24 meses no TR, com nomes e localizadores das duas fontes.
- Ausência de afirmação de que um documento necessariamente prevalece sobre o outro.
- Classificação fundamentada, podendo ser esclarecimento ou proposta de correção condicionada ao contexto; não exigir uma única classificação jurídica para este teste.
- Lista de opções e espera pela seleção, sem gerar uma impugnação completa antecipadamente.

Teste a busca em seguida:

```text
No certame teste-001-v1, execute pesquisar_evidencias com consulta "prazo execução meses", corpus edital e limite 5. Mostre as fontes encontradas e explique os limites da busca.
```

Devem aparecer os dois arquivos. A busca combina palavras por OR; não é busca vetorial ou prova de cobertura integral.

## 6. Testar persistência e separação

No mesmo usuário, abra outro chat, habilite a Tool e peça:

```text
Execute consultar_status para teste-001-v1 e depois para teste-vazio-001. Não importe novos documentos.
```

O primeiro deve manter os documentos; o segundo deve estar vazio. Cada usuário recebe uma pasta derivada de seu identificador autenticado. Se houver uma segunda conta para teste, ela deve ver um índice vazio para o mesmo `certame_id`.

## 7. Testar a conexão com o TCU

```text
No certame teste-001-v1, execute coletar_acordaos_tcu com inicio 0, quantidade 2 e paginas 1. Depois consulte o status. Informe quantos registros vieram e o limite da cobertura. Não trate esses acórdãos como precedentes pertinentes ou verificados.
```

O resultado pode trazer dois registros ou uma resposta de erro explícita, conforme disponibilidade da API/rede. Não há filtro temático nesse endpoint. Se a coleta funcionar, o corpus `tcu` deve constar no status. Os registros devem permanecer como candidatos com inteiro teor não conferido. Não espere encontrar um tema jurídico específico nessa amostra.

A coleta depende de saída HTTPS para `dados-abertos.apps.tcu.gov.br`. Não repita sem limite em caso de bloqueio. A busca oficial na web deve complementar o índice em casos reais.

## 8. Testar seleção e minuta

```text
Inclua somente o ponto sobre a divergência dos prazos. Prepare uma minuta de teste com campos para os dados que faltam. Não protocole.
```

Verifique as seis partes da minuta, correspondência entre fatos e pedidos, campos para qualificação/destinatário e ausência de afirmação de tempestividade sem datas verificadas. Nenhum protocolo real deve ocorrer: este pacote não tem ferramenta de envio.

## 9. Teste com edital real

Crie chat novo, use novo `certame_id` e anexe edital, TR e demais documentos, inclusive retificações. Ative pesquisa web/leitura oficial. Peça primeiro somente a matriz e a cobertura. Confira manualmente uma amostra de transcrições e cada precedente utilizado na peça. Só depois escolha os pontos para a minuta.

PDF digitalizado exige OCR externo; páginas sem texto produzem aviso ou falha. PDFs com algum texto, mas com partes em imagem, ainda podem perder conteúdo sem aviso automático. Tabelas e notas exigem conferência no original. DOCX não conserva paginação, nem relações de células no índice, e não indexa cabeçalhos, rodapés ou notas.

## Dados e limites

- O índice guarda textos, nomes, hashes e localizadores. Não envia documentos a serviço de embeddings; a saída da Tool é, porém, entregue ao modelo configurado no Open WebUI, conforme o provedor usado por você.
- O isolamento é por usuário + certame, não por chat. Não reutilize o ID para outro cliente ou versão.
- Reindexar o mesmo upload substitui seus trechos. Reenviar o arquivo cria outro ID e mantém o anterior: use novo `certame_id` para uma versão limpa.
- Excluir chat/upload não remove o índice. Para descarte, o administrador deve remover o banco específico do certame na pasta do usuário, com a Tool fora de uso, incluindo arquivos auxiliares SQLite se existirem. O pacote não expõe exclusão ao modelo.
- Não usar armazenamento de rede incompatível com travas SQLite. Múltiplas réplicas de backend precisam de avaliação própria de armazenamento/concorrência; este pacote destina-se inicialmente ao teste em um backend.
- A integração de uploads usa `Files.get_file_by_id` e `Storage.get_file` do backend, que podem mudar entre versões. O adaptador aceita lookup síncrono e assíncrono. Falha de importação exige conferir a versão, não liberar acesso arbitrário a caminhos.
- Não há atualização agendada, benchmark jurídico, geração de arquivos nem monitoramento automático.

## Diagnóstico

| Sintoma | Conferir |
|---|---|
| Modelo responde sem chamar a Tool | Habilitação no chat, modo Native e suporte do modelo; peça `consultar_status` explicitamente. |
| Lista de anexos vazia | Reanexar uploads próprios no chat; aguardar upload; Knowledge não equivale a anexo direto. |
| Erro de importação `open_webui` | O Python foi executado fora do backend, ou as APIs internas mudaram. |
| `No module named pypdf` | Dependência no backend/container e política de instalação de plugins. |
| `no such module: fts5` | Build SQLite do backend sem FTS5. |
| Índice desaparece no reinício | Volume persistente/configuração de `DATA_DIR`. |
| Arquivo não pertence ao usuário | Fazer upload com a própria conta; o pacote não lê arquivos de terceiros. |
| Busca TCU vazia | Catálogo parcial; conferir coleta e complementar na pesquisa oficial. |
| Banco bloqueado | Aguardar operação em andamento; revisar concorrência e armazenamento. |

## Validação técnica local

Testes executados: 17 aprovados, incluindo isolamento, propriedade de anexos, paginação, persistência, reindexação e falhas. A integração Open WebUI foi simulada; não houve teste end-to-end na interface nem teste de rede ao vivo nesta adaptação. Os testes não certificam qualidade jurídica.

Para repetir fora do Open WebUI, em ambiente Python de desenvolvimento:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install pydantic packaging 'pypdf==6.10.0'
.venv/bin/python -m unittest discover -s tests -v
```

No Windows, use `.venv\Scripts\python.exe`. Execute a partir da pasta deste pacote. Não importe os arquivos de teste em Workspace > Tools.

## Fontes verificadas

Consultadas em 28/09/2026:

- [Skills: importação, ativação e formato](https://docs.openwebui.com/features/workspace/skills/).
- [Desenvolvimento de Tools: classe, Valves e argumentos injetados](https://docs.openwebui.com/features/extensibility/plugin/tools/development/).
- [Modelo de arquivos do backend](https://github.com/open-webui/open-webui/blob/main/backend/open_webui/models/files.py).
- [Provedor de armazenamento do backend](https://github.com/open-webui/open-webui/blob/main/backend/open_webui/storage/provider.py).

### Correção de salvamento da Tool (1.0.1)

O Open WebUI separa `requirements` por vírgulas. A faixa anterior era dividida em dois pacotes e impedia o salvamento. O cabeçalho agora fixa `pypdf==6.10.0`, versão usada nos testes locais. Substitua o conteúdo da Tool pelo arquivo atualizado ou altere apenas a linha `requirements`. Não é necessário atualizar o pip para corrigir esse erro.
