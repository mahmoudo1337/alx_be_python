class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    
    
    def deposit(self, amount):
        return f"Deposited: ${self.account_balance + amount}"
    
    def withdraw(self, amount):
        if self.account_balance <= amount:
            return False
        else:
            return f"Withdrew: ${self.account_balance - amount}"
        
    def display_balance(self):
        print( f"Current Balance: ${self.account_balance:.2f}")