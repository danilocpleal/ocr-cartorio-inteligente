"""Configurações reutilizadas em todo o backend.

Este arquivo concentra caminhos de diretórios, constantes e pequenas
funções auxiliares para manter o restante do código mais limpo.
"""
from __future__ import annotations

from pathlib import Path

# Diretório raiz do projeto
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# Pasta temporária onde os uploads ficarão armazenados.
TEMP_DIR = PROJECT_ROOT / "temp_uploads"
# Pasta de exportação dos relatórios.
EXPORT_DIR = PROJECT_ROOT / "exportados"

# Garante que as pastas existam durante a inicialização do backend.
TEMP_DIR.mkdir(parents=True, exist_ok=True)
EXPORT_DIR.mkdir(parents=True, exist_ok=True)
