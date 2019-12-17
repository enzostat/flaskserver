#imports
from flask import Flask
from bson.objectid import ObjectId
from datetime import datetime
from blueprints.barbers import barbers_blueprint


#initialize app

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'


#Blueprints
app.register_blueprint(barbers_blueprint)


if __name__ == 'main':
    app.run()