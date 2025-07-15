from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.user import User as models
from schemas import user as schemas
from schemas.response import ResponseSchema
from utils.security import hash_password, verify_password



# Register 
def register(db:Session, user:schemas.Register):
    
    validate_email = db.query(models).filter(models.email == user.email).first()
    if  validate_email:
        return ResponseSchema(
            code=str(status.HTTP_400_BAD_REQUEST), 
            status="error",
            message="email already exist.",
            data= None
        )
        
    hashed = hash_password(user.password)
    user_data = user.model_dump()
    user_data["password"] = hashed
    
    new_user = models(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return ResponseSchema(
        code=str(status.HTTP_201_CREATED),
        status="ok",
        message="Register successfully",
        data= new_user
    )
    
# Login
def login(db:Session, user:schemas.Login):
    # 1. Check email
    # 2. Verify password 
    # 3. Create Token
    # 4. Response
    return