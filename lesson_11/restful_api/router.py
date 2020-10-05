from flask import Flask
from flask_restful import Api
from resources import UserResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/users', '/users/<user_id>')

app.run(
    debug=True
)