import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))

    legos = db.relationship("Lego", backref="users", lazy=False)

    collections = db.relationship("Collection", backref="users", lazy=False)

    # Should I add check_password?

    def get_id(self):
        return self.user_id


class Collection(db.Model):
    __tablename__ = "collections"

    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_title = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    legos = db.relationship("Lego", backref="collections", lazy=False)


class Lego(db.Model):
    __tablename__ = "legos"

    lego_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    l_title = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text)
    picture_path = db.Column(db.String)
    instructions_url = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    c_id = db.Column(db.Integer, db.ForeignKey("collections.c_id"), nullable=True)

    comments = db.relationship("Comment", backref="legos", lazy=False)


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

    legos = db.relationship("Lego", backref="wishlists", lazy=False)


def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db...")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    