from fabric.api import local
from fabric.utils import abort
import os.path

html_files = ["home.html", "signup.html"]

def static_analyzer():
	'''Runs Pylint analyzer'''
	local("pylint server.py")

def init_server():
	'''Initializes the database'''
	local("export FLASK_APP=server.py")
	local("flask initdb")

def run_server():
	'''Runs the application'''
	verify_files()
	local("flask run")

def verify_files():
    '''test that all html files used in app.py exist in templates folder'''
    for file in html_files:
    	file_path = "templates/" + file
        if (not os.path.isfile(file_path)):
    	    abort("No file %s found in /templates/" % file)