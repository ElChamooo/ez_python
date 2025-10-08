import secrets

class BankAccount:
    # Class variable
    bank_name = "EZPython Bank"
    accounts_by_iban = {}  # registry IBAN -> account

    def __init__(self, owner, balance=0):
        # Instance variables
        self.owner = owner
        self.balance = balance

        # Always generate a random, unique 16-digit numeric IBAN (cannot be provided)
        while True:
            candidate = ''.join(secrets.choice('0123456789') for _ in range(16))
            if candidate not in BankAccount.accounts_by_iban:
                self.IBAN = candidate
                break

        # register account
        BankAccount.accounts_by_iban[self.IBAN] = self

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance} (IBAN: {self.IBAN})")

    def transfer(self, target_iban, amount):
        """
        Transfer amount to another account identified by its IBAN.
        """
        if not (isinstance(target_iban, str) and target_iban.isdigit() and len(target_iban) == 16):
            print("Target IBAN must be a 16-digit string.")
            return

        target = BankAccount.accounts_by_iban.get(target_iban)
        if target is None:
            print("No account found with the provided IBAN.")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient funds for transfer.")
            return

        # perform transfer
        self.balance -= amount
        target.balance += amount
        print(f"Transferred {amount} from {self.owner} (IBAN: {self.IBAN}) to {target.owner} (IBAN: {target.IBAN}).")
        print(f"New balance: {self.owner}: {self.balance}, {target.owner}: {target.balance}")


# Create two accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Perform transactions on account1
account1.show_balance()
account1.deposit(500)
account1.withdraw(300)
account1.show_balance()

# Perform transactions on account2
account2.show_balance()
account2.deposit(200)
account2.withdraw(100)
account2.show_balance()

# Transfer between accounts
account1.transfer(account2.IBAN, 200)
account1.show_balance()
account2.show_balance()