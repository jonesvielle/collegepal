from pydantic import BaseModel

class CreateCommunity(BaseModel):
    communityName:str
    picture:str
    description:str
    population:int
    school:str
    password:str
    # admin

class UpdateCommunity(BaseModel):
    communityId:str

class JoinCommunity(BaseModel):
    communityName:str
    firstName:str
    lastName:str
    email:str
