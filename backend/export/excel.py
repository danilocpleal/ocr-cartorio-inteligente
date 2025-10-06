from datetime import datetime

def export_to_excel(dados_lista: list, output_path: str = None):
    if not output_path:
        output_path = f"resultado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    linhas = []
    for item in dados_lista:
        nomes = item.get("nomes", [])
        for i in range(len(nomes)):
            linha = {
                "Arquivo": item.get("arquivo", ""),
                "Nome": nomes[i] if i < len(nomes) else "",
                "Qualidade Nome": item.get("qualidade_nomes", [""])[i] if i < len(item.get("qualidade_nomes", [])) else "",
                "CPF": item.get("cpfs", [""])[i] if i < len(item.get("cpfs", [])) else "",
                "Qualidade CPF": item.get("qualidade_cpfs", [""])[i] if i < len(item.get("qualidade_cpfs", [])) else "",
                "Situação Jurídica": item.get("situacoes", [""])[i] if i < len(item.get("situacoes", [])) else "",
                "Aberturas": ", ".join(item.get("aberturas", [])),
                "Registros": ", ".join(item.get("registros", [])),
                "Averbações": ", ".join(item.get("averbacoes", []))
            }
            linhas.append(linha)

    df = pd.DataFrame(linhas)
    df.to_excel(output_path, index=False)