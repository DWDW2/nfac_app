# models.py
from config import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)
    password = db.Column(db.String(250),
                         nullable=False)

class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    decription = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(200), nullable=False)
    