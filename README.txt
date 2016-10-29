##############################
# README.txt
# Columbia Coders
##############################


System overview
------------------------------------------------------------------------------
Running the System:
We use a fab file to automate running the system. Below are the supported commands

'fab static_analyzer' - Executes the pylint analyzer on app.py
'fab run_tests' - Executes the sqlite database tests
'fab prepare_deploy' - Runs static analyzer, tests, initalizes database and runs app.py
'fab quick_deploy' - Initializes database and runs app.py
'fab run_server' - Only runs app.py. Used when you want to run application without reinitalizing the database

Static Analysis:
For static analysis we are using Pylint. Pylint checks for errors and code smells. To analyze a file simply type ‘pylint [file]’ (or use ‘fab static_analysis’ as explained above) and it will output the results. This analyzer helps us identify some areas of code which could be improved upon.

Test Cases:
We have an automated test that check database integrity. Run this with 'fab run_tests'


Using the system
------------------------------------------------------------------------------
Login page:
The login page is where a user will be first directed. The user can type a username and password to login.
Login credentials can be created at the signup page which can be reached from the login page.

Signup page:
A user can create a username and password combination here. If a username has already been taken,
the system will indicate to the user to select another username.

Accounts page:
After login, the user can view his/her bank accounts and also choose to add a new bank account.
The user is also able to logout from this page.

Add account page:
The user can enter a name, type (checking/savings), and balance for a new account.