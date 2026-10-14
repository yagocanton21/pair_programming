from fastapi import FastAPI
from database import get_connection

app = FastAPI()

@app.get("/")
def root():
    return{"message": "API online"}

