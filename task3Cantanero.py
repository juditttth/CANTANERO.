class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        """Initialize the bank account with account number, owner, and balance."""
        if not account_number or not owner:
            raise ValueError("Account number and owner cannot be empty.")
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₱{amount:.2f}. New balance: ₱{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₱{amount:.2f}. New balance: ₱{self.balance:.2f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        """Display the current account balance."""
        print(f"Account balance: ₱{self.balance:.2f}")


account = BankAccount(account_number="09632800175", owner="Irene", balance=7000)


account.deposit(1000)  
account.withdraw(5000)  
account.display_balance()  