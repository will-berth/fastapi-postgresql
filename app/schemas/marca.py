from typing import Optional
from pydantic import BaseModel

class Marca(BaseModel):
    id: Optional[int]
    nombre: str

    class Config:
        orm_mode: True

class MarcaCreate(Marca):
    pass