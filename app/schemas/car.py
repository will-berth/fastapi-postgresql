from typing import List, Optional
from pydantic import BaseModel

class Auto(BaseModel):
    id: Optional[int]
    puertas: int
    color: str
    marca: Optional[int]

    class Config:
        orm_mode = True