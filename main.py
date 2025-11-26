from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine, Base
from models import Admin , Autores , Editoras , Emprestimos , Favoritos , Livros , Usuarios
from schemas import AdminCreate, AdminResponse, AdminUpdade, AutoresCreate, AutoresResponse, EditorasCreate, EditorasResponse, EditorasUpdate, EmprestimosCreate , EmprestimosResponse, EmprestimosUpdade, FavoritosCreate, FavoritosResponse, FavoritosUpdade, LivrosCreate, LivrosResponse, LivrosUpdade, UsuariosCreate, UsuariosResponse, UsuariosUpdade

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return "No ar"






# Get
@app.get("/autores", response_model=List[AutoresResponse])
def listar_autores(db: Session = Depends(get_db)):
    author = db.query(Autores).all()

    return author


@app.get("/editoras", response_model=List[EditorasResponse])
def listar_editoras(db: Session = Depends(get_db)):
    editora = db.query(Autores).all()

    return editora


@app.get("/usuarios", response_model=List[UsuariosResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuario = db.query(Autores).all()

    return usuario



@app.get("/livros", response_model=List[LivrosResponse])
def listar_livros(db: Session = Depends(get_db)):
    livros = db.query(Autores).all()

    return livros



@app.get("/emprestimos", response_model=List[EmprestimosResponse])
def listar_emprestimos(db: Session = Depends(get_db)):
    emprestimos = db.query(Autores).all()

    return emprestimos



@app.get("/favoritos", response_model=List[FavoritosResponse])
def listar_autores(db: Session = Depends(get_db)):
    author = db.query(Autores).all()

    return author



@app.get("/admin", response_model=List[AdminResponse])
def listar_Admins(db: Session = Depends(get_db)):
    admin = db.query(Autores).all()

    return admin






# Posts


@app.post("/editoras", response_model = EditorasResponse)
def adicionar_Editora(editoras: EditorasCreate, db: Session = Depends(get_db)):
    nova_editora = Editoras(**editoras.model_dump())

    db.add(nova_editora)
    db.commit()
    db.refresh(nova_editora)

    return nova_editora


@app.post("/autores", response_model = AutoresResponse)
def adicionar_Editora(autores: AutoresCreate, db: Session = Depends(get_db)):
    novo_autor = Editoras(**autores.model_dump())

    db.add(novo_autor)
    db.commit()
    db.refresh(novo_autor)

    return novo_autor


@app.post("/livros", response_model = LivrosResponse)
def adicionar_livro(livro: LivrosCreate, db: Session = Depends(get_db)):
    novo_livro = Livros(**livro.model_dump())

    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)

    return novo_livro



@app.post("/emprestimos", response_model = EmprestimosResponse)
def adicionar_livro(emprestimos: EmprestimosCreate, db: Session = Depends(get_db)):
    novo_emprestimos = Emprestimos(**emprestimos.model_dump())

    db.add(novo_emprestimos)
    db.commit()
    db.refresh(novo_emprestimos)

    return novo_emprestimos



@app.post("/usuarios", response_model = UsuariosResponse)
def adicionar_livro(usuario: FavoritosCreate, db: Session = Depends(get_db)):
    novo_usuario = Livros(**usuario.model_dump())

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario



@app.post("/favoritos", response_model = FavoritosResponse)
def adicionar_livro(favorito: FavoritosCreate, db: Session = Depends(get_db)):
    novo_favorito = Favoritos(**favorito.model_dump())

    db.add(novo_favorito)
    db.commit()
    db.refresh(novo_favorito)

    return novo_favorito



@app.post("/admin", response_model = AdminResponse)
def criar_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    novo_admin = Admin(**admin.model_dump())

    db.add(novo_admin)
    db.commit()
    db.refresh(novo_admin)

    return novo_admin


