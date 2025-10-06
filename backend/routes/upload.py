from fastapi import APIRouter, UploadFile, File
from typing import List
import shutil
import os

router = APIRouter()
os.makedirs("temp", exist_ok=True)

@router.post("/upload-multiplos/")
async def upload_multiplos(files: List[UploadFile] = File(...)):
    resultados = []
    for file in files:
        file_path = f"temp/{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        resultados.append({"filename": file.filename, "saved_to": file_path})
    return resultados
