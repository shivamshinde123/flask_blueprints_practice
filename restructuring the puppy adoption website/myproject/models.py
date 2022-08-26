## models
from myproject import db
# we will set up db inside the __init__.py file

class Puppy(db.Model):
    __tablename__ = 'Puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='Puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Owner of the puppy {self.name} is {self.owner.name}"


class Owner(db.Model):
    __tablename__ = 'Owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('Puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id