from flask import Blueprint, request, redirect, jsonify
from models.index import db
from bson.objectid import ObjectId

barbers_blueprint = Blueprint('barbers', __name__, url_prefix='/barbers')

@barbers_blueprint.route('/', methods=["GET"])
def index():
    docs = []
    for doc in db.barbers.find():
        doc['_id'] = str(doc['_id'])
        docs.append(doc)

    return jsonify(docs)


@barbers_blueprint.route('/new', methods=["POST"])
def post_barber():
    name = request.form["name"]
    scheduled = []
    shopId = request.form["shopId"]

    print('Added a new barber')

    db.barbers.insert_one({
        'name': name,
        'scheduled': scheduled,
        'shopId': shopId
    })

    return 'Barber Created'
