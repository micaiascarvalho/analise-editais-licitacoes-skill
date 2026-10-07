# Avaliação comportamental da triagem

Os casos de `cases.json` incluem recortes de peças, saídas anteriores, trechos resumidos do edital CBMDF e um controle sintético; **não equivalem ao conjunto integral dos editais**. Servem para testar decisões diante do texto fornecido; não permitem validar a legalidade final dos certames. Não mostre `expected_class`, `must_identify` nem `must_not_assert` ao modelo avaliado.

## Procedimento reproduzível

1. Para cada caso de `cases.json`, forneça o `SKILL.md` e somente `origin` e `materials` como entrada. Como o texto desses casos já foi fornecido, a leitura ou extração de arquivos não se aplica. Peça cobertura, classificação principal e matriz de achados. Use a mesma versão do modelo e as mesmas entradas ao comparar revisões da skill.
2. Registre a resposta integral, versão da skill, modelo e data. Nos casos textuais, pesquisa externa ou afirmação de leitura de arquivo não fornecido invalida o ensaio. Em avaliação separada com arquivo ou link sem texto, permita ferramentas de extração conforme a skill e registre páginas e anexos efetivamente lidos; pesquisa jurídica independente continua fora do escopo.
3. Pontue por caso: **classe** (1 se coincide com `expected_class`), **fundamentação documental** (1 se identifica todos os itens de `must_identify` sem inventar fonte), **contenção** (1 se não afirma nenhum `must_not_assert`). Um caso passa com 3/3. Não conte apenas palavras iguais: julgue o sentido jurídico e documental. Se um caso admitir outra classe após revisão jurídica, corrija o gabarito com justificativa registrada antes de usá-lo para comparar versões.
4. Registre à parte citações legais ou jurisprudenciais inventadas, afirmações de leitura de anexo ausente, peça redigida ou pedido de protocolo. Qualquer ocorrência exige correção antes da instalação.

## Comparação inicial e limites

A saída anterior do modelo para o FMS sugeriu como ponto suficientemente sustentado o uso de e-mail `gmail.com`; `FMS-07-email` mede a correção desse falso positivo. A mesma saída não tratou de divergências de jornada, critério mensal/anual, prepostos e materiais, mas declarava cobertura limitada das seções disponibilizadas. Por isso, a ausência desses temas **não é uma medida de recall comparável** aos novos casos.

A outra saída disponível foi produzida para o CBMDF, edital diferente; não a use para calcular ganho quantitativo no FMS. Quando o edital FMS e os anexos completos forem fornecidos, crie uma amostra anotada por revisor jurídico e execute versão antiga e nova **sobre a mesma entrada**. Nessa avaliação, conte cobertura dos achados relevantes, falsos positivos, fidelidade das transcrições, classificação da providência e pendências declaradas. Não use a peça do analista como gabarito infalível: algumas teses também exigem prova ou podem restringir a competição.

Nos casos de objeto composto, avalie se o modelo detecta atividades especializadas dentro do item principal, cruza habilitação, justificativa do agrupamento, preço e subcontratação, e distingue uma dúvida documentável de uma restrição demonstrada. A simples diferença entre atividades não basta para marcar impugnação; a existência de subcontratação também não encerra a análise sem conferir seu alcance e as exigências do executor.
