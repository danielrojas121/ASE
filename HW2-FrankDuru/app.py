''' Using Flask framework '''
from flask import Flask, render_template
from flaskext.mysql import MySQL

APP = Flask(__name__)
APP.config["DEBUG"] = True  # Only include this while you are testing your app
MYSQL = MySQL()

# MySQL configurations
APP.config['MYSQL_DATABASE_USER'] = 'frankcabada'
APP.config['MYSQL_DATABASE_PASSWORD'] = 'Fc182641!'
APP.config['MYSQL_DATABASE_DB'] = 'Vanmo'
APP.config['MYSQL_DATABASE_HOST'] = 'localhost'
MYSQL.init_app(APP)

CONN = MYSQL.connect()
CURSOR = CONN.cursor()

@APP.route("/")
def home():
    ''' function called on landing page '''
    #cursor.execute("SELECT VERSION()")
    #data = cursor.fetchone()
    #return "Database version : %s " % data
    return render_template("index.html")

@APP.teardown_appcontext
def close_connection(error):
    ''' function called on termination of app.py '''
    if hasattr(CONN, 'connection'):
        CONN.close()
    return error

if __name__ == "__main__":
    APP.run()
