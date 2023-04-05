from flask import Flask, render_template, blueprints, url_for, redirect
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError
# from flask_bcrypt import Bcrypt
from dashboard import dashboard


client = Blueprint("client", __name__, static_folder='static', render_template='templates')

# change config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pieniazek21@localhost/bucketlist'
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy(app)


@client.route('/dashboard')
@login_required
def addClient():
    return 0;