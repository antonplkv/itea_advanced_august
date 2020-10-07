from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
import json
from models import User
from schemas import UserSchema


class UserResource(Resource):

    def get(self, user_id=None):
        if user_id:
            data_result = User.objects.get(id=user_id)
        else:
            data_result = User.objects()

        return UserSchema().dump(data_result, many=True)

    def post(self):
        try:
            data = UserSchema().load(request.json)
        except ValidationError as e:
            return {'error': str(e)}
        user = User.objects.create(**data)
        return UserSchema().dump(user)

    def put(self, user_id):
        user = User.objects(id=user_id)
        user.update(**request.json)
        return json.loads(user.to_json())

    def delete(self):
        pass