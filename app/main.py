from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Error(BaseModel):
    code: int
    message	: str


@app.get("/pets", response_model=List[schemas.Pet], responses={"default": {"model": Error}})
async def pets_list(tags: Optional[List[str]] = Query(None), limit: Optional[int] = None, db: Session = Depends(get_db)):
    pets = crud.get_pets(db, tags=tags, limit=limit)
    return pets


@ app.post("/pets", response_model=schemas.Pet, responses={"default": {"model": Error}})
async def create_pets(pet: schemas.NewPet, db: Session = Depends(get_db)):
    db_pet = crud.get_pet_by_name(db, name=pet.name)
    if db_pet:
        raise HTTPException(
            status_code=400, detail="Pet name already registered")
    return crud.create_pet(db=db, pet=pet)


@ app.get("/pets/{id}", response_model=schemas.Pet, responses={"default": {"model": Error}})
async def get_pet(id: int, db: Session = Depends(get_db)):
    pets = crud.get_pet(db, id=id)
    return pets


@ app.delete("/pets/{id}", status_code=204, responses={"default": {"model": Error}})
async def delete_pet(id: int, db: Session = Depends(get_db)):

    return crud.delete_pet(db, id=id)
