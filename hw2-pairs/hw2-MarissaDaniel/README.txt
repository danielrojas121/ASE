Practice with Development Technologies: Homework 2

For this assignment, we deviated a bit from what we described in our team’s project proposal. Initially intending to use Java as our programming language, this has since changed to Python. Our database has also changed to SQLite while the other pair of our team is using MySQL. This will help us determine which database will be better for our project. This modification will be represented in our team’s revised project proposal.

GitHub Repository:
Our repository is located at the following URL:
https://github.com/dhr2119/ASE.git
This is our team’s shared project repository. Within this, our team created two directories for each of the pairs. Our files are located in ASE/hw2-pairs/hw2-MarissaDaniel

Toy System:
For this system, we are using Python and a framework called Flask. Flask will enable us to easily build a web interface for our project. Along with this, we are using SQLite as our database for persistent data storage.

The main objectives for us were a few things: environment setup with Python/Flask, have a working HTML webpage, and connect a database to persist data to using the webpage.

Environment setup consisted of installing ‘pip’ which is a Python package manager and enables installation of Flask. Along with these main components, installation is also required for Pylint and Fabric.

Our system begins at a welcome page. To demonstrate persistent data storage, this welcome page also lists the contents of the database which is populated through the signup page. The signup page allows a user to create a username and password. The user is then redirected back to the welcome page to display the contents of the database. The database is able to keep the information stored between separate executions of server.py which is executed by running ‘fab run_server’ (explained in the next section).
The application will be started on port 5000 and you can navigate your internet browser to ‘localhost:5000’.

Running the System:
We chose to use Fabric to organize a script file called fabfile.py. This file is used to run a series of commands.
‘fab static_analysis’ will use the Pylint static analyzer to analyze our server.py file.
To run the system, use the following two commands:
‘fab init_server’ will export certain variables and initialize the database in preparation to run the server.
‘fab run_server’ will execute and run the server. This is the command that will be used whenever you would like to rerun the web server.
Static Analysis:
For static analysis we are using Pylint. Pylint checks for errors and code smells. To analyze a file simply type ‘pylint [file]’ (or use ‘fab static_analysis’ as explained above) and it will output the results. This analyzer helped us identify some areas of code which could be improved upon.

Challenges:
Initially, there was a little difficulty setting up pip and using pip to install Flask. This had to do with differing Python versions, but took a short time to solve.

Test Cases:
We have an automated test that checks if the proper HTML files exist when running the server. This is important so the user doesn’t come across an error when trying to access a certain web page.
Also, the way we designed the system is similar to a test itself to show persistent data storage. A user can signup with a username and password and the contents of the database will be listed on the welcome page. This proves that this data is being persisted to the database can be retrieved and displayed on a webpage. This can be tested by you.
As of now, users are able to signup using an already existing username, but we will work to improve this. Users should not be able to create a new username that is already being currently used.

Outcome:
We feel that this was a very productive and key assignment. It has allowed us to go through the setup process using our chosen technologies and begin to understand what works and what does not work. We feel Python and Flask will work well for our project. We will be collaborating with our team members to decide which database will work best for our needs.
