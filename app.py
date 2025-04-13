from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/jsontest')
def json_test():
    return {'name': 'John', 'age': 28, 'city': 'New York',
            'array of objects': [{'name': 'John', 'age': 29, 'city': 'New York'},
                                     
                                    {'name': 'John', 'age': 30, 'city': 'New York'}],}
if __name__ == '__main__':
    app.run(debug=True)
