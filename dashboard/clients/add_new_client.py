from flask import Flask
from flask import Blueprint, render_template
from flask_login import login_required
import app
import db_connection

add_client_bp = Blueprint("addclient", __name__, static_folder='static', template_folder='templates')

db = db_connection.db()
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clientName = db.Column(db.String(80), nullable=False, unique=True)

    # kolumny relacyjne - mają mieć opcję tylko kont z flagą $specseo lub $account
    seoSpec = db.Column(db.String(80), nullable=False)
    account = db.Column(db.String(80), nullable=False)

    clientUrl = db.Column(db.String(80), nullable=False)
    copyType = db.Column(db.String(80), nullable=False)
    #kolumna typu data
    startDate = db.Column(db.String(80), nullable=False)

    projectType = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(80), nullable=False)

    apiKey = db.column(db.String(80))



@add_client_bp.route('/', methods=['POST','GET'])
@login_required
def add_client():
    """Add new client to DB"""
    return render_template('add-client.html')