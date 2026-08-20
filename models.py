# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base


class ProdutoDB(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)


class AlunoDB(Base):
    __tablename__ = "estudantes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    matricula = Column(Integer, nullable=False)
    curso = Column(String(50), nullable=False)  
    email = Column(String(100), nullable=False)