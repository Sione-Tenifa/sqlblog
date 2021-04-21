"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"
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
    first_name = db.Column(db.String,
                     nullable=False,
                     unique=True)
    last_name = db.Column(db.String,
                     nullable=False,
                     unique=True)                    
    img = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE_URL)
    
    @property
    def full_name(self):
        """Return full ntitleof user."""

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Blog post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref='users')

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")