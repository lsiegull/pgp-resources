from flask import Flask
app = Flask(__name__)

# returns a "hello world" string to the frontend
@app.route('/')
def hello_world():
    return 'Hello, World!'
