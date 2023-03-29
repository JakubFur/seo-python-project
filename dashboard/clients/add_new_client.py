from flask import Flask
from flask import Blueprint, render_template
from flask_login import login_required

add_client = Blueprint("addclient", __name__, static_folder='static', template_folder='templates')


@add_client.route('/add-client', methods=['POST','GET'])
@login_required
def add_client():
    """Add new client to DB"""
    return render_template('index.html')