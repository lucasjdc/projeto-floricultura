from pydantic import BaseModel, Field, validator
from datetime import datetime

class Produto(BaseModel):
    nome: str = Field(..., min_length=1)
    quantidade: int = Field(..., ge=1)
    preco: float = Field(..., ge=0)
    data: str
    descricao: str | None = None

    @validator("data")
    def validar_data(cls, v):
        try:
            datetime.strptime(v, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data deve estar no formato dd/mm/aaaa")
        return v