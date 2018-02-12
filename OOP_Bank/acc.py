class Account:

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

account = Account("balance.txt")
print(account.balance)
account.withraw(200)
account.commit()
print(account.balance)
account.deposit(500)
print(account.balance)
account.commit()
