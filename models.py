from flask_sqlalchemy import SQLAlchemy
import string
from random import choices

db = SQLAlchemy()


class Link(db.Model):
    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String, nullable=False)
    short_url = db.Column(db.String)

    def __init__(self, url):
        self.original_url = url
        self.short_url = self.shorten()

    def shorten(self):
        characters = string.digits + string.ascii_letters
        short_url = "".join(choices(characters, k=5))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.shorten()

        return short_url
