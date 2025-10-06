"""Implementação local utilizando Tesseract OCR."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, List

import fitz  # PyMuPDF
import pytesseract
from PIL import Image

from models import DocumentoExtraido
from parser.atos_parser import parse_text

# Permite que o caminho do executável do Tesseract seja configurado via variável de ambiente.
TESSERACT_PATH = os.getenv("TESSERACT_CMD")
if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def extrair_texto_tesseract(caminho_arquivo: Path | str) -> str:
    """Extrai texto de imagens ou PDFs usando Tesseract."""

    caminho = Path(caminho_arquivo)
    if not caminho.exists():
        return ""

    texto = ""
    ext = caminho.suffix.lower()

    try:
        if ext in {".jpg", ".jpeg", ".png", ".tiff"}:
            imagem = Image.open(caminho)
            texto = pytesseract.image_to_string(imagem, lang="por")
        elif ext == ".pdf":
            doc = fitz.open(caminho)
            for pagina in doc:
                imagem = pagina.get_pixmap()
                img = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
                texto += pytesseract.image_to_string(img, lang="por")
    except Exception as exc:  # pragma: no cover - dependente do SO
        print(f"Erro ao processar {caminho}: {exc}")

    return texto


def processar_com_tesseract(lista_arquivos: Iterable[Path | str]) -> List[DocumentoExtraido]:
    """Processa uma sequência de arquivos usando Tesseract."""

    resultados = []
    for arquivo in lista_arquivos:
        texto = extrair_texto_tesseract(arquivo)
        dados = parse_text(texto)
        dados["arquivo"] = str(arquivo)
        resultados.append(DocumentoExtraido(**dados))
    return resultados
