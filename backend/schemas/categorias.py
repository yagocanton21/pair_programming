from pydantic import BaseModel

# Esquema para criar uma categoria
class CategoriaCreate(BaseModel):
    nome: str

# Esquema para retornar uma categoria
class CategoriaResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True
        