from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    if name.isalpha():
        email = input("Enter email: ")
        user = User(name, email)
        if not user.is_valid_email(email):
            print("Invalid email address!")  # ✅ Issue #7
            return
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
        print("No users available. Please create a user first.\n")  # ✅ Issue #4
        return

    list_users()
    try:
        idx = int(input("Select user number: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")  # ✅ Issue #5
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
        print("Invalid account type!")  # ✅ Issue #6
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
            print("Invalid user selection.\n")  # ✅ Issue #5
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
            print("Invalid account selection.\n")  # ✅ Issue #3
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
            print("Invalid user selection.\n")  # ✅ Issue #5
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
            print("Invalid account selection.\n")  # ✅ Issue #3
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
            print("Invalid user selection.\n")  # ✅ Issue #5
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
