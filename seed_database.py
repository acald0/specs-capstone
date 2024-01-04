from os import system
from server import app
from models import db, connect_to_db, Lego, Category, Comment, User, Wishlist

system("dropdb lego-app")
system("createdb lego-app")

connect_to_db(app)

with app.app_context():
    db.create_all()

    user1 = User(username="UncleBobbyB", password="legopass")
    user2 = User(username="FrankinTankin", password="didyouknowthat")
    db.session.add_all([user1, user2])
    db.session.commit()