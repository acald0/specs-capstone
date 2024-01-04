import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))


class Category(db.Model):
    __tablename__ = "categories"

    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_title = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))


class Lego(db.Model):
    __tablename__ = "legos"

    lego_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    l_title = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text)
    picture_path = db.Column(db.String)
    instructions_url = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    c_id = db.Column(db.Integer, db.ForeignKey("categories.c_id"), nullable=True)


class Comment(db.Model):
    __tablename__ = "comments"

    cmt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    lego_id = db.Column(db.Integer, db.ForeignKey("legos.lego_id"))


class Wishlist(db.Model):
    __tablename__ = "wishlists"

    w_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    lego_id = db.Column(db.Integer, db.ForeignKey("legos.lego_id"))


def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db...")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    