import os
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
from parser.atos_parser import parse_text

# 👇 Caminho do Tesseract no Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_texto_tesseract(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return ""

    ext = caminho_arquivo.lower().split('.')[-1]
    texto = ""

    try:
        if ext in ['jpg', 'jpeg', 'png', 'tiff']:
            imagem = Image.open(caminho_arquivo)
            texto = pytesseract.image_to_string(imagem, lang='por')
        elif ext == 'pdf':
            doc = fitz.open(caminho_arquivo)
            for pagina in doc:
                imagem = pagina.get_pixmap()
                img = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
                texto += pytesseract.image_to_string(img, lang='por')
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")

    return texto

def processar_com_tesseract(lista_arquivos):
    resultados = []
    for arquivo in lista_arquivos:
        texto = extrair_texto_tesseract(arquivo)
        dados = parse_text(texto)
        dados["arquivo"] = arquivo
        resultados.append(dados)
    return resultados