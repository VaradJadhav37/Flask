from flask import Flask, request
from flask_restful import Api, Resource
import os
from pymongo import MongoClient
app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb+srv://VaradJ:varad21@cluster0.vpdku.mongodb.net/flask?retryWrites=true&w=majority&appName=Cluster0')

db=client.aNewDB
UserNum=db["UserNum"]
UserNum.insert_one({
    'numofusers': 0,
})
class Visit(Resource):
    def get(self):
        prev_num=UserNum.find({})[0]["numofusers"]
        UserNum.update_one({}, {"$set": {'numofusers': prev_num+1}})
        return str('Hello, World! You are visitor number: ' + str(prev_num+1))
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
api.add_resource(Visit, '/hello')
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
