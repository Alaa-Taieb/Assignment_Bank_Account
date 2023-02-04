class BankAccount:
    bank_accounts = []
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bank_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all(cls):
        for account in cls.bank_accounts:
            account.display_account_info()
    

account_1 = BankAccount(0.02, 300)
account_2 = BankAccount(0.03, 250)

account_1.deposit(50).deposit(35).deposit(175).withdraw(10).yield_interest().display_account_info()
account_2.deposit(75).deposit(135).withdraw(25).withdraw(35).yield_interest().display_account_info()

BankAccount.print_all()