from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Miguel"}
    posts = [
        {"author": {"username": "John"}, "body": {"Beautiful day in Portland..."}},
        {"author": {"username": "Pista"}, "body": {"Ez aztan nagyon fasza!"}},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
