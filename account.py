'''Account Class for bank accounts in Vanmo app'''

class Account(object):

    def __init__(self, account_id, account_name, username, account_type, balance):
        self.__account_id = account_id
        self.__account_name = account_name
        self.__username = username
        self.__account_type = account_type
        self.__balance = balance

        def getAccountId(self):
        	return self.__account_id

        def getAccountName(self):
        	return self.__account_name

        def getUsername(self):
        	return self.__username

        def getAccountType(self):
        	return self.__account_type

        def getBalance(self):
        	return self.__balance

        def setBalance(self, newBalance):
        	self.__balance = newBalance