class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)


account = BankAccount("Jagannath", 5000)
account.deposit(2000)
account.withdraw(1500)
account.display()
