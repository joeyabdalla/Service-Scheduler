from flask import Flask

from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class ServiceListResource(Resource):
    def get(self):
        return {"message": "List of services"}

api.add_resource(ServiceListResource, '/services')

if __name__ == "__main__":
    app.run(debug=True)
