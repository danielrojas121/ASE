from fabric.api import local

def static_analyzer():
	local("pylint app.py")

def init_server():
	local("export FLASK_APP=app.py")
	local("flask initdb")

def run_server():
	local("flask run")
