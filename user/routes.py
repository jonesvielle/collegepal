from .models import CreateCommunity
class Routes:
    def read_root(self):
        return {"Hello": "World"}