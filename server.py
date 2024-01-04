from flask import Flask, render_template
import crud
from models import connect_to_db

app = Flask(__name__)
app.secret_key = "secret_pass"

@app.route("/")
def homepage():
    users = crud.get_users()
    return render_template("homepage.html", users=users)

@app.route("/login")
def login():
    pass

@app.route("/collections")
def all_collections():
    return render_template("all_collections.html")

@app.route("/collections/<c_id>")
def collection():
    pass

@app.route("/add")
def add_legos():
    pass

@app.route("/wishlist")
def wishlist():
    pass
 

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)