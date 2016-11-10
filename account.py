"""Account Class for bank accounts in Vanmo app"""

class Account(object):
    """Account class to store and manipulate account data"""
    def __init__(self, account_name, account_type, username):
        """initialize account object with provided parameters"""
        self.__account_name = account_name
        self.__account_type = account_type
        self.__username = username
        self.__balance = 0.00

    def get_account_name(self):
        """return account name"""
        return self.__account_name

    def get_account_type(self):
        """return type of account (CHECKING/SAVINGS)"""
        return self.__account_type

    def get_username(self):
        """return associated user's username"""
        return self.__username

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

    def __repr__(self):
        """pretty print account object"""
        return "[account:%s type:%s user:%s balance:%s]" % (self.__account_name,
                                                            self.__account_type,
                                                            self.__username,
                                                            str(self.__balance))
