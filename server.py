from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def about():
    return render_template('add.html')


@app.route('/auth')
def auth():
    return render_template('auth.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)