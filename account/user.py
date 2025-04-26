import re

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self): 
        return sum(acc.get_balance() for acc in self.accounts)

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return "Account removed."
        return "Account not found."

    def is_valid_email(self, email):
        # Simple email regex pattern
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance()}"
