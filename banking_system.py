import sys

accounts = {}

def create_account():
    global accounts
    name = input("Enter your name: ")
    balance = float(input("Enter initial balance: "))
    if balance < 0:
        print("Initial balance cannot be negative.")
        return
    account_number = len(accounts) + 1
    accounts[account_number] = {"name": name, "balance": balance}
    print(f"Account created successfully! Your account number is {account_number}")

def deposit():
    global accounts
    account_number = int(input("Enter account number: "))
    if account_number not in accounts:
        print("Account does not exist.")
        return
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Deposit amount cannot be negative.")
        return
    accounts[account_number]["balance"] += amount
    print("Deposit successful.")

def withdraw():
    global accounts
    account_number = int(input("Enter account number: "))
    if account_number not in accounts:
        print("Account does not exist.")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount < 0:
        print("Withdrawal amount cannot be negative.")
        return
    if amount > accounts[account_number]["balance"]:
        print("Insufficient funds.")
        return
    accounts[account_number]["balance"] -= amount
    print("Withdrawal successful.")

def view_balance():
    global accounts
    account_number = int(input("Enter account number: "))
    if account_number not in accounts:
        print("Account does not exist.")
        return
    print(f"Your balance is: {accounts[account_number]['balance']}")

def main():
    while True:
        print("\nWelcome to the simple banking system")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            view_balance()
        elif choice == '5':
            print("Thank you for using the banking system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
