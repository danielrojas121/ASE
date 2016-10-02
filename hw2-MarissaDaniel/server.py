import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, render_template, request, g, flash

app = Flask(__name__)
app.config.from_object(__name__)
app.config["DEBUG"] = True  # Only  include this while you are testing your app

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'vanmo.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/signup") 
def signup():
	return render_template("signup.html")

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into logins (username, password) values (?, ?)',
                 [request.form['username'], request.form['password']])
    db.commit()
    flash('New entry was successfully posted')
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
