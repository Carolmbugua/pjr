from main import db
class  Inventories(db.Model):
    __tablename__ = 'inventories'
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    sales = db.relationship('Sales', backref='inventories', lazy=True)

   #add a new record
    def add_records(self):
        db.session.add(self)
        db.session.commit()

     #fetching all records
    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    @classmethod
    def fetch_one_record(cls,id):
        return cls.query.filter_by(item_id=id).first()

