from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///milma.db'
db = SQLAlchemy(app)

from models import Farmer, MilkCollection, Payment

# Create DB
@app.before_first_request
def create_tables():
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