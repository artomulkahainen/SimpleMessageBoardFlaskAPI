from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "posts"

    def __init__(self, post):
        self.post = post

    def __repr__(self):
        return f"<Post {self.post}>"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    post = db.Column(db.String)
