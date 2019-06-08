import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_admin import Admin

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flask_blueprints.db'

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
admin = Admin(app)

from app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
