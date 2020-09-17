import os
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from models import *

# Configure app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_link():
    url = request.form['original-url']
    if Link.query.filter_by(original_url=url).first():
        link = Link.query.filter_by(original_url=url).first()
    else:
        link = Link(url)
        db.session.add(link)
        db.session.commit()

    return render_template("add.html", original_url=url, short_url=link.short_url)


@app.route("/<url>", methods=["POST", "GET"])
def redrect(url):
    link = Link.query.filter_by(short_url=url).first_or_404()
    if link:
        if link.original_url.find("http://") != 0 and link.original_url.find("https://") != 0:
            link.original_url = "http://" + link.original_url
    return redirect(link.original_url)


if __name__ == "__main__":
    app.run()
