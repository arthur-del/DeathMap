from flask import Flask
from flask_restful import Api, Resource
from deathMap import getOneMatchDeathCoordinate

app = Flask(__name__)
api = Api(app)


class DeathCoordinates(Resource):
    
    #Requires: request, username(string)
    #Returns: DeathCoordinates(Array Of dictionaries)
 def get(self, username):
    return getOneMatchDeathCoordinate(username, "RGAPI-eb5e2718-c2e4-4560-9102-519b9424d496")
        


api.add_resource(DeathCoordinates, "/deathCoordinates/<string:username>")

if __name__ == "__main__":
    app.run(debug=True)
