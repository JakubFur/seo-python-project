from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
# import db_connection

import dashboard.dashboard
from dashboard.dashboard import panel
from dashboard.clients.add_new_client import add_client_bp


app = Flask(__name__)
app.register_blueprint(panel, ulr_prefix='/dashboard')
app.register_blueprint(add_client_bp, url_prefix='/add-client')
bcrypt = Bcrypt(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pieniazek21@localhost/bucketlist'
app.config['SQLALCHEMY_TRACK_MODYFICATIONS'] = False
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy(app)

login_menager = LoginManager()
login_menager.init_app(app)
login_menager.login_view = "login"


@login_menager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Rejestracja")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError("Użytkownik o takiej nazwie istnieje!")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Logowanie")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pieniazek21@localhost/bucketlist'
# mysql = SQLAlchemy(app)


@app.route('/')
def home():
    """Strona główna"""
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    """Strona logowania"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('/dashboard')
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    """Wylogowanie"""
    logout_user()
    flash("Wylogowano")
    return redirect(url_for('home'))


@app.route('/register', methods=['GET','POST'])
def register():
    """Rejestracja"""
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Zarejestrowano użytkownika")
        return redirect(url_for('login')), 201
    flash("Nieprawidłowe dane!")
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=80)