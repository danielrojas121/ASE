"""Transactions Class for Vanmo app"""
#from account import Account

class Transaction(object):
    """Transaction class to store and manipulate transaction data in a session"""
    def __init__(self, time_stamp, account_1, account_2, amount, t_type): #pylint: disable=R0913
        self.__time_stamp = time_stamp
        self.__account_1 = account_1
        self.__account_2 = account_2
        self.__amount = amount
        self.__transaction_type = t_type

    def get_time_stamp(self):
        """return time stamp from initialization"""
        return self.__time_stamp

    def get_account_1(self):
        """return first account in transaction"""
        return self.__account_1

    def get_account_2(self):
        """return second account in transaction"""
        return self.__account_2

    def get_amount(self):
        """return amount of money in this transaction"""
        return self.__amount

    def get_transaction_type(self):
        """return the type of transaction"""
        return self.__transaction_type

    def __repr__(self):
        """pretty print transaction object"""
        return """[time_stamp:%s account_1:%s account_2:%s amount:%s
        type:%s]""" % (self.__time_stamp, self.__account_1, self.__account_2,
                       self.__amount, self.__transaction_type)
