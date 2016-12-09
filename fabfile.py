'''These modules used to check system and run application'''
import platform
from fabric.api import local, shell_env

def prepare_deploy():
    '''Run all tests, initialize server and db, and run app'''
    clean()
    static_analyzer()
    init_database()
    run_tests()
    report_test_coverage()
    run_server()

def quick_deploy():
    '''No static analysis or test; only use for repeated debugging'''
    clean()
    init_database()
    run_server()

def static_analyzer():
    '''Runs Pylint analyzer'''
    local("pylint app.py")
    local("pylint custom_json_encoder.py")
    local("pylint user.py")
    local("pylint account.py")
    local("pylint transaction.py")

def run_tests():
    '''Perform tests here'''
    local("sqlite3 < dbtest.txt")
    local("pytest")

def report_test_coverage():
    '''Run coverage on our test suite'''
    local("coverage run test_app.py")
    local("coverage report")

def init_database():
    '''Initializes the server'''
    if platform.system() == 'Windows':
        print("Must call command 'export FLASK_APP=app.py' before first run")
        local('flask initdb')
    else:
        with shell_env(FLASK_APP='app.py'):
            local('flask initdb')

def run_server():
    '''Runs the application w/o reinitializing the database'''
    if platform.system() == 'Windows':
        local('flask run')
    else:
        with shell_env(FLASK_APP='app.py'):
            local('flask run')

def clean():
    '''Remove all pyc files from current directory'''
    local("find . -name \*.pyc -delete")
