from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import user as crud
from database import get_db
from schemas import user as schemas
from schemas.response import ResponseSchema

router = APIRouter(prefix="/user", tags=["user"])

# Register
@router.post("/", response_model= ResponseSchema[schemas.RegisterResponse])
def register(user:schemas.Register, db:Session = Depends(get_db)):
    return crud.register(db, user)

# Login
@router.post("/", response_model= ResponseSchema[schemas.LoginResponse])
def login(user:schemas.Login, db:Session = Depends(get_db)):
    return crud.login(db, user)