'''Account Class for bank accounts in Vanmo app'''

class Account(object):

    def __init__(self, account_name, username, account_type, balance):
        self.account_name = account_name
        self.username = username
        self.account_type = account_type
        self.balance = balance
