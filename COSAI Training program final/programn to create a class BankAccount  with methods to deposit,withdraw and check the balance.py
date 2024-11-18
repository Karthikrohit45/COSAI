class BankAccount:
    def __init__(self, initial_balance):
        """Initialize the account with an initial balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        """Check the current balance."""
        return self.balance


if __name__ == "__main__":
    account = BankAccount(1000)  
    
    account.deposit(500)         
    account.withdraw(300)         
    print("Final balance:", account.check_balance())  
