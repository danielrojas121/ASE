# content of test_sample.py
import pytest
from flask import session

def login():
	session['logged_in'] = True

def test_app(client):
	assert client.get('/view_current_account').status_code == 302
	#login()
	#assert client.get('/view_current_account').status_code == 200