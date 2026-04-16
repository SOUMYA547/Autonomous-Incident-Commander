from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def auth():
    if random.random() < 0.2:
        return {"error": "timeout error"}
    return {"status": "auth success"}