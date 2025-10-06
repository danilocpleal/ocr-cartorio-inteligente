"""Modelos Pydantic compartilhados pelas rotas."""
from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class DocumentoExtraido(BaseModel):
    """Estrutura com os dados de um único documento processado."""

    arquivo: str = Field(..., description="Caminho original do arquivo processado")
    nomes: List[str] = Field(default_factory=list, description="Lista de nomes encontrados")
    qualidade_nomes: List[str] = Field(
        default_factory=list, description="Classificação de completude para cada nome"
    )
    cpfs: List[str] = Field(default_factory=list, description="CPFs identificados no texto")
    qualidade_cpfs: List[str] = Field(
        default_factory=list, description="Validação dos CPFs encontrados"
    )
    situacoes: List[str] = Field(
        default_factory=list, description="Situações jurídicas associadas aos nomes"
    )
    aberturas: List[str] = Field(default_factory=list, description="Atos de abertura identificados")
    registros: List[str] = Field(default_factory=list, description="Registros encontrados")
    averbacoes: List[str] = Field(default_factory=list, description="Averbações presentes no texto")


class ProcessamentoResumo(BaseModel):
    """Dados agregados sobre a execução do OCR."""

    motor_usado: str
    quantidade_arquivos: int
    arquivo_exportado: Optional[str] = Field(
        None, description="Caminho para o arquivo de exportação gerado"
    )


class ProcessamentoResponse(BaseModel):
    """Resposta padrão retornada pelas rotas de processamento."""

    resumo: ProcessamentoResumo
    dados_extraidos: List[DocumentoExtraido]
