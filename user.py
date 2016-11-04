'''User Class for Vanmo app'''
from account import Account

class User(object):

    def __init__(self, user_id, username, password):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__accounts = [] #list to keep track of this user's accounts

    def getUserId(self):
        return self.__user_id

    def getUserName(self):
        return self.__username

    def getAccounts(self):
        return self.__acounts

    def addAccount(self, account_object):
        self.__accounts.append(account_object)