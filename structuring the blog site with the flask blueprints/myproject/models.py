from myproject import db

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

