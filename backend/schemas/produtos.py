from pydantic import BaseModel
from typing import Optional

# Esquema para criar um produto
class ProdutoCreate(BaseModel):
    nome: str
    quantidade: float
    preco_unitario: float
    id_categoria: Optional[int] = None

# Esquema para retornar um produto
class ProdutoResponse(BaseModel):
    id: int
    nome: str
    quantidade: float
    preco_unitario: float
    id_categoria: int

    class Config:
        from_attributes = True