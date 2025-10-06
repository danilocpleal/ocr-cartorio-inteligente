from fastapi import APIRouter, Query
from utils.file_loader import contar_arquivos, listar_arquivos
from engines.tesseract_engine import processar_com_tesseract
from engines.google_engine import processar_com_google
from engines.nextcode_engine import processar_com_nextcode
from export.excel import export_to_excel

router = APIRouter()

@router.get("/processar/")
def processar_diretorio(caminho: str = Query(..., description="Caminho do diretório com arquivos")):
    qtd = contar_arquivos(caminho)
    arquivos = listar_arquivos(caminho)

    if qtd < 10000:
        motor = "Tesseract + IA Local"
        dados = processar_com_tesseract(arquivos)
    elif qtd <= 100000:
        motor = "Google Document AI"
        dados = processar_com_google(arquivos)
    else:
        motor = "Nextcode OCR"
        dados = processar_com_nextcode(arquivos)

    export_to_excel(dados, "resultado.xlsx")

    return {
        "motor_usado": motor,
        "quantidade_arquivos": qtd,
        "dados_extraidos": dados
    }