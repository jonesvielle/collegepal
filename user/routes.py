from datetime import datetime
from fastapi.responses import JSONResponse
import pymongo
import uuid
conn_string = 'mongodb://jones123:jones123@cluster0-shard-00-00.qelfv.azure.mongodb.net:27017,cluster0-shard-00-01.qelfv.azure.mongodb.net:27017,cluster0-shard-00-02.qelfv.azure.mongodb.net:27017/dataiot?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
client = pymongo.MongoClient(conn_string)
db = client.collegepal
class Routes:
    def read_root(self):
        return {"Hello": "World"}
    
    def create_community(CreateCommunity):
        community_name = CreateCommunity.__getattribute__("communityName")
        picture = CreateCommunity.__getattribute__("picture")
        description = CreateCommunity.__getattribute__("description")
        population = CreateCommunity.__getattribute__("population")
        school = CreateCommunity.__getattribute__("school")
        password = CreateCommunity.__getattribute__("password")
        date = datetime.now()
        id = uuid.uuid4().hex
        data = {
            "_id":id,
            "communityName":community_name,
            "picture":picture,
            "description":description,
            "population":population,
            "date":date,
            "school":school,
            "password":password
        }
        if db.communities.find_one({"school":school, "community_name":community_name}):
            return JSONResponse({"message":"group name exists already"}, 401)
        if db.communities.insert_one(data):
            return JSONResponse({"message":"uploaded"}, 200)
        return JSONResponse({"message":"something went wrong"}, 400)

    def join_community(JoinCommunity):
        communityName = JoinCommunity.__getattribute__("communityName")
        firstName = JoinCommunity.__getattribute__("firstName")
        lastName = JoinCommunity.__getattribute__("lastName")
        email = JoinCommunity.__getattribute__("lastName")
        id = uuid.uuid4().hex
        date = datetime.now()
        data = {
            "communityName":communityName,
            "firstName":firstName,
            "lastName":lastName,
            "email":email,
            "_id":id,
            "date":date
        }
        if db.members.find_one({"email":email, "communityName":communityName}):
            return JSONResponse({"message":"member already exist in this community"}, 401)
        if db.members.insert_one(data):
            return JSONResponse({"message":"joined sucessfully"}, 200)
        return JSONResponse({"message":"something went wrong"}, 400)
