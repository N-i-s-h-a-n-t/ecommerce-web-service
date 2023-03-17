from . import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), nullable=False)
