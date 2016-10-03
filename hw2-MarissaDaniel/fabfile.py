from fabric.api import local

def build_file():
	static_analyzer()
	run_server()


def run_server():
	local("python server.py")

def static_analyzer():
	local("pylint server.py")