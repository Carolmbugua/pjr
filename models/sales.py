from datetime import datetime
from main import db

class  Sales(db.Model):
    __tablename__ = 'sales'
    item_id = db.Column(db.Integer, primary_key=True)
    inv_id = db.Column(db.Integer, db.ForeignKey('inventories.item_id'))
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


   #add a new record
    def add_records(self):
        db.session.add(self)
        db.session.commit()

     #fetching all records
    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    @classmethod
    def fetch_one_records(cls,id):
        return cls.query.filter_by(item_id=id).first()