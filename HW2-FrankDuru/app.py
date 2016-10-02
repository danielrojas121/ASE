from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'frankcabada'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Fc182641!'
app.config['MYSQL_DATABASE_DB'] = 'Vanmo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def home():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT VERSION()")
	data = cursor.fetchone()
	conn.close()
	return "Database version : %s " % data
	#return render_template("index.html")

if __name__ == "__main__":
    app.run()

