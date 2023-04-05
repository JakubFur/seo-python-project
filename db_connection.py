# testowanie przerzucenia połączenia db.
# https://stackoverflow.com/questions/66473161/how-put-db-connection-in-seperate-file-and-use-in-another-file-in-python
# solution no1---------------------------

# import mysql.connector

# db_connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Pieniazek21"
#     )

#--------------------------------------------

# solution no2 ==============================
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    # fields here
    pass


        # ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pieniazek21@localhost/bucketlist'
        # app.config['SECRET_KEY'] = '1234'
        # db = SQLAlchemy(app)