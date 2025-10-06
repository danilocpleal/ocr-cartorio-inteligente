"""Motor fictício para integração futura com o Google Document AI."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

from models import DocumentoExtraido
from parser.atos_parser import parse_text


def processar_com_google(lista_arquivos: Iterable[Path | str]) -> List[DocumentoExtraido]:
    """Processa arquivos simulando o uso do Google Document AI."""

    resultados = []
    for arquivo in lista_arquivos:
        # Por enquanto apenas retornamos uma mensagem informativa mantendo a estrutura.
        dados = parse_text("")
        dados["arquivo"] = str(arquivo)
        dados["situacoes"].append("Processamento pendente no Google")
        resultados.append(DocumentoExtraido(**dados))
    return resultados
