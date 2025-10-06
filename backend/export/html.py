"""Geração de relatórios HTML simples."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

from models import DocumentoExtraido


def export_to_html(dados_lista: Iterable[DocumentoExtraido], output_path: str | Path) -> Path:
    linhas = [
        "<html><head><meta charset='utf-8'><title>OCR Cartório</title>",
        "<style>body{font-family:Inter,Arial,sans-serif;background:#f8fafc;padding:24px;}table{border-collapse:collapse;width:100%;background:white;border-radius:8px;overflow:hidden;box-shadow:0 10px 30px rgba(15,23,42,0.08);}th,td{padding:12px;border-bottom:1px solid #e2e8f0;text-align:left;}th{background:#0f172a;color:#f8fafc;text-transform:uppercase;font-size:12px;letter-spacing:.08em;}tr:hover{background:#f1f5f9;}</style></head><body>",
        "<h1>Dados Extraídos</h1><table>",
        "<tr><th>Arquivo</th><th>Nome</th><th>Qualidade Nome</th><th>CPF</th><th>Qualidade CPF</th><th>Situação Jurídica</th><th>Aberturas</th><th>Registros</th><th>Averbações</th></tr>",
    ]

    for item in dados_lista:
        dados = item.model_dump() if isinstance(item, DocumentoExtraido) else dict(item)
        nomes = dados.get("nomes", []) or [""]
        max_len = max(len(nomes), len(dados.get("cpfs", [])), 1)

        for indice in range(max_len):
            linhas.append("<tr>")
            linhas.append(f"<td>{dados.get('arquivo','')}</td>")
            linhas.append(f"<td>{_get_safely(dados.get('nomes', []), indice)}</td>")
            linhas.append(
                f"<td>{_get_safely(dados.get('qualidade_nomes', []), indice)}</td>"
            )
            linhas.append(f"<td>{_get_safely(dados.get('cpfs', []), indice)}</td>")
            linhas.append(
                f"<td>{_get_safely(dados.get('qualidade_cpfs', []), indice)}</td>"
            )
            linhas.append(
                f"<td>{_get_safely(dados.get('situacoes', []), indice)}</td>"
            )
            linhas.append(f"<td>{', '.join(dados.get('aberturas', []))}</td>")
            linhas.append(f"<td>{', '.join(dados.get('registros', []))}</td>")
            linhas.append(f"<td>{', '.join(dados.get('averbacoes', []))}</td>")
            linhas.append("</tr>")

    linhas.append("</table></body></html>")

    output_path = Path(output_path)
    output_path.write_text("\n".join(linhas), encoding="utf-8")
    return output_path


def _get_safely(items: list[str], index: int) -> str:
    try:
        return items[index]
    except IndexError:
        return ""
