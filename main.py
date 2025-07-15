from fastapi import FastAPI, HTTPException
from database import Base, engine
from routes  import user
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message":"FastAPI-Authentication !!!"}