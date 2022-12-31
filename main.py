from fastapi import FastAPI
from user.routes import Routes
from user.models import CreateCommunity, JoinCommunity

app = FastAPI()

@app.get("/")
def read_root():
    return Routes().read_root()

@app.post("/create_communities/")
def create_communities(createCommunity:CreateCommunity):
    return Routes.create_community(createCommunity)

@app.post("/join_community/")
def join_community(joinCommunity:JoinCommunity):
    return Routes.join_community(joinCommunity)
