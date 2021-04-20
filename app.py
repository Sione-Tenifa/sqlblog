"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash, session
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog_user_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension

connect_db(app)

@app.route('/')
def list_users():
    users = User.query.all()

    return render_template('index.html', users=users)