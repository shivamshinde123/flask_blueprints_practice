from forms import AddForm, DelForm, AddOwner
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASDOHEiohOIH'


## SQL database section

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)


## models

class Puppy(db.Model):

    __tablename__ = 'Puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='Puppy',uselist=False)
    

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Owner of the puppy {self.name} is {self.owner.name}"


class Owner(db.Model):

    __tablename__ = 'Owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('Puppies.id'))


    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_puppies',methods=['GET', 'POST'])
def add_puppies():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        new_puppy = Puppy(name)
        db.session.add(new_puppy)
        db.session.commit()

        return redirect(url_for('list_puppies'))

    return render_template('add.html',form=form)

@app.route('/list_puppies',methods=['GET', 'POST'])
def list_puppies():

    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)


@app.route('/delete_puppies',methods=['GET', 'POST'])
def delete_puppies():


    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_puppies'))

    return render_template('delete.html',form=form)


@app.route('/add_owner',methods=['GET', 'POST'])
def add_owner():

    form = AddOwner()

    if form.validate_on_submit():

        name = form.name.data
        puppy_id = form.puppy_id.data

        new_owner = Owner(name,puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_puppies'))

    return render_template('add_owner.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
 