from flask import Flask
from flask_restful import Api, Resource
from deathMap import getOneMatchDeathCoordinate
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources = {
    r"/*":{
        "origins":"http://127.0.0.1:5000"
    }
})
#app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)
#@cross_origin()

class DeathCoordinates(Resource):
    
    #Requires: request, username(string)
    #Returns: DeathCoordinates(Array Of dictionaries)
 def get(self, username):
    return getOneMatchDeathCoordinate(username, "RGAPI-d5277d75-6708-4f25-8ad6-e1f5d74c5cea")
        


api.add_resource(DeathCoordinates, "/deathCoordinates/<string:username>")

if __name__ == "__main__":
    app.run(debug=True)
