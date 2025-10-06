"""Rotas responsáveis pelo processamento dos arquivos."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from models import ProcessamentoResponse
from services.ocr_service import processar_caminho

router = APIRouter(prefix="/processar", tags=["Processamento"])


@router.get("/diretorio", response_model=ProcessamentoResponse)
def processar_diretorio(
    caminho: str = Query(..., description="Caminho do diretório com arquivos para OCR")
) -> ProcessamentoResponse:
    """Processa todos os arquivos encontrados no diretório informado."""

    try:
        return processar_caminho(caminho)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover - fallback genérico
        raise HTTPException(status_code=500, detail=str(exc)) from exc
