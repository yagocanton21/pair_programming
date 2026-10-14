from pydantic import BaseModel
from typing import Optional

# Esquema para criar uma movimentação
class MovimentacaoCreate(BaseModel):
    id_produto: int          
    quantidade: float 
    tipo: str       

# Esquema para retornar uma movimentação
class MovimentacaoResponse(BaseModel):
    id: int
    id_produto: Optional[int] = None
    tipo: str
    quantidade: float        
    data: str

    class Config:
        from_attributes = True
