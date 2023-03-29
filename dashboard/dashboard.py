from flask import Flask
from flask import Blueprint, render_template
from flask_login import login_required



panel = Blueprint("dashboard", __name__, static_folder='static', template_folder='templates')

@panel.route('/dashboard')
@login_required
def dashboard():
    """Dashboard"""
    # return render_template('dashboard.html')
    return render_template('dashboard.html')
# @dashboard.route('/indexing-api', methods=['GET', 'POST'])
# @login_required
# def indexingAPI():
#     return render_template('dashboard.html');


