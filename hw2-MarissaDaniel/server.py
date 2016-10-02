from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True  # Only  include this while you are testing your app

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/signup")
def signup():
	return render_template("signup.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
