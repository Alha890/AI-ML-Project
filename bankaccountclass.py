class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")
    def check_balance(self):
        print("Current Balance:", self.balance)
account = BankAccount()
account.deposit(5000)
account.withdraw(2000)
account.check_balance()