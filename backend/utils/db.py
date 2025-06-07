from flask_mysqldb import MySQL
from flask import g

mysql = MySQL()

def init_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'R6@#Siege'
    app.config['MYSQL_DB'] = 'ecommerce'
    mysql.init_app(app)

def get_db():
    if 'db' not in g:
        g.db = mysql.connection
    return g.db
