from main import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String(100), unique=True, nullable=False)