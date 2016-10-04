from fabric.api import local

def run_server():
	local("export FLASK_APP=server.py")
	local("flask initdb")
	local("flask run")

def static_analyzer():
	local("pylint server.py")