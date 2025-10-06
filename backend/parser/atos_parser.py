"""Responsável por extrair informações estruturadas do texto OCR."""
from __future__ import annotations

import re
from typing import Dict, List

CPF_REGEX = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")
NOME_REGEX = re.compile(r"[A-Z][A-Z\s]+(?=\s+\|)")
SITUACAO_REGEX = re.compile(
    r"(Transmitente|Adquirente|Herdeiro|Falecido|Doador|Emitente|Cônjuge|Cadastro fiscal)",
    re.IGNORECASE,
)


def validar_cpf(cpf: str) -> str:
    """Valida um CPF de forma simplificada."""

    numeros = re.sub(r"\D", "", cpf)
    if len(numeros) != 11 or numeros == numeros[0] * 11:
        return "Inválido"
    return "Válido"


def avaliar_nome(nome: str) -> str:
    """Classifica se o nome parece completo (possui pelo menos nome e sobrenome)."""

    partes = nome.strip().split()
    return "Completo" if len(partes) >= 2 else "Incompleto"


def parse_text(text: str) -> Dict[str, List[str]]:
    """Realiza o parsing das informações relevantes do texto do cartório."""

    atos_abertura = re.findall(r"\bAB\.|\bAb\.", text)
    registros = re.findall(r"\bR\.?\d+\b", text)
    averbacoes = re.findall(r"\bAv\.?\d+\b", text)

    cpfs = CPF_REGEX.findall(text)
    nomes = [nome.strip() for nome in NOME_REGEX.findall(text)]
    situacoes = [match.title() for match in SITUACAO_REGEX.findall(text)]

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
        "situacoes": situacoes,
    }
