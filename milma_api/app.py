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