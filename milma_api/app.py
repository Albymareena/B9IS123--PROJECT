from flask import Flask, request, jsonify
from db import db
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3307/milma_db'
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

@app.route('/api/farmers/<int:id>', methods=['DELETE'])
def delete_farmer(id):
    farmer = Farmer.query.get_or_404(id)
    db.session.delete(farmer)
    db.session.commit()
    return '', 204

# MILK COLLECTION ROUTES
@app.route('/api/milk_collections', methods=['GET'])
def get_milk_collections():
    records = MilkCollection.query.all()
    return jsonify([r.to_dict() for r in records])

@app.route('/api/milk_collections/<int:id>', methods=['GET'])
def get_milk_collection(id):
    record = MilkCollection.query.get_or_404(id)
    return jsonify(record.to_dict())

@app.route('/api/milk_collections/farmer/<int:farmer_id>', methods=['GET'])
def get_milk_by_farmer(farmer_id):
    records = MilkCollection.query.filter_by(farmer_id=farmer_id).all()
    return jsonify([r.to_dict() for r in records])

@app.route('/api/milk_collections', methods=['POST'])
def create_milk_collection():
    data = request.json
    record = MilkCollection(**data)
    db.session.add(record)
    db.session.commit()
    return jsonify(record.to_dict()), 201

@app.route('/api/milk_collections/<int:id>', methods=['PUT'])
def update_milk_collection(id):
    data = request.json
    record = MilkCollection.query.get_or_404(id)
    for key, value in data.items():
        setattr(record, key, value)
    db.session.commit()
    return jsonify(record.to_dict())

@app.route('/api/milk_collections/<int:id>', methods=['DELETE'])
def delete_milk_collection(id):
    record = MilkCollection.query.get_or_404(id)
    db.session.delete(record)
    db.session.commit()
    return '', 204

# PAYMENT ROUTES
@app.route('/api/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([p.to_dict() for p in payments])

@app.route('/api/payments/<int:id>', methods=['GET'])
def get_payment(id):
    payment = Payment.query.get_or_404(id)
    return jsonify(payment.to_dict())

@app.route('/api/payments/farmer/<int:farmer_id>', methods=['GET'])
def get_payments_by_farmer(farmer_id):
    payments = Payment.query.filter_by(farmer_id=farmer_id).all()
    return jsonify([p.to_dict() for p in payments])

@app.route('/api/payments', methods=['POST'])
def create_payment():
    data = request.json
    payment = Payment(**data)
    db.session.add(payment)
    db.session.commit()
    return jsonify(payment.to_dict()), 201

@app.route('/api/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    data = request.json
    payment = Payment.query.get_or_404(id)
    for key, value in data.items():
        setattr(payment, key, value)
    db.session.commit()
    return jsonify(payment.to_dict())

@app.route('/api/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    payment = Payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)