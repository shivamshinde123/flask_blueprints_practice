from flask import Flask, render_template, redirect, url_for, flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app  = Flask(__name__)

app.config['SECRET_KEY'] = 'OHoihOIhoiH'

## database setup

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from myproject.articles.views import articles_blueprint

app.register_blueprint(articles_blueprint, url_prefix='/articles')

