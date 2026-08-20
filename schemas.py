# schemas.py
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoResponse(ProdutoBase):
    id: int

class AlunoBase(BaseModel):
    nome: str
    matricula: int
    curso: str
    email: str

class AlunoCreate(AlunoBase):
    pass

class AlunoResponse(AlunoBase):
    id: int


class Config:
    from_attributes = True

