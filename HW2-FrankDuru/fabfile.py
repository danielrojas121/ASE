from fabric.api import local

def prepare_deploy():
	pylint_check()
	run_app()

def pylint_check():
	local("pylint app.py")

def run_app():
	local("python app.py")

# PASS STATIC ANALYSIS, TEST CASES, AND OTHER CALLS HERE

''' 
Possible test cases:

- Check DB connection
- 

'''