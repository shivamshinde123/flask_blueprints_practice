from flask import Blueprint
from myproject.articles.forms import AddForm, DelForm
from flask import Flask,render_template,redirect,url_for,session,flash
from myproject import db
from myproject.models import BlogPosts


articles_blueprint = Blueprint('articles',__name__,
                               template_folder="templates/articles")

@articles_blueprint.route('/list')
def list():
    articles = BlogPosts.query.all()
    return render_template('list.html', articles=articles)

@articles_blueprint.route('/add',methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        article_title = form.article_title.data
        article_content = form.article_content.data

        new_article = BlogPosts(name, article_title, article_content)
        db.session.add(new_article)
        db.session.commit()

        session['name'] = form.name.data
        session['article_title'] = form.article_title.data
        flash(f"The article named {session['article_title']} posted by {session['name']}.")

        return redirect(url_for('articles.list'))
    return render_template('add.html', form=form)

@articles_blueprint.route('/delete',methods=['GET', 'POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        article_title = form.article_title.data
        post = BlogPosts.query.filter_by(article_title=article_title).first()
        db.session.delete(post)
        db.session.commit()

        session['article_title'] = form.article_title.data
        flash(f"The article named {session['article_title']} deleted.")

        return redirect(url_for('articles.list'))
    return render_template('delete.html', form=form)

