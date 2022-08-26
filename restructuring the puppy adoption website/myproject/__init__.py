import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# here we will set up the database and migration capabilities
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASDOHEiohOIH'


## SQL database section

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)

from myproject.owners.views import owners_blueprint
from myproject.puppies.views import puppy_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppy_blueprint,url_prefix='/puppies')