# Teste integral — Pregão Eletrônico FMS nº 111/2026

**Data:** 06/10/2026. **Modelo:** `gpt-6.1-sol`. **Skill:** versão instalada de `impugnacao-editais-tcu`. **Entrada:** texto extraído das 214 páginas do [edital e anexos](../../../files/IMPUGNACOES/FMS/EDITAL+PE+111.2026.pdf), com marcadores da página física do PDF. A [saída cega integral](fms-111-2026-saida-cega.md) foi preservada sem edição.

## Método e limites

O modelo recebeu a skill e o texto integral do PDF, sem a peça do analista ou as saídas antigas. O registro da execução contém apenas mensagens do modelo, **nenhuma chamada de ferramenta**; a análise não pesquisou legislação, não redigiu peça nem tentou protocolo. A extração cobriu as 214 páginas; os dados decisivos das tabelas de proposta, postos e planilha foram conferidos visualmente. A auditoria posterior, separada da execução cega, confrontou a saída com o PDF, a [peça do analista](../../../files/IMPUGNACOES/FMS/IMPUGNAC%CC%A7A%CC%83O%20-%20FMS%20APOIO%20ADM%20HOSPITALAR.docx) e fontes oficiais. A revisão aprofundada se concentrou nos fundamentos da peça, em H01–H15 e nos achados complementares destacados abaixo; **não certifica juridicamente as 31 linhas da saída bruta**.

Registro da execução: 202.543 tokens de entrada e 11.228 de saída; SHA-256 do PDF `3b4629633593c62d7ae51a39be57dbdabbf1d722c765d8cf22296364aab7be28` e da skill instalada `ab12417618ab88756445a3a7487f1c0d2d4425b6e323c2ef428a661041891c53`.

O PDF contém edital (pp. 1–78), TR e seus apêndices (pp. 79–165), modelo de proposta (pp. 166–168), demais anexos e minuta (pp. 169–214). O Anexo F, pp. 159–165, é **modelo de planilha em branco**, não orçamento preenchido. ETP, memória de lotação, despacho NUSO, CCTs, retificações e respostas a esclarecimentos não vieram nesta entrada. Isso não prova que estejam ausentes da publicação ou do processo. A abertura indicada no arquivo é 18/09/2026; este teste é retrospectivo e não confirma a situação posterior do certame.

A peça do analista é referência de *temas examinados*, não gabarito de procedência. A antiga saída da skill para o FMS usou apenas seções disponibilizadas; por isso, a comparação com ela é qualitativa, sem cálculo de ganho de acurácia com entradas desiguais. A outra saída anterior era de um edital CBMDF e não entra no comparativo do FMS.

## Resultado contra os oito fundamentos do analista

| Tema da peça sênior | Saída cega | Auditoria do PDF e classificação mais adequada |
| --- | --- | --- |
| Modo fechado-aberto | H07 localizou a escolha e o rito condicional de aberto-fechado | **Esclarecimento**, não tese demonstrada de troca obrigatória do modo. O TR formal pp. 80–81, itens 1.7.1–1.7.5, traz motivação específica ignorada na peça; o item 6.11 do edital p. 21 começa com “Caso seja adotado”. |
| Insalubridade generalizada | D09 recusou adicional para todos os postos | **Não sustentado** como pedido para os 541 trabalhadores. Lotação hospitalar não prova exposição; falta laudo/despacho NUSO e distribuição por função e unidade. |
| Telefonista | H06 identificou 12×36 no edital/Anexo II e 36h no TR, além do CBO divergente do eletricista | **Impugnação preliminar** para harmonizar as tabelas e custos. A saída classificou como mero esclarecimento, apesar do efeito material sobre sete telefonistas e dois eletricistas (pp. 5–6, 91 e 167). A tese de ilegalidade trabalhista da escala depende da atividade concreta/CCT. |
| Um preposto por hospital | H29 localizou obrigação e dúvida de dedicação | **Esclarecimento/risco de custo**. O TR p. 103 exige um por unidade hospitalar, mas o Anexo F p. 160 admite adaptar rubricas e p. 164 contém “Outros”/custos indiretos; ausência de linha nominal não prova impossibilidade de cotar. |
| Atestado exclusivamente hospitalar | H17/D03 registraram similaridade, três anos, 50% e somatório | **Não sustentado** o pedido sênior de restringir atestados a hospitais sem demonstrar necessidade técnica. O item 8.5.1 p. 27 já exige compatibilidade em características; eventual precisão objetiva do termo “similar” pode ser esclarecida. |
| Materiais “não exaustivos” | H10 confrontou TR p. 102 e anexos C/D/E pp. 144–159 | **Esclarecimento forte**, com potencial de impugnação após conferir se há detalhamento adicional publicado: existem quantidades, mas faltam unidade temporal de reposição e limites para certos insumos de manutenção. |
| Motoristas/ambulância e insalubridade | H21 mencionou transporte de pacientes/material biológico, sem avaliar o adicional; D09 descartou apenas a tese genérica | **Lacuna do teste.** TR p. 93 descreve tarefas que justificam pergunta específica sobre exposição e laudo. Não há prova para impor 20% aos 18 motoristas indiscriminadamente. |
| Cota ME/EPP de 25% | H08 localizou edital p. 62 versus capa p. 2 e TR p. 82 | **Impugnação preliminar** para corrigir regra expressa de participação. A saída subestimou como esclarecimento: item 16.8.1 manda reservar 25%, mas o objeto é lote único de serviços e o TR afasta a cota. |

**Cobertura temática:** sete fundamentos foram enfrentados diretamente; a questão específica dos motoristas apareceu apenas como descrição de tarefas, sem análise do adicional. Cobertura não equivale a concordância: em quatro temas, a saída reduziu ou rejeitou com razão a formulação da peça sênior.

## Oito esclarecimentos da peça

| Questão sênior | Cobertura pela saída cega | Auditoria |
| --- | --- | --- |
| Hora noturna reduzida/12×36 | **Ausente** | Edital p. 18 e TR p. 122 exigem hora reduzida e prorrogação; resta conferir critério de cálculo na escala. |
| Substituto intrajornada | **Parcial, com descarte excessivo em D10** | Anexo F p. 163 tem rubrica, mas não resolve quais postos exigem substituição nem quantos substitutos cotar. |
| Aviso prévio em renovações | **Parcial em H28** | Reconheceu depósito integral inicial, sem enfrentar claramente o tratamento nas prorrogações. |
| Plano de saúde de 40% | **Coberto em H22** | A rubrica existe, mas base de cálculo, adesão e instrumento coletivo exigem conferência. |
| Tabelas de telefonista, eletricista e adicionais | **Coberto em H06/H23** | Jornadas/CBO conflitantes foram localizados; a tese de adicional para cada função depende de prova. |
| Título “cooperativas” com texto de consórcios | **Ausente como erro específico** | Edital p. 15, item 3.3.20.1; erro de revisão, sem efeito material demonstrado isoladamente. |
| Planilha separada de encargos sociais | **Parcial em H13** | Anexo F pp. 161–162 traz percentuais, mas não foi localizada planilha separada à qual edital/TR remetem; risco 3% está explicitado. |
| Preço mensal versus anual | **Coberto em H01** | Além da capa p. 3, a saída achou referências a item/lance unitário contra TR p. 80 e Anexo F p. 165. |

São três questões cobertas diretamente, três parciais e duas ausentes. Essa contagem avalia temas, não a procedência de cada quesito.

## Achados novos que sobreviveram à auditoria

A saída identificou inconsistências importantes não desenvolvidas na peça sênior:

1. **H02 — IMR e glosas:** o corpo do edital/TR e a minuta preveem redução de 5%/10%, enquanto o Anexo B contém faixas de 5%/10%/20%/40% para a mesma avaliação (pp. 49, 110, 141 e 189). É impugnação preliminar rastreável.
2. **H03 — Multas:** mora e inexecução total recebem percentuais/bases diferentes no edital, em outra seção do próprio edital e em duas cláusulas da minuta (pp. 60, 64, 200 e 211). É impugnação preliminar rastreável.
3. **H04 — Repactuação/reajuste:** edital, TR e minuta divergem quanto ao marco e ao índice; a cláusula XV usa orçamento de 28/05/2025 e IPCA, enquanto outros itens usam repactuação e um índice escrito incorretamente como “Índice Nacional de Preços ao Consumidor Amplo (INPC)” (pp. 52–53, 113–114, 192–193 e 212–213). É impugnação preliminar rastreável; os marcos legais ainda exigem conferência.
4. **H05 — Absorção obrigatória de empregados da contratada anterior:** a exigência literal consta do edital, TR e minuta (pp. 38, 101 e 186). A possível ingerência no recrutamento justifica impugnação preliminar, sujeita a CCT e fundamento específico. Não se demonstrou sucessão trabalhista automática.
5. **H15 — Vedação geral a instituições sem fins lucrativos:** o item 1.10.4 (pp. 8 e 82) exclui a categoria inteira por remissão a acórdão. A restrição demanda nexo com objeto e estatuto; é hipótese preliminar real, sem afirmar aptidão de toda entidade.

H16 também localizou lote único + vedação de consórcios/subcontratação e o próprio edital p. 23 dizendo que o objeto é divisível e precisa de parcelamento. O modelo o tratou apenas como risco; a motivação do ETP e o efeito no mercado ainda precisam ser verificados. H09 (prazos de mobilização/tecnologia) e H11 (541 profissionais versus demanda sem mínimo) são esclarecimentos materiais adicionais.

## Erros de classificação e falsos positivos evitados

Entre as nove linhas rotuladas **impugnação preliminar** na saída cega, a auditoria inicial mantém H01–H05 e H15 nessa classe e **rebaixa H12, H13 e H14** a esclarecimento/risco, salvo prova adicional. H12 interpretou “vínculo de qualquer outra natureza” como podendo alcançar qualquer relação comercial, embora o contexto seja funcional; H13 desconsiderou ressalva para FAP e adaptação da planilha; H14 depende de demonstrar uma carga fiscal efetiva integral ou alternativa para empresa sem doze meses de histórico. Em sentido inverso, H06 e H08 foram classificados de forma conservadora demais: suas contradições afetam custo e participação e merecem correção formal. H10 pode subir após confirmação de que nenhum documento publicado delimita os consumos.

A saída evitou falsos positivos importantes: **Gmail** como ilegalidade automática (D12); suposta exigência de atestado único/hospitalar (D03); insalubridade para todos os postos (D09); orçamento sigiloso como vício automático (D01); inexequibilidade automática abaixo de 50% (D07). O antigo texto FMS sugerira impugnar Gmail, cooperativas e PIS/COFINS com apoio insuficiente; a nova saída contém contrapontos e, para cooperativas, rejeita a ilegalidade automática. Ainda assim, H14 manteve a tese tributária forte demais sem caso concreto.

O formato foi obedecido em grande parte: 31 achados e 15 descartes com localizador, confronto, efeito, contraponto e pendência. A quantidade dificulta priorização prática. A ausência da memória de lotação referida no TR p. 89 foi registrada como lacuna de cobertura (D02), corretamente sem afirmar omissão na publicação; dada sua materialidade, deve aparecer também entre as primeiras verificações do pacote público.

## Próxima iteração recomendada da skill

1. Priorizar contradições **entre regras obrigatórias** que mudam participação, jornada, preço, medição, sanção ou reajuste; classificá-las como impugnação preliminar quando a correção formal for indispensável, mesmo que pareçam resíduos de modelo.
2. Para encargos e tributos, exigir exemplo verificável da empresa/regime atingido ou hipótese objetiva que a própria regra impede. Sem isso, usar esclarecimento/risco e declarar a prova faltante.
3. Fazer uma checagem por função das atividades descritas versus adicionais e qualificações, sem presumir exposição por trabalhar em hospital. Isso teria recuperado a questão específica dos motoristas.
4. Dar aos documentos referidos e não presentes no pacote uma fila própria de **verificação da publicação**; não converter a lacuna em alegação de omissão, mas também não escondê-la nos descartes.
5. Apresentar primeiro 5–10 pontos decisivos, consolidar duplicatas e deixar achados secundários em anexo. Manter todos os candidatos rastreáveis para revisão.

Este teste demonstra melhora de cobertura e contenção diante do PDF integral, mas **não mede precisão jurídica geral**. As correções acima dependem de nova avaliação cega antes de alterar a skill instalada.

## Fontes externas usadas somente na auditoria posterior

- [Lei nº 14.133/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm), em especial arts. 5º, 9º, 15, 18, 25, 55 §1º, 67, 92, 135 e 164.
- [Lei Complementar nº 123/2006](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm), art. 48, III.
- [Manual do TCU sobre habilitação técnica](https://licitacoesecontratos.tcu.gov.br/5-5-2-habilitacao-tecnica/) e [impugnação/esclarecimento](https://licitacoesecontratos.tcu.gov.br/5-1-1-impugnacao-e-pedidos-de-esclarecimento/).
- [NR-15, Anexo 14, Ministério do Trabalho e Emprego](https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/arquivos/normas-regulamentadoras/nr-15-anexo-14.pdf/view).
- [Orientação do MGI sobre PIS/COFINS em serviços com dedicação exclusiva](https://www.gov.br/compras/pt-br/agente-publico/orientacoes-e-procedimentos/19-orientacoes-sobre-pis-e-cofins-em-contratacoes-de-prestacao-de-servicos-com-dedicacao-exclusiva-de-mao-de-obra).
