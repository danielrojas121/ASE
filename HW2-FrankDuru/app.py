''' Using Flask framework '''
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

APP = Flask(__name__)
APP.config["DEBUG"] = True  # Only include this while you are testing your app
MYSQL = MySQL(APP)

# MySQL configurations
APP.config['MYSQL_DATABASE_USER'] = 'frankcabada'
APP.config['MYSQL_DATABASE_PASSWORD'] = 'Fc182641!'
APP.config['MYSQL_DATABASE_DB'] = 'Vanmo'
APP.config['MYSQL_DATABASE_HOST'] = '209.2.220.201'
MYSQL.init_app(APP)

CONN = MYSQL.connect()
CURSOR = CONN.cursor()

@APP.route("/")
def home():
    ''' load landing page '''
    #cursor.execute("SELECT VERSION()")
    #data = cursor.fetchone()
    #return "Database version : %s " % data
    return render_template("index.html")

@APP.route("/login", methods=['POST', 'GET'])
def login():
    ''' check database to verify user data and login if allowed '''
    #return render_template("home.html")
    username = request.form['usr']
    password = request.form['pwd']
    CURSOR.execute("""SELECT * from `user` WHERE `user_username`='%s' AND
    	`user_password`='%s'""" % (username, password))
    data = CURSOR.fetchone()
    if data is None:
        return "Wrong Input"
    else:
        return render_template("home.html")

@APP.route("/signup", methods=['POST', 'GET'])
def signup():
    ''' redirect user to sign up page to create an account '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            CURSOR.execute("""INSERT INTO `user` (`user_username`, `user_password`)
                VALUES ('%s', '%s')""" % (username, password))
            CONN.commit()
        except CONN.Error as error:
            print error
            CONN.rollback()
        return redirect("/")
    else:
        return render_template("signup.html")

@APP.teardown_appcontext
def close_connection(error):
    ''' function called on termination of app.py '''
    if hasattr(CONN, 'connection'):
        CONN.close()
    return error

if __name__ == "__main__":
    APP.run()
