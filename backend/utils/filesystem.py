"""Utilidades relacionadas a manipulação de arquivos e diretórios."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Iterable


def generate_safe_filename(filename: str) -> str:
    """Gera um nome de arquivo seguro, removendo caracteres especiais."""

    if not filename:
        raise ValueError("Nome de arquivo não pode ser vazio")

    # Normaliza para remover acentos e outros caracteres problemáticos.
    normalized = unicodedata.normalize("NFKD", filename)
    normalized = normalized.encode("ascii", "ignore").decode("ascii")

    # Substitui qualquer caractere que não seja alfanumérico, ponto ou hífen.
    sanitized = re.sub(r"[^A-Za-z0-9._-]", "_", normalized)
    return sanitized


def ensure_directory(path: Path) -> None:
    """Garante que um diretório exista."""

    path.mkdir(parents=True, exist_ok=True)


def delete_files(paths: Iterable[Path]) -> None:
    """Remove uma sequência de arquivos, ignorando erros."""

    for path in paths:
        try:
            path.unlink(missing_ok=True)
        except OSError:
            # Em produção poderíamos logar o erro, mas não queremos quebrar o fluxo.
            continue
