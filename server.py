from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from forms import LoginForm, LegoForm
import crud
from models import db, connect_to_db, User, Collection, Lego, Comment, Wishlist

# Do I need to import this?

app = Flask(__name__)
app.secret_key = "secret_pass"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/")
# @login_required
def homepage():
    legos = Lego.query.all()
    return render_template("homepage.html",legos=legos)

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                # I think this might be wrong
                login_user(user)
                return redirect(url_for("homepage"))
        return "Incorrect credentials"
    return render_template("login.html", login_form=login_form)
    # Could add flash messages

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/collections")
@login_required
def all_collections():
    collections = crud.get_collections_by_user(current_user.user_id)
    # Need to edit to single user?

    return render_template("all_collections.html", collections=collections)

@app.route("/collections/<c_id>")
# @login_required
def collection(c_id):
    legos = crud.get_legos_by_collection(c_id=c_id)
    return render_template("collection_details.html", legos=legos)

# @app.route("/add", methods=["GET", "POST"])
# # @login_required
# def add_legos():
#         # Why isn't this working?
#     # if request.method == "POST":
#     #     return redirect("/")
#     # else:
#         return render_template("add.html")

@app.route("/wishlist")
@login_required
def wishlist():
    wishlists = current_user.wishlists
    return render_template("wishlist.html", wishlists=wishlists)

@app.route("/add", methods=["GET", "POST"])
def add_lego():
    lego_form = LegoForm()

    if lego_form.validate_on_submit():
        l_title = lego_form.l_title.data
        description = lego_form.description.data
        picture_path = lego_form.picture_path.data
        instructions_url = lego_form.instructions_url.data

        new_lego = Lego(l_title=l_title, description=description, picture_path=picture_path, instructions_url=instructions_url)

        db.session.add(new_lego)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("add.html", lego_form=lego_form)
 
#  Update request to database
@app.route("/lego_set/<lego_id>", methods=["GET", "POST"])
def lego_set(lego_id):
    lego = Lego.query.filter_by(lego_id=lego_id).first()
    return render_template("lego_set.html", lego=lego)

@app.route("/all_legos")
def all_legos():
    user = current_user
    legos = crud.get_legos_by_user(current_user.user_id)
    return render_template("all_legos.html", user=user, legos=legos)

@app.route("/update_lego/<lego_id>", methods=["GET", "POST"])
def update_lego(lego_id):
    lego = Lego.query.get(lego_id)
    lego_form = LegoForm(obj=lego)

    if lego_form.validate_on_submit():
        lego.l_title = lego_form.l_title.data
        lego.description = lego_form.description.data
        lego.picture_path = lego_form.picture_path.data
        lego.instructions_url = lego_form.instructions_url.data

        db.session.commit()
        return redirect(f"/lego_set/{lego_id}")
    else:
        return render_template("update.html", lego_form=lego_form, lego_id=lego_id)

@app.route("/delete_lego/<lego_id>", methods =["GET", "POST"])
def delete_lego(lego_id):
    lego = Lego.query.get(lego_id)
    c_id = lego.c_id
    for wishlist in lego.wishlists:
        db.session.delete(wishlist)
    db.session.delete(lego)
    db.session.commit()
    return redirect(f"/collections/{c_id}")

@app.route("/add_to_wishlist/<lego_id>", methods = ["GET", "POST"])
def add_wishlist(lego_id):
    lego = Lego.query.get(lego_id)
    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)