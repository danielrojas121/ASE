# content of test_sample.py
import pytest

'''Various test get methods on app routes'''
def test_get_home_OK(client):
	assert client.get('/').status_code == 200

def test_get_signup_OK(client):
	assert client.get('/signup').status_code == 200

def test_get_view_account_redirect(client):
	assert client.get('/view_current_account').status_code == 302

def test_get_add_account_redirect(client):
	assert client.get('/add_bank_account').status_code == 302

'''Login post tests'''
def test_post_login_bad_request(client):
	assert client.post('/login').status_code == 400

def test_bad_login(client):
	assert client.post('/login', data=dict(usr = 'martychavezgarzamcfly', pwd = 'dog')).status_code == 200 #? 302
	assert client.get('/view_current_account').status_code == 302

def test_good_login(client):
	assert client.post('/signup', data=dict(username = 'testinglogin', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testinglogin', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200

'''Login empty fields tests'''
def test_login_empty_usr(client):
	assert client.post('/login', data=dict(usr = '', pwd = 'themostsecure')).status_code == 200 #? 302
	assert client.get('/view_current_account').status_code == 302

def test_login_empty_pass(client):
	assert client.post('/login', data=dict(usr = 'daniel', pwd = '')).status_code == 200 #? 302
	assert client.get('/view_current_account').status_code == 302

def test_login_empty(client):
	assert client.post('/login', data=dict(usr = '', pwd = '')).status_code == 200 #? 302
	assert client.get('/view_current_account').status_code == 302

'''Signup empty bad request test'''
def test_signup_empty_bad_request(client):
	assert client.post('/signup', data=dict(usr = '', pwd = '')).status_code == 400
	assert client.get('/view_current_account').status_code == 302

def test_signup_empty_usr(client):
	assert client.post('/signup', data=dict(username = '', password = 'test')).status_code == 302

def test_signup_empty_pass(client):
	assert client.post('/signup', data=dict(username = 'Michael', password = '')).status_code == 302

'''Signup duplicate username'''
def test_duplicate_signup(client):
	assert client.post('/signup', data=dict(username = 'testinglogin', password = 'test')).status_code == 302
	assert client.post('/signup', data=dict(username = 'testinglogin', password = 'test')).status_code == 302
	#assert client.post('/login', data=dict(usr = 'testinglogin', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 302

'''Account tests'''
def test_add_account(client):
	assert client.post('/signup', data=dict(username = 'testingaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingaccount', account_name= 'Chase', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.get('/view_current_account').status_code == 200

def test_add_bad_account(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking')).status_code == 400
	

