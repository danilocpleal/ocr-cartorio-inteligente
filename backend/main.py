"""Ponto de entrada da aplicação FastAPI.

Este módulo inicializa a instância do FastAPI, configura a pasta de
arquivos estáticos do frontend e registra as rotas da API. A ideia é que
qualquer configuração global (middleware, CORS, etc.) fique centralizada
neste arquivo para facilitar a manutenção.
"""
from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from routes.processar import router as processar_router
from routes.upload import router as upload_router

# Diretório raiz do projeto. Usamos Path para ganhar portabilidade entre SOs.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# Pasta do frontend (onde ficam index.html e assets construídos pelo Vite)
FRONTEND_PATH = PROJECT_ROOT / 'frontend'
FRONTEND_DIST_PATH = FRONTEND_PATH / 'dist'
# Caminho do arquivo principal do frontend (prefere o build gerado).
INDEX_CANDIDATES = [FRONTEND_DIST_PATH / 'index.html', FRONTEND_PATH / 'index.html']

app = FastAPI(
    title="OCR Cartório Inteligente",
    description=(
        "API responsável por receber arquivos de cartório, processá-los "
        "com diferentes motores de OCR e disponibilizar os dados "
        "estruturados para exportação."
    ),
    version="1.0.0",
)

# Permite que o frontend (executando geralmente em http://localhost:5173)
# faça chamadas para a API sem esbarrar em bloqueios de CORS.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Faz o mount da pasta estática (prioriza a pasta dist caso exista).
static_dir = FRONTEND_DIST_PATH if FRONTEND_DIST_PATH.exists() else FRONTEND_PATH
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", response_class=HTMLResponse)
def serve_index() -> HTMLResponse:
    """Retorna o conteúdo do ``index.html`` do frontend.

    Caso o arquivo não exista (por exemplo em ambiente de desenvolvimento
    onde o Vite esteja servindo os arquivos), retornamos uma mensagem
    simples para não quebrar o carregamento da API.
    """

    for candidate in INDEX_CANDIDATES:
        if candidate.exists():
            return HTMLResponse(candidate.read_text(encoding="utf-8"))
    return HTMLResponse("Frontend não encontrado. Execute o build do Vite.")


# Rotas da API separadas por domínio de responsabilidade.
app.include_router(upload_router)
app.include_router(processar_router)
