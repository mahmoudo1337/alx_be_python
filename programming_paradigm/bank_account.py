class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    
    
    def deposit(amount):
        print(f"Deposited: ${self.account_balance + amount}")
    
    def withdraw(amount):
        if self.account_balance < amount:
            print("Insufficient Funds")
        print(f"Withdrew: ${self.account_balance - amount}")
        
    def display_balance():
        print(f"Current Balance: {self.account_balance}")