from fabric.api import local
import platform

def prepare_deploy():
	static_analyzer()
	init_server()
	run_server()

def static_analyzer():
	local("pylint app.py")

def init_server():
	if (platform.system() == 'Windows'):
		windows_init()
	else:
		default_init()
	local("flask initdb")

def default_init():
	local("export FLASK_APP=app.py")

def windows_init():
	local("set FLASK_APP=app.py")

def run_server():
	local("flask run")
