from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base
from sqlalchemy.orm import relationship

class Auto(Base):
    __tablename__ = 'autos'

    id = Column(Integer, primary_key=True, index=True)
    puertas = Column(Integer)
    color = Column(String(20))
    marca = Column(ForeignKey('marcas.id'))

    marcaItem = relationship('Marca', back_populates='items')

class Marca(Base):
    __tablename__ = 'marcas'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20))

    items = relationship('Auto', back_populates='marcaItem')