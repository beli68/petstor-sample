from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas


def get_pet(db: Session, id: int):
    return db.query(models.Pet).filter(models.Pet.id == id).first()


def get_pet_by_name(db: Session, name: str):
    return db.query(models.Pet).filter(models.Pet.name == name).first()


def get_pets(db: Session, limit: Optional[int] = None, tags: Optional[List[str]] = None):
    if tags:
        return db.query(models.Pet).filter(models.Pet.tag.in_(tags)).limit(limit).all()
    return db.query(models.Pet).limit(limit).all()


def create_pet(db: Session, pet: schemas.NewPet):
    db_pet = models.Pet(
        name=pet.name, tag=pet.tag)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def delete_pet(db: Session, id: int):
    db.query(models.Pet).filter(models.Pet.id == id).delete()

    db.commit()

    return
