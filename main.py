from fastapi import FastAPI
from user.routes import Routes

app = FastAPI()

@app.get("/")
def read_root():
    return Routes().read_root()
