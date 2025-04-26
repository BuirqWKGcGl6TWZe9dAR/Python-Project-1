from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount
import string

users = []

def create_user():
    name = input("Enter name: ")
    if name.isalpha():
        email = input("Enter email: ")
        user = User(name, email)
        if not user.is_valid_email(email):
            print("Invalid email address!")
            return  # Prevents user from being added with invalid email
        users.append(user)
        print(f"User {name} created.\n")
    else:
        print("Name must not contain digits or punctuations!")

def list_users():
    if not users:
        print("No users available.\n")
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    if not users:
        print("No users available. Please create a user first.\n")
        return  # ✅ Issue #1: Prevent proceeding without users

    list_users()
    try:
        idx = int(input("Select user number: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return

    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    try:
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))
    except ValueError:
        print("Invalid input.\n")
        return

    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)
    else:
        print("Invalid account type!")
        return

    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    if not users:
        print("No users available.\n")
        return

    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
    except ValueError:
        print("Invalid input.\n")
        return

    user = users[idx]
    if not user.accounts:
        print("This user has no accounts.\n")
        return

    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    try:
        acc_idx = int(input("Select account: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid account selection.\n")
            return
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid input.\n")
        return

    user.accounts[acc_idx].deposit(amount)
    print("Deposit successful.\n")

def withdraw_money():
    if not users:
        print("No users available.\n")
        return

    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
    except ValueError:
        print("Invalid input.\n")
        return

    user = users[idx]
    if not user.accounts:
        print("This user has no accounts.\n")
        return

    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    try:
        acc_idx = int(input("Select account: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid account selection.\n")
            return
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid input.\n")
        return

    try:
        user.accounts[acc_idx].withdraw(amount)
        print("Withdrawal successful.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    if not users:
        print("No users available.\n")
        return

    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return
    except ValueError:
        print("Invalid input.\n")
        return

    user = users[idx]
    if not user.accounts:
        print("This user has no accounts.\n")
        return

    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc.get_transaction_history():
            print(tx)

# Fix for Issue #2: Ensure balance consistency after multiple operations
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance
        self.transaction_history = []

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transaction_history.append(f"Deposited: Rs. {amount}")
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: Rs. {amount}")
        
    def get_transaction_history(self):
        return self.transaction_history
