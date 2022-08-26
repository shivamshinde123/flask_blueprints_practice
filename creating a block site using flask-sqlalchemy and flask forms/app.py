from forms import AddForm,DelForm
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


class BlogPosts(db.Model):


    __tablename__ = 'BlogPosts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    article_title = db.Column(db.Text)
    article_content = db.Column(db.Text)

    def __init__(self,name,article_title,article_content):
        self.name = name
        self.article_title = article_title
        self.article_content = article_content

    def __repr__(self):
        return f"The article with the name {self.article_title} is written by {self.name}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list_articles')
def list_articles():
    articles = BlogPosts.query.all()
    return render_template('list_articles.html',articles=articles)


@app.route('/add_articles',methods=['GET', 'POST'])
def add_articles():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        article_title = form.article_title.data
        article_content = form.article_content.data

        new_article = BlogPosts(name,article_title,article_content)
        db.session.add(new_article)
        db.session.commit()

        session['name'] = form.name.data
        session['article_title']  = form.article_title.data
        flash(f"The article named {session['article_title']} posted by {session['name']}.")

        return redirect(url_for('list_articles'))
    return render_template('add_articles.html',form=form)


@app.route('/delete_articles',methods=['GET', 'POST'])
def delete_articles():

    form = DelForm()

    if form.validate_on_submit():
        
        article_title = form.article_title.data
        post = BlogPosts.query.filter_by(article_title=article_title).first()
        db.session.delete(post)
        db.session.commit()

        session['article_title'] = form.article_title.data
        flash(f"The article named {session['article_title']} deleted.")

        return redirect(url_for('list_articles'))
    return render_template('delete_articles.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)