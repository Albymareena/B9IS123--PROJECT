from flask import Flask, request, jsonify
from db import db
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1:3306/milma_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models import Farmer, MilkCollection, Payment

with app.app_context():
    db.create_all()

# FARMER ROUTES
@app.route('/api/farmers', methods=['GET'])
def get_farmers():
    farmers = Farmer.query.all()
    return jsonify([farmer.to_dict() for farmer in farmers])

@app.route('/api/farmers/<int:id>', methods=['GET'])
def get_farmer(id):
    farmer = Farmer.query.get_or_404(id)
    return jsonify(farmer.to_dict())

@app.route('/api/farmers', methods=['POST'])
def create_farmer():
    data = request.json
    farmer = Farmer(**data)
    db.session.add(farmer)
    db.session.commit()
    return jsonify(farmer.to_dict()), 201

@app.route('/api/farmers/<int:id>', methods=['PUT'])
def update_farmer(id):
    data = request.json
    farmer = Farmer.query.get_or_404(id)
    for key, value in data.items():
        setattr(farmer, key, value)
    db.session.commit()
    return jsonify(farmer.to_dict())