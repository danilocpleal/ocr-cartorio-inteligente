"""Serviços responsáveis por orquestrar o processamento dos arquivos."""
from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Sequence

from fastapi import UploadFile

from config import EXPORT_DIR, TEMP_DIR
from engines.google_engine import processar_com_google
from engines.nextcode_engine import processar_com_nextcode
from engines.tesseract_engine import processar_com_tesseract
from export.excel import export_to_excel
from models import DocumentoExtraido, ProcessamentoResponse, ProcessamentoResumo
from parser.atos_parser import parse_text
from utils.file_loader import contar_arquivos, listar_arquivos
from utils.filesystem import generate_safe_filename

# Mapear o nome do motor para a função correspondente facilita manutenção e testes.
ENGINE_PIPELINES = {
    "Tesseract + IA Local": processar_com_tesseract,
    "Google Document AI": processar_com_google,
    "Nextcode OCR": processar_com_nextcode,
}


def selecionar_motor_por_quantidade(total_arquivos: int) -> str:
    """Retorna o motor recomendado de acordo com a quantidade de arquivos."""

    if total_arquivos < 10_000:
        return "Tesseract + IA Local"
    if total_arquivos <= 100_000:
        return "Google Document AI"
    return "Nextcode OCR"


def processar_caminho(diretorio: str) -> ProcessamentoResponse:
    """Processa todos os arquivos de um diretório informado."""

    total_arquivos = contar_arquivos(diretorio)
    lista = listar_arquivos(diretorio)
    motor = selecionar_motor_por_quantidade(total_arquivos)

    dados_processados = _executar_motor(motor, lista)
    resumo = _gerar_resumo(motor, total_arquivos, dados_processados)

    return ProcessamentoResponse(resumo=resumo, dados_extraidos=dados_processados)


async def processar_uploads(files: Iterable[UploadFile]) -> ProcessamentoResponse:
    """Salva os uploads recebidos, processa e retorna os dados extraídos."""

    caminhos_salvos: List[Path] = []
    for upload in files:
        # Salvamos cada arquivo com um nome seguro e único para evitar colisões.
        nome_seguro = generate_safe_filename(upload.filename)
        destino = TEMP_DIR / f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}_{nome_seguro}"
        with destino.open("wb") as buffer:
            shutil.copyfileobj(upload.file, buffer)
        caminhos_salvos.append(destino)

    motor = selecionar_motor_por_quantidade(len(caminhos_salvos))
    dados_processados = _executar_motor(motor, caminhos_salvos)
    resumo = _gerar_resumo(motor, len(caminhos_salvos), dados_processados)

    return ProcessamentoResponse(resumo=resumo, dados_extraidos=dados_processados)


def _executar_motor(motor: str, arquivos: Sequence[Path | str]) -> List[DocumentoExtraido]:
    """Chama o motor correto para processar a lista de arquivos."""

    pipeline = ENGINE_PIPELINES.get(motor)
    if not pipeline:
        raise ValueError(f"Motor de OCR desconhecido: {motor}")

    resultados_brutos = pipeline(arquivos)
    # Garantimos que cada item seja convertido para ``DocumentoExtraido``.
    documentos = []
    for item in resultados_brutos:
        if isinstance(item, DocumentoExtraido):
            documentos.append(item)
            continue

        # Para manter compatibilidade com motores que ainda retornam dicionários.
        documentos.append(DocumentoExtraido(**item))
    return documentos


def _gerar_resumo(
    motor: str, total_arquivos: int, dados: Sequence[DocumentoExtraido]
) -> ProcessamentoResumo:
    """Cria um resumo da execução e dispara as exportações."""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    arquivo_exportado = EXPORT_DIR / f"resultado_{timestamp}.xlsx"
    export_to_excel(dados, arquivo_exportado)

    return ProcessamentoResumo(
        motor_usado=motor,
        quantidade_arquivos=total_arquivos,
        arquivo_exportado=str(arquivo_exportado),
    )


def processar_texto_bruto(texto: str, origem: str) -> DocumentoExtraido:
    """Permite processar um texto já extraído, útil para testes unitários."""

    dados = parse_text(texto)
    dados["arquivo"] = origem
    return DocumentoExtraido(**dados)
