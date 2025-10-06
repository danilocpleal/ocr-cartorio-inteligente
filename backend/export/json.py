import json

def export_to_json(dados_lista: list, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dados_lista, f, ensure_ascii=False, indent=2)