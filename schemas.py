from pydantic import BaseModel
from typing import Optional, List

# Autores
class AutoresCreate(BaseModel):
    nome: str


class AutoresUpdate(BaseModel):
    nome: Optional[str] = None


class AutoresResponse(BaseModel):
    id: int
    nome: str 


    class Config:
        from_attributes = True



# Editoras
class EditorasCreate(BaseModel):
    nome: str


class EditorasUpdate(BaseModel):
    nome: Optional[str] = None


class EditorasResponse(BaseModel):
    id: int
    nome: str 

    class Config:
        from_attributes = True


# Usuarios
class UsuariosCreate(BaseModel):
    nome: str
    email: str
    senha: str


class UsuariosUpdade(BaseModel):
    senha: Optional[str] = None


class UsuariosResponse(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

    class Config:
        from_attributes = True



# Admin
class AdminCreate(BaseModel):
    nome: str
    email: str
    senha: str



class AdminUpdade(BaseModel):
    senha: Optional[str] = None



class AdminResponse(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

    class Config:
        from_attributes = True




# Livros
class LivrosCreate(BaseModel):
    titulo: str
    editora_id: int
    author_id: int


class LivrosUpdade(BaseModel):
    titulo: Optional[str] = None
    author_id: Optional[int] = None
    editora_id: Optional[int] = None


class LivrosResponse(BaseModel):
    id: int
    titulo: str
    author_id: int
    editora_id: int


    class Config:
        from_attributes = True



# Favoritos
class FavoritosCreate(BaseModel):
    livro_id: int
    usuario_id: int


class FavoritosUpdade(BaseModel):
    livro_id: Optional[int] = None
    usuario_id: Optional[int] = None


class FavoritosResponse(BaseModel):
    id: int
    livro_id: int
    usuario_id: int

    class Config:
        from_attributes = True



# Emprestimos
class EmprestimosCreate(BaseModel):
    livro_id: int
    usuario_id: int
    data_retirada: str
    data_devolucao: str


class EmprestimosUpdade(BaseModel):
    livro_id: int
    usuario_id: int
    data_retirada: str
    data_devolucao: str


class EmprestimosResponse(BaseModel):
    id: int
    livro_id: int
    usuario_id: int
    data_retirada: str
    data_devolucao: str

    class Config:
        from_attributes = True
