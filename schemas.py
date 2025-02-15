from pydantic import BaseModel
from typing import List, Optional

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int
    obrigacoes: List["ObrigacaoAcessoriaResponse"] = []

    class Config:
        from_attributes = True

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str  
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    empresa_id: int

class ObrigacaoAcessoriaResponse(ObrigacaoAcessoriaBase):
    id: int

    class Config:
        from_attributes = True
