from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(150), nullable=False, unique=True)
    last_name = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.String(150), nullable=False, unique=True)
    billing_address = db.Column(db.String(150), nullable=False, unique=True)
    shipping_address = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    
    def __init__(self, username, first_name, last_name, phone, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.billing_address = billing_address
        self.shipping_address = shipping_address
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'<User: {self.username} | {self.email}>'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    price = db.Column(db.String(150))
    category = db.Column(db.String(150))
    description = db.Column(db.String(300))
    image_url = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, price, category, description, image_url, user_id):
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        self.image_url = image_url
        self.user_id = user_id

    def __repr__(self):
        return f'<Product: {self.name}>'