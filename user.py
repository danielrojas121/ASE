"""User Class for Vanmo app"""
#from account import Account

class User(object):
    """User class to store and manipulate user data in a session"""
    def __init__(self, user_id, username):
        self.__user_id = user_id
        self.__username = username
        self.__accounts = [] #list to keep track of this user's accounts
        self.__transactions = [] #list to keep track of this user's transactions

    def get_user_id(self):
        """return user id"""
        return self.__user_id

    def get_username(self):
        """return username"""
        return self.__username

    def get_accounts(self):
        """return list of accounts"""
        return self.__accounts

    def get_transactions(self):
        """return list of transactions"""
        return self.__transactions

    def add_account(self, account_object):
        """add a new account to list of accounts"""
        self.__accounts.append(account_object)

    def add_transaction(self, t_object, update_accounts=True):
        """add a new transaction object to list of transactions"""
        self.__transactions.append(t_object)

        if update_accounts:
            account_from = t_object.get_account_1()
            account_to = t_object.get_account_1()
            amount = float(t_object.get_amount())
            t_type = t_object.get_transaction_type()

            if t_type == "Transfer" or t_type == "Payment" or t_type == "Purchase":
                self.update_account_balance(account_from, amount, "Withdraw")
                self.update_account_balance(account_to, amount, "Deposit")
            else:
                self.update_account_balance(account_from, amount, t_type)

    def update_account_balance(self, account_name, transaction_amount, transaction_type):
        """update a specified account's balance after a transactions"""
        i = 0
        found = False
        while not found and i < len(self.__accounts):
            account = self.__accounts[i]
            if account.get_account_name() == account_name:
                found = True
                if transaction_type == "Withdraw":
                    account.withdraw(transaction_amount)
                elif transaction_type == "Deposit":
                    account.deposit(transaction_amount)
            i += 1

    def __repr__(self):
        """pretty print user object"""
        return "[id:%s username:%s accounts:%s transactions:%s]" % (self.__user_id,
                                                                    self.__username,
                                                                    self.__accounts,
                                                                    self.__transactions)
