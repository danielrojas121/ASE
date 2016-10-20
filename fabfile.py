'''These modules used to check system and run application'''
import platform
from fabric.api import local, shell_env

def prepare_deploy():
    '''Run all tests, initialize server and db, and run app'''
    static_analyzer()
    init_server()
    run_server()

# ADD TESTS HERE
def static_analyzer():
    '''Runs Pylint analyzer'''
    #local("pylint fabfile.py")
    local("pylint app.py")

def init_server():
    '''Initializes the server'''
    if platform.system() == 'Windows':
        local('set FLASK_APP=app.py')
        local('flask initdb')
    else:
        with shell_env(FLASK_APP='app.py'):
            local('flask initdb')

def run_server():
    '''Runs the application'''
    if platform.system() == 'Windows':
        local('flask run')
    else:
        with shell_env(FLASK_APP='app.py'):
            local('flask run')
