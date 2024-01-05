from models import db, User, Collection, Lego, Comment, Wishlist, connect_to_db


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


def create_collection(c_title, user_id):
    collection = Collection(c_title=c_title,user_id=user_id)

    return collection

def get_collections():
    return Collection.query.all()

def get_collections_by_user(user_id):
    return Collection.query.filter_by(user_id=user_id).all()

def get_collection_by_id(c_id):
    collection = Collection.query.get(c_id)
    return collection

def get_legos_by_collection(c_id):
    legos = Lego.query.filter_by(c_id=c_id).all()
    return legos

def create_lego(l_title,description,picture_path, instructions_url, user_id, c_id):
    lego = Lego(l_title=l_title, description=description, picture_path=picture_path, instructions_url=instructions_url,user_id=user_id, c_id=c_id)

    return lego

def get_lego_by_id(lego_id):
    lego = Lego.query.get(lego_id).first()
    return lego

def get_legos_by_user(user_id):
    legos = Lego.query.filter_by(user_id=user_id).all()
    return legos

def get_legos_by_wishlist(w_id):
    legos = Lego.query.filter_by(w_id=w_id).all()
    return legos

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