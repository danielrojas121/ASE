from fabric.api import local

def static_analyzer():
	local("pylint server.py")

def init_server():
	local("export FLASK_APP=server.py")
	local("flask initdb")
	local("flask run")

def run_server():
	local("flask run")
