from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
from models import Events
import sqlite3


app = Flask(__name__, static_folder='./static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy()



login_manager = LoginManager()
login_manager.init_app(app)


	
class Users(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(250), unique=True, nullable=False)
	password = db.Column(db.String(250), nullable=False)
	
class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    decription = db.Column(db.String, nullable=False)
    date = db.Column(db.Integer, nullable=False)


db.init_app(app)


with app.app_context():
	db.create_all()


@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)


@app.route('/register', methods=["GET", "POST"])
def register():
	if request.method == "POST":
		user = Users(username=request.form.get("username"),
					password=request.form.get("password"))
		db.session.add(user)
		db.session.commit()
		return redirect(url_for("login"))
	return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		user = Users.query.filter_by(
			username=request.form.get("username")).first()
		if user.password == request.form.get("password"):
			login_user(user)
			return redirect(url_for("home"))
	return render_template("login.html")


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("home"))


@app.route("/")
def home():
	return render_template("home.html")

@app.route('/profile')
def profile():
    return render_template('profile.html')




@app.route('/events')
def events():
	conn = sqlite3.connect('instance/db.sqlite')
	cur = conn.cursor()
	title = cur.execute(''' SELECT title FROM events ''').fetchone()
	return render_template('events.html', title=title)

if __name__ == "__main__":
	app.run()
