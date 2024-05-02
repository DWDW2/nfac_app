from flask import Flask, render_template, request, url_for, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
#config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'A21858BFA39E229F847D2463D776A'
app.json.compact = False
db = SQLAlchemy(app=app)
login_manager = LoginManager()
login_manager.init_app(app)
#модели Sqlalchemy
class Users(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)
    password = db.Column(db.String(1000),
                         nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    registered_events = db.relationship('UserEvent', back_populates='user')

class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    decription = db.Column(db.String(300))
    url_to_img = db.Column(db.String(300))
    envent_url = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(300), nullable=False)
    city = db.Column(db.String(300), nullable=False)
    registrations = db.relationship('UserEvent', back_populates='event')

class UserEvent(db.Model):
    __tablename__ = 'user_events'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True)
    user = db.relationship('Users', back_populates='registered_events')
    event =db.relationship('Events', back_populates='registrations')

with app.app_context():
	db.create_all()

#app
@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)


@app.route('/')
def home():
    if 'user_id' in session:
        user = Users.query.filter_by(id=session['user_id']).first()
        username = user.username
    else:
         username = ''
    return render_template('home.html', user=username)

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        hashed_password = generate_password_hash(password)

        existing_user = Users.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))
        
        new_user = Users(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']  
        password = request.form['password']
        user = Users.query.filter((Users.username == identifier) | (Users.email == identifier)).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or email or password. Please try again.', 'error')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)

    flash('You have been logged out.', 'info')

    return redirect(url_for('home'))
#Функция для нахождения ивентов
@app.route('/findevents')
def events_page():
    if 'user_id' in session:
        user = Users.query.filter_by(id=session['user_id']).first()
        username = user.username
    else:
         username = ''
    return render_template('events.html', user=username)

#функция для получения ивентов
@app.route('/search', methods=['GET', 'POST'])
def findEvents():
    if 'user_id' in session:
        user = Users.query.filter_by(id=session['user_id']).first()
        username = user.username
    else:
         username = ''
    city = request.args.get('city')
    category = request.args.get('category')

    print(city, category)

    if city or category:
        results = Events.query.filter(Events.category.icontains(category) & Events.city.icontains(city)) \
        .order_by(Events.id.asc()).all()
    else:
        results = Events.query.order_by(Events.id.asc())
    return render_template("events_result.html", results=results, user=username)
    





if __name__ == "__main__":
	app.run()
