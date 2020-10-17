from typing import List, Optional

from pydantic import BaseModel


class PetBase(BaseModel):
    id: int
    name: str
    tag	: Optional[str] = None


class NewPet(BaseModel):
    name: str
    tag	: Optional[str] = None


class Pet(PetBase):
    id: int
    name: str
    tag	: Optional[str] = None

    class Config:
        orm_mode = True
