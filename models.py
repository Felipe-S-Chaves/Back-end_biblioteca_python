from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from database import Base


class Autores(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True , nullable=False)

    livros = relationship("Livros", back_populates="autores")


class Editoras(Base):
    __tablename__ = "editoras"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)

    livros = relationship("Livros", back_populates="editoras")      



class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    email = Column(String, unique=True ,index=True, nullable=False)
    senha = Column(String, index=True, nullable=False)

    emprestimos = relationship("Emprestimos", back_populates="usuarios")


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    email = Column(String, unique=True ,index=True, nullable=False)
    senha = Column(String, index=True, nullable=False)



class Livros(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("autores.id"), nullable=False)
    editora_id = Column(Integer, ForeignKey("editoras.id"), nullable=False)

    emprestimos = relationship("Emprestimos", back_populates="livros")
    favoritos = relationship("Favoritos", back_populates="livros")
    editoras = relationship("Editoras", back_populates="livros")
    autores = relationship("Autores", back_populates="livros")




class Favoritos(Base):
    __tablename__ = "favoritos"

    id = Column(Integer, primary_key=True, index=True)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    livros = relationship("Livros", back_populates="favoritos")



class Emprestimos(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True, index=True)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    data_retirada = Column(Date, index=True, nullable=False)
    data_devolucao = Column(Date, index=True, nullable=False)

    livros = relationship("Livros", back_populates="emprestimos")
    usuarios = relationship("Usuarios", back_populates="emprestimos")