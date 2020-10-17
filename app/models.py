from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Pet(Base):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tag = Column(String)
