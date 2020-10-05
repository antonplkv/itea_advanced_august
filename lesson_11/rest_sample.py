from flask import Flask, request
from models import User

app = Flask(__name__)


def get_response(data, status=200):
    return app.response_class(
        response=data,
        status=status,
        mimetype='application/json'
    )


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id=None):
    if request.method == 'GET':
        data = User.objects().to_json()
        return get_response(data)

    elif request.method == 'POST':
        user_obj = User.objects.create(**request.json)
        return get_response(user_obj.to_json())

    elif request.method == 'PUT':
        print(request.method)
    elif request.method == 'DELETE':
        print(request.method)

    return ''


app.run(debug=True)