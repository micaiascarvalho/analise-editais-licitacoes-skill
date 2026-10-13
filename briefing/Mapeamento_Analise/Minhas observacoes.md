O modelo deve seguir essa lógica para classificar algo como impugnável:

#### Como cruzar e demonstrar na impugnação:

- **Cruzamento:** Confrontar **Anexos Internos e Meios Externos** a depender do tipo de anexo e o cruzamento a ser feito.
- **A Prova:** O que fazer para mostrar que algo se sustenta como impugnável ou não.
- **Fundamento Jurídico:** Artigo Violado e Princípios Infringidos.

(CAPRICHO PARA PRODUÇÃO FINAL)
A estrutura criada para analisar deve ser versionável, pois a lei pode mudar e a jurisprudência também. Sendo assim toda referência HardCoded para a lei não deve existir no projeto, deve ser consultável. Mas sei que a análise elaborada tem por base a lei (14.133/2021) então existem partes que só se aplicam a ela e isso não pode ser versionável.

(OTIMIZAÇÃO DA ANÁLISE)
Pude perceber que existem vícios frequente em editais. Para esses vícios podemos elaborar impugnações padrões e alterara apenas os parâmetros do edital a ser impugnado.

(ORGANIZAÇÃO POR EDITAL)
Na aplicação podemos armazenar todos os documentos gerados para determinado edital e agrupar isso por edital. A exemplo: Impugnações geradas e Esclarecimentos.

(PROCESSO DO PIPELINE)
Na última etapa, das retificações e esclarecimentos, esse processo é dinâmico e a cada nova publicação do pregoeiro deve rodar novamente a análise para verificar se há algo impugnável. A aplicação poderia verificar se há novas publicações (Se for possível) e dada a verificação fazer a triagem para impugnar ou apenas sinalizar para o analisar que autorizará a triagem. **Precisamos analisar esse processo separadamente pois tem requisitos específicos e custos também. PROVALVEMENTE PRECISA ANALISAR TODO O EDITAL NOVAMENTE**
