from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/jsontest')
def json_test():
    json_data = {
        'name': 'John',
        'age': 28,
        'city': 'New York',
        'array of objects': [
            {'name': 'John', 'age': 29, 'city': 'New York'},
            {'name': 'John', 'age': 30, 'city': 'New York'}
        ]
    }
    return json_data

@app.route('/addnums', methods=['POST'])
def add_nums():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return {'result': result}

class Subtract(Resource):
    def post(self):
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        result = num1 - num2
        return {'result': result}

api.add_resource(Subtract, '/subtract')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
