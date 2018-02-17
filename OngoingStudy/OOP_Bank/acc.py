class Account:
# This class creates a bank account object
# This is a generic class since there are few bank account types. Then, we are using inheritence.
# The Account is a base class
# Terminology:
# Class - the blueprint; Object instance - instantiation of the class.

# Instance Variable - self.X - Variables that are defined by the class and accessible
# by the instance.

# Class Variable - decleared outside the method, shared by all instances of the class.
# all instances of the class have the *same* class variable! Those are rarely used

# Doc strings - """ - Class documentation """ - refer to as instance.__doc__

# Data member - class variable / instance variable (another concept)

# C'tor - __init__ function

# Class method - another method

# instantiation - e.g. checking = Checking("acc.txt", 1)

# inheritence - a sub class out of a base class. The sub class has the base class methods + attrs + it's own.

# Attributes - type for example

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as  file:
            self.balance = int(file.read())
            #balance - instance variable
            #self - object

    def withraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as  file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking account instances """
    type = "checking"
    # Checking = Account + other stuff - this is the syntax for inheritence
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking("balance.txt", 1)
checking.transfer(5)
checking.commit()
print(checking.balance)
print(checking.__doc__)
# Testing
# account = Account("balance.txt")
# print(account.balance)
# account.withraw(200)
# account.commit()
# print(account.balance)
# account.deposit(500)
# print(account.balance)
# account.commit()
