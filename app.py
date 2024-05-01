from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
from models import Events, Users
from config import LoginManager, db, app
import sqlite3





login_manager = LoginManager()
login_manager.init_app(app)

db.init_app(app)


with app.app_context():
	db.create_all()


@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)

@app.route('/')
def home():
	return render_template('home.html')
if __name__ == "__main__":
	app.run()
