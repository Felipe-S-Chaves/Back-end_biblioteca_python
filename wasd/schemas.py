from pydantic import BaseModel
from typing import Optional, List

class CarroCreate(BaseModel):
    modelo: str
    placa: str

class CarroUpdade(BaseModel):
    modelo: Optional[str] = None
    placa: Optional[str] = None

class CarroResponse(BaseModel):
    id: int
    modelo: str
    placa: str


    class Config:
        from_attributes = True


class DonoCreate(BaseModel):
    nome:str
    cpf:str

class DonoUpdade(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None

class DonoResponse(BaseModel):
    id: int
    nome: str
    cpf: str

    class Config:
        from_attributes = True


class DonoComCarrosResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    carros: List[CarroResponse] = []

    class Config:
        from_attributes = True



class CarroComDonoResponse(BaseModel):
    id: int
    modelo: str
    placa: str

    dono: Optional[DonoResponse] = None

    class Config:
        from_attributes = True

class CursoCreate(BaseModel):
    nome: str



class CursoResponse(BaseModel):
    id: int
    nome: str


    class Config:
        from_attributes = True

class AlunoCreate(BaseModel):
    nome: str


class AlunoResponse(BaseModel):
    id: int
    nome: str
    cursos: List[CursoResponse] = []

    class Config:
        from_attributes=True            