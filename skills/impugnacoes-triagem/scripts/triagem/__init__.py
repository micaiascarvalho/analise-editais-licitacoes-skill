"""Pacote da máquina de estados da triagem; o ponto de entrada é scripts/estado.py.

Mapa regra → módulo:
  portões e fase derivada (fila, minuta em revisão, próxima ação, alertas, status) → fases.py
  evidência e aprovação (genérica, lote, negação, condição, uma minuta por vez) → evidencia.py
  gravação e trava (leitura de entrada, gravação atômica, .estado.lock, forma do estado.json) → persistencia.py
  invariantes do validar → invariantes.py
  registro.md → registro.py
  arquivos das minutas (sha256, histórico, restauração) → arquivos.py
  comandos: slug, iniciar, status, documentos, prosseguir, prazo, itens, decidir, reabrir → comandos.py;
  minuta → minutas.py; peca → peca.py
  base (recusa, relógio, texto, listas, hash, datas, IDs, slug) → comum.py
"""
