# import SQLAlchemy as SQLAlchemy
# import SQLAlchemy
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy
# print(SQLAlchemy.__version__)
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pieniazek21@localhost/bucketlist'
mysql = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)