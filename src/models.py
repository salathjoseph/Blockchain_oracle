from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shop_owner = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pending')
