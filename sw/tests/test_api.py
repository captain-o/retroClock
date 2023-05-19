from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    data = {'key': 'value'}
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
