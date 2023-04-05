from flask import Flask
from flask import Blueprint, render_template
from flask_login import login_required
# from dashboard.clients.add_new_client import add_client_bp

panel = Blueprint("main", __name__, static_folder='static', template_folder='templates')

# jako app.register działa w pliku main, ale nie działa w dashboard, dlaczego?
# panel.register_blueprint(add_client_bp, url_prefix='/add-client')


@panel.route('/dashboard', methods=['POST','GET'])
# @panel.route('/', methods=['POST','GET'])
@login_required
def dashboard():
    """Dashboard"""
    return render_template('dashboard.html')

# @panel.route('/add-client')
# @login_required
# def add_client():
#     """Dashboard"""
#     # return render_template('dashboard.html')
#     return render_template('Indexing-api.html')


# @dashboard.route('/indexing-api', methods=['GET', 'POST'])
# @login_required
# def indexingAPI():
#     return render_template('dashboard.html');


