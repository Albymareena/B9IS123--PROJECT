from db import db
from datetime import datetime

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    village = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    bank_account = db.Column(db.String(100))

    def to_dict(self):
        return dict(id=self.id, name=self.name, village=self.village, contact=self.contact, bank_account=self.bank_account)

class MilkCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    volume_litres = db.Column(db.Float)
    fat_percentage = db.Column(db.Float)
    snf_percentage = db.Column(db.Float)

    def to_dict(self):
        return dict(id=self.id, farmer_id=self.farmer_id, date=self.date.isoformat(),
                    volume_litres=self.volume_litres, fat_percentage=self.fat_percentage,
                    snf_percentage=self.snf_percentage)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
    amount = db.Column(db.Float)
    status = db.Column(db.String(50))  # 'Paid' or 'Pending'
    date = db.Column(db.Date, default=datetime.utcnow)

    def to_dict(self):
        return dict(id=self.id, farmer_id=self.farmer_id, amount=self.amount,
                    status=self.status, date=self.date.isoformat())
