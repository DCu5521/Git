class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        return self.balance

    def withdraw_money(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

# create an instance of the Wallet class
my_wallet = Wallet()

# add money to the wallet
my_wallet.add_money(11040455)
# check the balance
print(my_wallet.balance) # prints amount specified

# withdraw money from the wallet
my_wallet.withdraw_money(204653)
# check the balance
print(my_wallet.balance) # prints amount specified
