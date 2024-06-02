from fastapi import FastAPI
from databases import Database

app=FastAPI()

@app.get('/')
async def homepage():
    return "Welcome to FastApi"

