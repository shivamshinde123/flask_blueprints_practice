from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired


class AddForm(FlaskForm):

    name = StringField('Author Name: ')
    article_title = StringField('Article Title: ')
    article_content= TextAreaField('Article Content: ')
    submit = SubmitField('Post Now')


class DelForm(FlaskForm):

    article_title = StringField('Name of  the Article: ')
    submit = SubmitField('Delete the article')