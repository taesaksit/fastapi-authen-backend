from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.user import User as UserModel
from schemas import user as schemas
from schemas.response import ResponseSchema
from utils.security import hash_password, verify_password, create_access_token


# Utils: get user by email
def get_user_by_eamil(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


# Register
def register(db: Session, user: schemas.Register):
    db_user = get_user_by_eamil(db, user.email)

    if db_user:
        return ResponseSchema(
            code=status.HTTP_400_BAD_REQUEST,
            status="error",
            message=f"email {db_user.email} already exist.",
            data=None,
        )

    hashed_password = hash_password(user.password)
    user_data = user.model_dump()
    user_data["password"] = hashed_password

    new_user = UserModel(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return ResponseSchema(
        code=status.HTTP_201_CREATED,
        status="ok",
        message="Register successfully",
        data=new_user,
    )


# Login
def login(db: Session, user: schemas.Login):

    db_user = get_user_by_eamil(db, user.email)

    if not db_user:
        return ResponseSchema(
            code=status.HTTP_404_NOT_FOUND,
            status="error",
            message=f"Email {user.email} Not found",
            data=None,
        )

    is_valid_password = verify_password(user.password, db_user.password)
    if not is_valid_password:  # check False
        return ResponseSchema(
            code=status.HTTP_401_UNAUTHORIZED,
            status="error",
            message="Incorrect password",
            data=None,
        )

    user_response = {
        "id": str(db_user.id),
        "email": db_user.email,
        "name": db_user.name,
    }

    access_token = create_access_token(data={"data": user_response})

    return ResponseSchema(
        code=status.HTTP_200_OK,
        status="ok",
        message="Login successfull",
        data={"access_token": access_token, "token_type": "barear"},
    )


def get_users(db: Session):
    db_users = db.query(UserModel).all()
    return ResponseSchema(
        code=status.HTTP_200_OK, status="ok", message="List all users", data=db_users
    )
