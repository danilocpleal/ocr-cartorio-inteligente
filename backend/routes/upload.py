"""Rotas responsáveis por upload de arquivos."""
from __future__ import annotations

from typing import List

from fastapi import APIRouter, File, HTTPException, UploadFile

from models import ProcessamentoResponse
from services.ocr_service import processar_uploads

router = APIRouter(prefix="/upload", tags=["Uploads"])


@router.post("/multiplos", response_model=ProcessamentoResponse)
async def upload_multiplos(files: List[UploadFile] = File(...)) -> ProcessamentoResponse:
    """Recebe múltiplos arquivos, processa e retorna o resultado."""

    if not files:
        raise HTTPException(status_code=400, detail="Nenhum arquivo recebido")

    return await processar_uploads(files)
