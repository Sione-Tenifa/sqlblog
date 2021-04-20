"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash, session
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'tenifa'
debug = DebugToolbarExtension

connect_db(app)

@app.route('/')
def list_users():
    users = User.query.all()

    return render_template('index.html', users=users)

@app.route('/new', methods=["GET"])
def users_new_form():
    """Show a form to create a new user"""

    return render_template('/new.html')

@app.route("/new", methods=["POST"])
def users_new():
    """Handle form submission for creating a new user"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img = request.form['img']

    new_user = User(first_name=first_name, last_name=last_name, img=img)


    db.session.add(new_user)
    db.session.commit()

    return redirect("/")

@app.route('/<int:user_id>')
def users_show(user_id):
    """Show a page with info on a specific user"""

    user = User.query.get_or_404(user_id)
    return render_template('show.html', user=user)

@app.route('/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('/edit.html', user=user)

@app.route('/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.img = request.form['img']

    db.session.add(user)
    db.session.commit()

    return redirect("/")

@app.route('/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/")

