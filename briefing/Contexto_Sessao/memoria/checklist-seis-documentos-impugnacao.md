---
name: checklist-seis-documentos-impugnacao
description: Os 6 documentos que o usuário exige por licitação a impugnar e onde ficam as pastas dos editais (files/IMPUGNACOES + Editais)
metadata:
  node_type: memory
  type: project
  originSessionId: 75992c45-fa9d-4fbc-a62e-2cef04caa42a
  modified: 2026-10-14T18:26:07.091Z
---

Para cada impugnação a Servfaz quer ter em mãos 6 documentos: Edital, Termo de Referência, Estudo Técnico Preliminar (ETP), Mapa de Cotações, Planilha de Custos e Minuta Contratual. As pastas ficam em `files/IMPUGNACOES + Editais/` (uma por órgão, com o .docx da impugnação). Em 2026-10-14 eram 4 licitações: CBM-DF PE 90099/2025, FMS Teresina PE 111/2026, Prefeitura de São Luís SRP 90.150/2025 e SEMED São Luís SRP 90.099/2025 (as duas de São Luís compartilham a UASG 980921).

**Why:** o usuário monta a análise de impugnação (skill `impugnacao-editais-tcu`) e precisa saber o que falta antes de redigir.

**How to apply:** ao checar cobertura, abrir o conteúdo dos PDFs (anexos costumam vir embutidos no PDF do edital) e separar "planilha modelo em branco" de "planilha estimada preenchida". Resultado de 2026-10-14: nenhuma licitação tinha os 6; Mapa de Cotações não estava em nenhuma. Ver [[pncp-api-e-base-legal-sigilo]] para o que é público.
