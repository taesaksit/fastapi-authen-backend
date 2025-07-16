from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import user as crud
from database import get_db
from schemas import user as schemas
from schemas.response import ResponseSchema
from typing import List
from utils import security

router = APIRouter(prefix="/user", tags=["user"])

# Login
@router.post("/login", response_model= ResponseSchema[schemas.LoginResponse])
def login(user:schemas.Login, db:Session = Depends(get_db)):
    return crud.login(db, user)

# Register
@router.post("/register", response_model= ResponseSchema[schemas.RegisterResponse])
def register(user:schemas.Register, db:Session = Depends(get_db)):
    return crud.register(db, user)

# Get All User
@router.get("/", 
            response_model=ResponseSchema[List[schemas.UserResponse]],
            dependencies=[Depends(security.is_login)]
            )
def read_users(db:Session = Depends(get_db)):
    return crud.get_users(db)