# models.py
from config import db

class Users(db.Model):
    __table__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)
    password = db.Column(db.String(1000),
                         nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)

class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    decription = db.Column(db.String, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    
class User_google_and_gith(db.Model):
    __tablename__ = 'users_external'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)