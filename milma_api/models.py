from app import db
from datetime import datetime

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    village = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    bank_account = db.Column(db.String(100))

    def to_dict(self):
        return dict(id=self.id, name=self.name, village=self.village, contact=self.contact, bank_account=self.bank_account)
