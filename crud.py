from models import db, User, Category, Lego, Comment, Wishlist, connect_to_db


def create_user(username, password):
    user = User(username=username, password=password)

    return user

def get_users():
    return User.query.all()

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user

def get_user_by_username(username):
    return User.query.filter(User.username == username).first()


def create_category(c_title, user_id):
    category = Category(c_title=c_title,user_id=user_id)

    return category

def get_categories():
    return Category.query.all()

def get_category_by_id(c_id):
    category = Category.query.get(c_id)
    return category

def create_lego(l_title,description,picture_path, instructions_url, user_id, c_id):
    lego = Lego(l_title=l_title, description=description, picture_path=picture_path, instructions_url=instructions_url,user_id=user_id, c_id=c_id)

    return lego

def get_lego_by_id(lego_id):
    lego = Lego.query.get(lego_id)
    return lego

def create_comment(comment, user_id, lego_id):
    new_comment = Comment(comment=comment, user_id=user_id, lego_id=lego_id)

    return new_comment

def get_comments_by_user(user_id):
    comment = Comment.query.get(user_id)
    return comment

def get_comments_by_lego(lego_id):
    comment = Comment.query.get(lego_id)
    return comment

def create_wishlist(user_id, lego_id):
    wishlist = Wishlist(user_id=user_id, lego_id=lego_id)
    return wishlist

def get_wishlist_by_user(user_id):
    wishlist = Wishlist.query.get(user_id)
    return wishlist

if __name__ == '__main__':
    from server import app
    connect_to_db(app)