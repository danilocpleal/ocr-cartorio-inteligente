import os

def contar_arquivos(diretorio: str) -> int:
    """Conta quantos arquivos existem no diretório"""
    return len([
        f for f in os.listdir(diretorio)
        if os.path.isfile(os.path.join(diretorio, f))
           and f.lower().endswith(('.pdf', '.jpg', '.jpeg', '.png', '.tiff'))
    ])

def listar_arquivos(diretorio: str) -> list:
    """Retorna a lista completa de caminhos dos arquivos válidos"""
    return [
        os.path.join(diretorio, f)
        for f in os.listdir(diretorio)
        if os.path.isfile(os.path.join(diretorio, f))
           and f.lower().endswith(('.pdf', '.jpg', '.jpeg', '.png', '.tiff'))
    ]