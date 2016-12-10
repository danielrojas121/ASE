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

def test_add_bad_account_negative_dollar(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking', dollars=-100, cents=45)).status_code == 302

def test_add_bad_account_negative_cent(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking', dollars=100, cents=-45)).status_code == 302

def test_add_bad_account_morethan_twodecimal_cent(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking', dollars=100, cents=450)).status_code == 302

def test_add_bad_account_overflow_dollar(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking', dollars=100000000, cents=45)).status_code == 302
'''
def test_add_bad_account_dirtydollar(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 200
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking', dollars='eeee', cents=45)).status_code == 302
'''
def test_add_bad_account_duplicateaccount(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking', dollars=100, cents=45)).status_code == 302

'''Transfer tests'''
def test_transfer(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'Saving', account_name2= 'Checking', dollars=50, cents=45)).status_code == 302

def test_transfer_negative_dollar(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'Saving', account_name2= 'Checking', dollars=-50, cents=45)).status_code == 302

def test_transfer_negative_cents(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'Saving', account_name2= 'Checking', dollars=50, cents=-45)).status_code == 302

def test_transfer_negative_dollar_cents(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'Saving', account_name2= 'Checking', dollars=-50, cents=-45)).status_code == 302

def test_transfer_more_than_two_decimals(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'Saving', account_name2= 'Checking', dollars=50, cents=123)).status_code == 302

def test_transfer_more_than_max(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'Saving', account_name2= 'Checking', dollars=50000000000, cents=12)).status_code == 200

def test_transfer_wrong_account1(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'None', account_name2= 'Checking', dollars=50, cents=12)).status_code == 200

def test_transfer_wrong_account2(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'Saving', account_name2= 'None', dollars=50, cents=12)).status_code == 200

def test_transfer_wrong_account12(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Saving', account_type='Saving', dollars=200, cents=45)).status_code == 302
	assert client.post('/transfer', data=dict(username= 'testingbadaccount', account_name1= 'No', account_name2= 'None', dollars=50, cents=12)).status_code == 200

'''Deposit test'''
def test_deposit(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/deposit', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=50, cents=45)).status_code == 302

def test_deposit_negative_dollar(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/deposit', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=-50, cents=45)).status_code == 302

def test_deposit_negative_cents(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/deposit', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=50, cents=-45)).status_code == 302

def test_deposit_negative_dollar_cents(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/deposit', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=-50, cents=-45)).status_code == 302

def test_deposit_more_than_2_decimals(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/deposit', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=50, cents=145)).status_code == 302

def test_deposit_more_than_max(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/deposit', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=50000000000000, cents=45)).status_code == 302

def test_deposit_wrong_account(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/deposit', data=dict(username= 'testingbadaccount', account_name= 'None', dollars=50, cents=45)).status_code == 200

'''Withdraw test'''
def test_withdraw(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/withdraw', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=50, cents=45)).status_code == 302

def test_withdraw_negative_dollar(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/withdraw', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=-50, cents=45)).status_code == 302

def test_withdraw_negative_cent(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/withdraw', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=50, cents=-45)).status_code == 302

def test_withdraw_negative_dollar_cent(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/withdraw', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=-50, cents=-45)).status_code == 302

def test_withdraw_more_than_2_decimals(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/withdraw', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=50, cents=145)).status_code == 302

def test_withdraw_more_than_max(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/withdraw', data=dict(username= 'testingbadaccount', account_name= 'Checking', dollars=50000000000000000, cents=45)).status_code == 200

def test_withdraw_wrong_account(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/withdraw', data=dict(username= 'testingbadaccount', account_name= '1', dollars=50, cents=45)).status_code == 200

'''Make Purchase Test'''
def test_purchase(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/purchase', data=dict(username= 'testingbadaccount', account_name= 'Checking', store_name= 'Academy', item_name='thermals', dollars=50, cents=45)).status_code == 302

def test_purchase_negative_dollar(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/purchase', data=dict(username= 'testingbadaccount', account_name= 'Checking', store_name= 'Academy', item_name='thermals', dollars=-50, cents=45)).status_code == 302

def test_purchase_negative_cent(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/purchase', data=dict(username= 'testingbadaccount', account_name= 'Checking', store_name= 'Academy', item_name='thermals', dollars=50, cents=-45)).status_code == 302

def test_purchase_negative_dollar_cent(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/purchase', data=dict(username= 'testingbadaccount', account_name= 'Checking', store_name= 'Academy', item_name='thermals', dollars=-50, cents=-45)).status_code == 302

def test_purhcase_more_than_2_decimals(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/purchase', data=dict(username= 'testingbadaccount', account_name= 'Checking', store_name= 'Academy', item_name='thermals', dollars=50, cents=145)).status_code == 302

def test_purchase_more_than_max(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/purchase', data=dict(username= 'testingbadaccount', account_name= 'Checking', store_name= 'Academy', item_name='thermals', dollars=50000000000000000, cents=45)).status_code == 200

def test_purchase_wrong_account(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Checking', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/purchase', data=dict(username= 'testingbadaccount', account_name= '1', store_name= 'Academy', item_name='thermals', dollars=50, cents=45)).status_code == 200

'''Send Money Test'''
def test_sendmoney_nosending_account(client):
	assert client.post('/signup', data=dict(username = 'testingbadaccount', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount', account_name= 'Chase', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.get('/logout').status_code == 302
	assert client.post('/signup', data=dict(username = 'testingbadaccount1', password = 'test')).status_code == 302
	assert client.post('/login', data=dict(usr = 'testingbadaccount1', pwd = 'test')).status_code == 302
	assert client.get('/view_current_account').status_code == 200
	assert client.post('/add_bank_account', data=dict(username= 'testingbadaccount2', account_name= 'Chase2', account_type='Checking', dollars=100, cents=45)).status_code == 302
	assert client.post('/sendmoney', data=dict(accountname_1= 'Chasebad', username2= 'testingbadaccount', accountname_2='Chase', dollars=100, cents=45)).status_code == 400



