from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base






class Dono(Base):
    __tablename__ = "donos"
    id = Column(Integer , primary_key= True, index= True)
    nome = Column(String , index= True)
    cpf = Column(String , index = True , unique = True)

    carros = relationship("Carro", back_populates="dono")



class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String, index=True, nullable=False)
    placa = Column(String, index=True, nullable = False)
    dono_id = Column(Integer, ForeignKey("donos.id"), nullable=True)

    dono = relationship("Dono", back_populates="carros")


alunos_cursos = Table(
    "alunos_cursos",
    Base.metadata,
    Column("aluno_id", Integer, ForeignKey("alunos.id", ondelete="CASCADE"), primary_key=True),
    Column("curso_id", Integer , ForeignKey("cursos.id", ondelete="CASCADE"), primary_key=True)
)



class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer , primary_key=True)
    nome = Column(String, nullable=False)

    cursos = relationship("Curso", secondary=alunos_cursos, back_populates="alunos", lazy="select")



class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer , primary_key=True)
    nome = Column(String , nullable=False)

    alunos = relationship("Aluno", secondary=alunos_cursos, back_populates="cursos")