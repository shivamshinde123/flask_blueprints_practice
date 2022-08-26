from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField("Owner's name")
    puppy_id = IntegerField('Id of the puppy')
    submit = SubmitField('Add Owner')

