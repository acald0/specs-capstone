from flask import Flask

app = Flask(__name__)
app.secret_key = "secret_pass"

@app.route("/")
def homepage():
    pass

@app.route("/login")
def login():
    pass

@app.route("/collections")
def all_collections():
    pass

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
    app.run(debug=True)