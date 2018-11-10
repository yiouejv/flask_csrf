#encoding: utf-8

from config import Base
from sqlalchemy import Column, Integer, String, Float

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    deposit = Column(Float(50), default=0)


Base.metadata.create_all()
