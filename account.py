"""Account Class for bank accounts in Vanmo app"""

class Account(object):
    """Account class to store and manipulate account data"""
    def __init__(self, account_id, account_name, username, account_type):
        """initialize account object with provided parameters"""
        self.__account_id = account_id
        self.__account_name = account_name
        self.__username = username
        self.__account_type = account_type
        self.__balance = 0

    def get_account_id(self):
        """return account id"""
        return self.__account_id

    def get_account_name(self):
        """return account name"""
        return self.__account_name

    def get_username(self):
        """return associated user's username"""
        return self.__username

    def get_account_type(self):
        """return type of account (CHECKING/SAVINGS)"""
        return self.__account_type

    def get_balance(self):
        """return account balance"""
        return self.__balance

    def deposit(self, amount):
        """add money into account balance"""
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """subtract money from account balance"""
        if amount > 0:
            self.__balance -= amount
