#imports
from flask import Flask
from bson.objectid import ObjectId
from datetime import datetime


#initialize app

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'


if __name__ == 'main':
    app.run()