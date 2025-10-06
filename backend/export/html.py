def export_to_html(dados_lista: list, output_path: str):
    html = "<html><head><meta charset='utf-8'><title>OCR Cartório</title></head><body>"
    html += "<h1>Dados Extraídos</h1><table border='1' cellpadding='5'>"
    html += "<tr><th>Arquivo</th><th>Nome</th><th>Qualidade Nome</th><th>CPF</th><th>Qualidade CPF</th><th>Situação Jurídica</th><th>Aberturas</th><th>Registros</th><th>Averbações</th></tr>"

    for item in dados_lista:
        for i in range(len(item["nomes"])):
            html += "<tr>"
            html += f"<td>{item.get('arquivo','')}</td>"
            html += f"<td>{item['nomes'][i] if i < len(item['nomes']) else ''}</td>"
            html += f"<td>{item['qualidade_nomes'][i] if i < len(item['qualidade_nomes']) else ''}</td>"
            html += f"<td>{item['cpfs'][i] if i < len(item['cpfs']) else ''}</td>"
            html += f"<td>{item['qualidade_cpfs'][i] if i < len(item['qualidade_cpfs']) else ''}</td>"
            html += f"<td>{item['situacoes'][i] if i < len(item['situacoes']) else ''}</td>"
            html += f"<td>{', '.join(item['aberturas'])}</td>"
            html += f"<td>{', '.join(item['registros'])}</td>"
            html += f"<td>{', '.join(item['averbacoes'])}</td>"
            html += "</tr>"

    html += "</table></body></html>"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)