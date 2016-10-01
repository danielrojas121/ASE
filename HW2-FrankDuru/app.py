from flask import Flask, request, render_template

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

@app.route("/")
def home():
	return render_template("home.html")

if __name__ == "__main__":
    app.run()