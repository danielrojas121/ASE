"""User Class for Vanmo app"""
#from account import Account

class User(object):
    """User class to store and manipulate user data in a session"""
    def __init__(self, user_id, username):
        self.__user_id = user_id
        self.__username = username
        self.__accounts = [] #list to keep track of this user's accounts

    def get_user_id(self):
        """return user id"""
        return self.__user_id

    def get_username(self):
        """return username"""
        return self.__username

    def get_accounts(self):
        """return list of accounts"""
        return self.__accounts

    def add_account(self, account_object):
        """add a new account to list of accounts"""
        self.__accounts.append(account_object)

    def __repr__(self):
        """pretty print user object"""
        return "[id:%s username:%s accounts:%s]" % (self.__user_id, self.__username,
                                                    self.__accounts)
