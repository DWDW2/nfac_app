# config.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# instantiate ap and set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
# define metadata, set up Flask-Migrate for migrations, instantiate d
db = SQLAlchemy(app)

# enables Cross-Origin Resource Sharing, allowing requests front-end
CORS(app)

# generate a secret key in command prompt using this command:
# `python -c 'import os; print(os.urandom(16))'`
app.config['SECRET_KEY'] = 'A21858BFA39E229F847D2463D776A'