"""Funções utilitárias para listar e contar arquivos válidos."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, List

# Extensões suportadas pelo pipeline de OCR.
EXTENSOES_VALIDAS = (".pdf", ".jpg", ".jpeg", ".png", ".tiff")


def _validar_diretorio(diretorio: str | os.PathLike[str]) -> Path:
    caminho = Path(diretorio)
    if not caminho.exists():
        raise FileNotFoundError(f"Diretório não encontrado: {diretorio}")
    if not caminho.is_dir():
        raise NotADirectoryError(f"O caminho informado não é um diretório: {diretorio}")
    return caminho


def contar_arquivos(diretorio: str | os.PathLike[str]) -> int:
    """Conta quantos arquivos elegíveis existem no diretório."""

    caminho = _validar_diretorio(diretorio)
    return sum(1 for f in caminho.iterdir() if _arquivo_valido(f))


def listar_arquivos(diretorio: str | os.PathLike[str]) -> List[Path]:
    """Retorna a lista completa de caminhos dos arquivos válidos."""

    caminho = _validar_diretorio(diretorio)
    return [f for f in caminho.iterdir() if _arquivo_valido(f)]


def _arquivo_valido(arquivo: Path) -> bool:
    return arquivo.is_file() and arquivo.suffix.lower() in EXTENSOES_VALIDAS
