"""
    Server
    Marisssa Ojeda
    Daniel Rojas
    Frank Cabada
    Duru Kahyaoglu
"""
import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, render_template, request, g, redirect

APP = Flask(__name__)
APP.config.from_object(__name__)
APP.config["DEBUG"] = True  # Only  include this while you are testing your APP

APP.config.update(dict(
    DATABASE=os.path.join(APP.root_path, 'vanmo.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
APP.config.from_envvar('FLASKR_SETTINGS', silent=True)

@APP.route("/")
def home():
    """Home page showing usernames and passwords."""
    sql_db = get_db()
    cur = sql_db.execute('select username, password from logins order by id asc')
    logins = cur.fetchall()
    return render_template("home.html", logins=logins)

@APP.route("/signup", methods=["POST", "GET"])
def signup():
    """Signup page where people can add username and password."""
    if request.method == "POST":
        sql_db = get_db()
        sql_db.execute('insert into logins (username, password) values (?, ?)',
                       [request.form['username'], request.form['password']])
        sql_db.commit()
        return redirect("/")
    else:
        return render_template("signup.html")

# EDIT THIS SO THAT CAN ONLY ACCESS WHEN USER IS SIGNED IN
@APP.route("/add_bank_account", methods=["POST", "GET"])
def add_bank_account():
    """Page to redirect to when user chooses to create new bank accounts"""
    if request.method == "POST":
        sql_db = get_db()
        sql_db.execute('insert into accounts (accountname, type, balance) values (?, ?, ?)', [request.form['accountname'], request.form['type'], request.form['balance']])
        sql_db.commit()
        cur = sql_db.execute('select * from accounts')
        accounts = cur.fetchall()
        return render_template("add_bank_account.html", accounts=accounts)
    else:
        sql_db = get_db()
        cur = sql_db.execute('select * from accounts')
        accounts = cur.fetchall()
        return render_template("add_bank_account.html", accounts=accounts)

@APP.route("/view_current_account", methods=["POST", "GET"])
def view_current_account():
    """Page to redirect to when user chooses to create new bank accounts"""
    return render_template("view_current_account.html")

def connect_db():
    """Connects to the specific database."""
    db_rv = sqlite3.connect(APP.config['DATABASE'])
    db_rv.row_factory = sqlite3.Row
    return db_rv

def init_db():
    """Initializes sql_db"""
    sql_db = get_db()
    with APP.open_resource('schema.sql', mode='r') as db_file:
        sql_db.cursor().executescript(db_file.read())
    sql_db.commit()

@APP.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

def get_db():
    """Opens a new database connection if there is none yet for the
    current APPlication context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@APP.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
    else:
        print error

if __name__ == "__main__":
    APP.run(host="0.0.0.0")
