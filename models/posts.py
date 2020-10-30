from app import db
from sqlalchemy import Column, Integer, String, TIMESTAMP

class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    post = Column(String)
    created_at = Column(TIMESTAMP)

    def __init__(self, post, created_at):
        self.post = post
        self.created_at = created_at

    def __repr__(self):
        return f'<id {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id, 
            'post': self.post,
            'created_at': self.created_at
        }