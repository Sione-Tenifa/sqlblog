"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User"""
    __tablename__ = "users"


    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name= {u.first_name} last_name={u.last_name} img={u.img}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(20),
                     nullable=False,
                     unique=True)
    last_name = db.Column(db.String(20),
                     nullable=False,
                     unique=True)                    
    img = db.Column(db.String(30), nullable=False)
    