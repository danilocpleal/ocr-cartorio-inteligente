"""Motor fictício para integração futura com o Nextcode OCR."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

from models import DocumentoExtraido
from parser.atos_parser import parse_text


def processar_com_nextcode(lista_arquivos: Iterable[Path | str]) -> List[DocumentoExtraido]:
    """Processa arquivos simulando o uso do Nextcode OCR."""

    resultados = []
    for arquivo in lista_arquivos:
        dados = parse_text("")
        dados["arquivo"] = str(arquivo)
        dados["situacoes"].append("Processamento pendente no Nextcode")
        resultados.append(DocumentoExtraido(**dados))
    return resultados
