from dotenv import load_dotenv
import os
load_dotenv()  # this reads the .env file
print(os.getenv("DATABASE_URL"))  # for testing

from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.db.models import *  # important


app = FastAPI(title="Rudrix")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}
