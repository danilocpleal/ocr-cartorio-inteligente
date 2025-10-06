import re

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return "Inválido"
    return "Válido"

def avaliar_nome(nome):
    partes = nome.strip().split()
    if len(partes) >= 2:
        return "Completo"
    return "Incompleto"

def parse_text(text: str):
    atos_abertura = re.findall(r'\bAB\.|\bAb\.', text)
    registros = re.findall(r'\bR\.?\d+\b', text)
    averbacoes = re.findall(r'\bAv\.?\d+\b', text)

    cpfs = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', text)
    nomes = re.findall(r'[A-Z][A-Z\s]+(?=\s+\|)', text)
    situacoes = re.findall(r'(Transmitente|Adquirente|Herdeiro|Falecido|Doador|Emitente|Cônjuge|Cadastro fiscal)', text)

    qualidade_cpfs = [validar_cpf(cpf) for cpf in cpfs]
    qualidade_nomes = [avaliar_nome(nome) for nome in nomes]

    return {
        "aberturas": atos_abertura,
        "registros": registros,
        "averbacoes": averbacoes,
        "nomes": nomes,
        "qualidade_nomes": qualidade_nomes,
        "cpfs": cpfs,
        "qualidade_cpfs": qualidade_cpfs,
        "situacoes": situacoes
    }