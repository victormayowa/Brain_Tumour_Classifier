# neuroscope/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__, template_folder='templates', static_folder='static')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy()

'''
def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    db.init_app(app)
    #db.create_all()
    return app
    '''