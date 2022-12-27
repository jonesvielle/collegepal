from pydantic import BaseModel

class CreateCommunity(BaseModel):
    comunityName:str
    picture:str
    descriptiion:str
    population:int
