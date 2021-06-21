from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class DeathMap(Resource):
    def get(self):
        return {"data": "This is a death map"}


api.add_resource(DeathMap, "/deathmap")

if __name__ == "__main__":
    app.run(debug=True)

    # 1. try to run this
    # 2 copy right loclhost url into request
