from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine, Base
from models import Carro, Dono, Aluno, Curso
from schemas import CarroCreate, CarroUpdade, CarroResponse, DonoResponse, DonoCreate, DonoComCarrosResponse,DonoUpdade,CarroComDonoResponse,AlunoCreate,AlunoResponse,CursoCreate,CursoResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return "No ar"


@app.get("/carros", response_model=List[CarroResponse])
def listar_carros(db: Session = Depends(get_db)):
    carros = db.query(Carro).all()

    return carros


@app.post("/carros", response_model = CarroResponse)
def criar_carros(carro: CarroCreate, db: Session = Depends(get_db)):
    novo_carro = Carro(**carro.model_dump())

    db.add(novo_carro)
    db.commit()
    db.refresh(novo_carro)

    return novo_carro


@app.delete("/carros/{id}",  status_code=204)
def deletar_carro(id: int , db: Session = Depends(get_db)):
    carro = db.query(Carro).filter(Carro.id == id ).first()

    if not carro:
        raise HTTPException(status_code=404, detail= "Carro não encontrado")
    
    db.delete(carro)
    db.commit()
    
    return None



@app.get("/donos", response_model=List[DonoResponse])
def listar_donos(db: Session = Depends(get_db)):
    dono = db.query(Dono).all()

    return dono

@app.post("/donos", response_model=DonoResponse, status_code=201)
def criar_dono(dono: DonoCreate, db: Session = Depends(get_db)):
    dono_existe = db.query(Dono).filter(Dono.cpf == dono.cpf).first()

    if dono_existe:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")
    
    novo_dono = Dono(**dono.model_dump())
    db.add(novo_dono)
    db.commit()
    db.refresh(novo_dono)

    return novo_dono

@app.post("/carros/{carro_id}/vincular/{dono_id}")
def vincular(carro_id: int, dono_id: int , db: Session = Depends(get_db)):
    carro = db.query(Carro).filter(Carro.id == carro_id).first()

    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    
    dono = db.query(Dono).filter(Dono.id == dono_id).first()


    if not dono:
        raise HTTPException(status_code=404, detail="Dono não encontrado")
    
    carro.dono_id = dono_id
    db.commit()
    db.refresh(carro)


    return {
        "message": "Carro vinculado com sucesso",
        "carro": {
            "id":carro.id,
            "modelo": carro.modelo,
            "placa": carro.placa
        },
        "dono": {
            "id": dono.id,
            "nome": dono.nome,
            "cpf":dono.cpf
        }
    }




@app.post("/alunos", response_model=AlunoResponse)
def criar_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    novo_aluno = Aluno(nome = aluno.nome)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)

    return novo_aluno 



@app.post("/cursos", response_model=CursoResponse)
def criar_cursos(curso: CursoCreate, db: Session = Depends(get_db)):
    novo_curso = Curso(nome = curso.nome)
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)

    return novo_curso 


@app.get("/alunos{id}", response_model=AlunoResponse)
def listar_alunos(id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).get(id)

    return aluno


@app.post("/alunos/{id_aluno}/cursos/{id_curso}")
def vincular_aluno(id_aluno: int , id_curso: int , db: Session = Depends(get_db)):
    aluno = db.query(Aluno).get(id_aluno)
    curso = db.query(Curso).get(id_curso)

    aluno.cursos.append(curso)
    db.commit()

    return {"message": "Aluno matriculado com sucesso"}