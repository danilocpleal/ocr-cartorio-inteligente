"""Exportação dos resultados em planilha Excel."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

import pandas as pd

from models import DocumentoExtraido


def export_to_excel(dados_lista: Iterable[DocumentoExtraido], output_path: str | Path | None = None) -> Path:
    """Exporta os dados para um arquivo Excel."""

    if not output_path:
        output_path = Path(f"resultado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
    else:
        output_path = Path(output_path)

    linhas = []
    for item in dados_lista:
        # Garante que estamos trabalhando com o modelo dataclass-like.
        if isinstance(item, DocumentoExtraido):
            dados = item.model_dump()
        else:
            dados = dict(item)

        nomes = dados.get("nomes", []) or [""]
        max_len = max(len(nomes), len(dados.get("cpfs", [])), 1)

        for indice in range(max_len):
            linhas.append(
                {
                    "Arquivo": dados.get("arquivo", ""),
                    "Nome": _get_safely(dados.get("nomes", []), indice),
                    "Qualidade Nome": _get_safely(dados.get("qualidade_nomes", []), indice),
                    "CPF": _get_safely(dados.get("cpfs", []), indice),
                    "Qualidade CPF": _get_safely(dados.get("qualidade_cpfs", []), indice),
                    "Situação Jurídica": _get_safely(dados.get("situacoes", []), indice),
                    "Aberturas": ", ".join(dados.get("aberturas", [])),
                    "Registros": ", ".join(dados.get("registros", [])),
                    "Averbações": ", ".join(dados.get("averbacoes", [])),
                }
            )

    df = pd.DataFrame(linhas)
    df.to_excel(output_path, index=False)
    return output_path


def _get_safely(items: list[str], index: int) -> str:
    try:
        return items[index]
    except IndexError:
        return ""
