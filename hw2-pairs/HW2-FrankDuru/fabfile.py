from fabric.api import local
from fabric.utils import abort
import os.path

# Must update this list when creating new HTML files
html_files = ["index.html", "signup.html", "home.html"]

def prepare_deploy():
    pylint_check()
    verify_html_files()
    start_app()

def pylint_check():
    '''pass static analysis'''
    local("pylint app.py")

def start_app():
    '''run web app'''
    local("python app.py")

def verify_html_files():
    '''test that all html files used in app.py exist in templates folder'''
    for file in html_files:
    	file_path = "templates/" + file
        if (not os.path.isfile(file_path)):
    	    abort("No file %s found in /templates/" % file)