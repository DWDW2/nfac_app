from app_init import app, get_db, FDataBase, connect_db, close_db
from flask import render_template
@app.route('/')
def read_evetns():
    return render_template('home.html')