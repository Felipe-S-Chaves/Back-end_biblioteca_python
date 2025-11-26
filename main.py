from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine, Base
from models import Admin , Autores , Editoras , Emprestimos , Favoritos , Livros , Usuarios
from schemas import AdminCreate, AdminResponse, AdminUpdade, AutoresCreate, AutoresResponse , AutoresUpdate, EditorasCreate, EditorasResponse, EditorasUpdate, EmprestimosCreate , EmprestimosResponse, EmprestimosUpdade, FavoritosCreate, FavoritosResponse, FavoritosUpdade, LivrosCreate, LivrosResponse, LivrosUpdade, UsuariosCreate, UsuariosResponse, UsuariosUpdade

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
    editora = db.query(Editoras).all()

    return editora


@app.get("/usuarios", response_model=List[UsuariosResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).all()

    return usuario



@app.get("/livros", response_model=List[LivrosResponse])
def listar_livros(db: Session = Depends(get_db)):
    livros = db.query(Livros).all()

    return livros



@app.get("/emprestimos", response_model=List[EmprestimosResponse])
def listar_emprestimos(db: Session = Depends(get_db)):
    emprestimos = db.query(Emprestimos).all()

    return emprestimos



@app.get("/favoritos", response_model=List[FavoritosResponse])
def listar_favoritos(db: Session = Depends(get_db)):
    favoritos = db.query(Favoritos).all()

    return favoritos



@app.get("/admin", response_model=List[AdminResponse])
def listar_Admins(db: Session = Depends(get_db)):
    admin = db.query(Admin).all()

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
def adicionar_autor(autores: AutoresCreate, db: Session = Depends(get_db)):
    novo_autor = Autores(**autores.model_dump())

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
def adicionar_emprestimo(emprestimos: EmprestimosCreate, db: Session = Depends(get_db)):
    novo_emprestimos = Emprestimos(**emprestimos.model_dump())

    db.add(novo_emprestimos)
    db.commit()
    db.refresh(novo_emprestimos)

    return novo_emprestimos



@app.post("/usuarios", response_model = UsuariosResponse)
def adicionar_usuarios(usuario: FavoritosCreate, db: Session = Depends(get_db)):
    novo_usuario = Usuarios(**usuario.model_dump())

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario



@app.post("/favoritos", response_model = FavoritosResponse)
def adicionar_favorito(favorito: FavoritosCreate, db: Session = Depends(get_db)):
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



# Puts


@app.put("/autores{autor_id}", response_model = AutoresResponse)
def editar_autor(autor_id: int, data: AutoresUpdate, db: Session = Depends(get_db)):
    autor_atualizado = db.query(Autores).filter(Autores.id == autor_id).first()
    
    if not autor_atualizado:
        raise HTTPException(status_code=404, detail="nao encontrado")
    
    dados_atualizados = data.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizados.items():
        setattr(autor_atualizado, campo, valor)


    db.commit()
    db.refresh(autor_atualizado)
    
    return autor_atualizado




@app.put("/livros{livro_id}", response_model = LivrosResponse)
def editar_livros(livro_id: int, data: LivrosUpdade, db: Session = Depends(get_db)):
    livro_atualizado = db.query(Livros).filter(Livros.id == livro_id).first()
    
    if not livro_atualizado:
        raise HTTPException(status_code=404, detail="nao encontrado")
    
    dados_atualizados = data.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizados.items():
        setattr(livro_atualizado, campo, valor)


    db.commit()
    db.refresh(livro_atualizado)
    
    return livro_atualizado




@app.put("/editoras{editora_id}", response_model = EditorasResponse)
def editar_editora(editora_id: int, data: EditorasUpdate, db: Session = Depends(get_db)):
    editora_atualizada = db.query(Editoras).filter(Editoras.id == editora_id).first()
    
    if not editora_atualizada:
        raise HTTPException(status_code=404, detail="nao encontrado")
    
    dados_atualizados = data.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizados.items():
        setattr(editora_atualizada, campo, valor)


    db.commit()
    db.refresh(editora_atualizada)
    
    return editora_atualizada





@app.put("/usuarios{usuario_id}", response_model = UsuariosResponse)
def editar_usuario(user_id: int, data: LivrosUpdade, db: Session = Depends(get_db)):
    user_atualizado = db.query(Usuarios).filter(Usuarios.id == user_id).first()
    
    if not user_atualizado:
        raise HTTPException(status_code=404, detail="nao encontrado")
    
    dados_atualizados = data.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizados.items():
        setattr(user_atualizado, campo, valor)


    db.commit()
    db.refresh(user_atualizado)
    
    return user_atualizado





@app.put("/admin{admin_id}", response_model = AdminResponse)
def editar_admin(admin_id: int, data: LivrosUpdade, db: Session = Depends(get_db)):
    admin_atualizado = db.query(Admin).filter(Admin.id == admin_id).first()
    
    if not admin_atualizado:
        raise HTTPException(status_code=404, detail="nao encontrado")
    
    dados_atualizados = data.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizados.items():
        setattr(admin_atualizado, campo, valor)


    db.commit()
    db.refresh(admin_atualizado)
    
    return admin_atualizado





@app.put("/emprestimos{emprestimo_id}", response_model = EmprestimosResponse)
def editar_emprestimo(emprestimo_id: int, data: LivrosUpdade, db: Session = Depends(get_db)):
    emprestimos_atualizado = db.query(Emprestimos).filter(Emprestimos.id == emprestimo_id).first()
    
    if not emprestimos_atualizado:
        raise HTTPException(status_code=404, detail="nao encontrado")
    
    dados_atualizados = data.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizados.items():
        setattr(emprestimos_atualizado, campo, valor)


    db.commit()
    db.refresh(emprestimos_atualizado)
    
    return emprestimos_atualizado






@app.put("/favoritos{favoritos_id}", response_model = FavoritosResponse)
def editar_favoritos(favoritos_id: int, data: LivrosUpdade, db: Session = Depends(get_db)):
    favoritos_atualizado = db.query(Favoritos).filter(Favoritos.id == favoritos_id).first()
    
    if not favoritos_atualizado:
        raise HTTPException(status_code=404, detail="nao encontrado")
    
    dados_atualizados = data.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizados.items():
        setattr(favoritos_atualizado, campo, valor)


    db.commit()
    db.refresh(favoritos_atualizado)
    
    return favoritos_atualizado






@app.delete("/autores/{autor_id}",  status_code=204)
def deletar_autor(autor_id: int , db: Session = Depends(get_db)):
    autor = db.query(Autores).filter(Autores.id == autor_id ).first()

    if not autor:
        raise HTTPException(status_code=404, detail= "não encontrado")
    
    db.delete(autor)
    db.commit()
    
    return None