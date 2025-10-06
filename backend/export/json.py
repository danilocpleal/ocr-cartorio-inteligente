"""Exportação dos resultados em JSON."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from models import DocumentoExtraido


def export_to_json(dados_lista: Iterable[DocumentoExtraido], output_path: str | Path) -> Path:
    serializavel = []
    for item in dados_lista:
        if isinstance(item, DocumentoExtraido):
            serializavel.append(item.model_dump())
        else:
            serializavel.append(dict(item))

    output_path = Path(output_path)
    output_path.write_text(
        json.dumps(serializavel, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return output_path
