from fastapi import FastAPI
from functions import greet
app = FastAPI()

@app.get("/")
async def root():
    response = greet()
    return {"message": response}