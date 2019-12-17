from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from models.index import db
from bson.objectid import ObjectId

user_blueprint = Blueprint('users', __name__, url_prefix='/users')

@user_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return 'Hello World'