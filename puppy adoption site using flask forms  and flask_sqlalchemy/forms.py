from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):


    name = StringField('Name of the puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove: ')
    submit = SubmitField('Remove Puppy')


class AddOwner(FlaskForm):

    name = StringField("Owner's name")
    puppy_id = IntegerField('Id of the puppy')
    submit = SubmitField('Add Owner')

