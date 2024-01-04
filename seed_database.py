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
    user3 = User(username="Guy", password="Yegoyand")
    db.session.add_all([user1, user2, user3])
    db.session.commit()

    category1 = Category(c_title="Star Wars", user_id=1)
    category2 = Category(c_title="Harry Potter", user_id=1)
    category3 = Category(c_title="Ninjago", user_id=2)
    db.session.add_all([category1, category2, category3])
    db.session.commit()

    lego1 = Lego(l_title="Venator-Class Republic Attack Center", description="Star wars republic cruiser ship", picture_path="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLRzq1-n22foNk2YLcLZSLZRpLxGY5bFkbDmiD0Xtw1mn97XjHhG4QbE9k0vHuZad1CFc&usqp=CAU", instructions_url="https://www.lego.com/en-us/service/buildinginstructions/75367?locale=en-us", user_id=1, c_id=1)
    lego2 = Lego(l_title="Imperial Light Cruiser", description="Star wars Imperial cruiser ship", picture_path="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj0NSIGxYHuq7DEdVu2TCLe3_eXbI8chb7Hg&usqp=CAU", user_id=1, c_id=1)
    lego3 = Lego(l_title="The Battle of Hogwarts", description="Hogwarts set with fighting characters", picture_path="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQO126K1qEQy9HiMUulWuHLY561piqOOqYwOMcjU2fU1Fw-926KVg1JvOGiSj-j4KejQa0&usqp=CAU", user_id=1, c_id=2)
    lego4 = Lego(l_title="Misfortune's Keep", description="Ninjago set featuring air ship", picture_path="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN7ibTlyTt5kwHbRrXW6f_2nZtvaUDCMB0nw&usqp=CAU", instructions_url="https://www.lego.com/en-us/service/buildinginstructions/70605", user_id=2, c_id=3)
    lego5 = Lego(l_title="Welcome to Apocalypseberg", description="Lego Movie Staut of Liberty set", picture_path="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCINScNI7OOPG9pa_equA3nTrLbYGfdkZQng&usqp=CAU", user_id=3)
    db.session.add_all([lego1, lego2, lego3, lego4, lego5])
    db.session.commit()

    comment1 = Comment(comment="Cool set!", user_id=1, lego_id=5)
    comment2 = Comment(comment="I like that lego guy", user_id=2, lego_id=4)
    db.session.add_all([comment1, comment2])
    db.session.commit()

    wishlist1 = Wishlist(user_id=1, lego_id=5)
    wishlist2 = Wishlist(user_id=2, lego_id=1)
    db.session.add_all([wishlist1, wishlist2])
    db.session.commit()