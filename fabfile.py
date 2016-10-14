from fabric.api import local, shell_env

def static_analyzer():
	'''Runs Pylint analyzer'''
	local("pylint app.py")

def init_server():
	'''Initializes the database'''
	with shell_env(FLASK_APP='app.py'):
		local("flask initdb")

def run_server():
	'''Runs the application'''
	with shell_env(FLASK_APP='app.py'):
		local("flask run")
