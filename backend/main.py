import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from routes.upload import router as upload_router
from routes.processar import router as processar_router

app = FastAPI()

# Caminho absoluto para a pasta frontend
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")

# Serve os arquivos estáticos (CSS, JS, imagens) em /static
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Serve o index.html na raiz "/"
@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open(os.path.join(frontend_path, "index.html")) as f:
        return f.read()

# Rotas da API
app.include_router(upload_router)
app.include_router(processar_router)