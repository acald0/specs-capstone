from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from forms import LoginForm
import crud
from models import db, connect_to_db, User, Category, Lego, Comment, Wishlist

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
    users = crud.get_users()
    return render_template("homepage.html", users=users)

@app.route("/login", methods=["POST"])
def login():
    login_form = LoginForm()
    username = login_form.username.data
    password = login_form.password.data

    user = User.query.filter_by(username=username).first()
    if user:
        if user.password == password:
            # I think this might be wrong
            login_user(user)
            return redirect(url_for("homepage"))
    return "Incorrect credentials"
    # Could add flash messages

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/collections")
# @login_required
def all_collections():
    return render_template("all_collections.html")

@app.route("/collections/<c_id>")
# @login_required
def collection():
    pass

@app.route("/add", methods=["POST"])
# @login_required
def add_legos():
    pass

@app.route("/wishlist")
# @login_required
def wishlist():
    pass
 

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)