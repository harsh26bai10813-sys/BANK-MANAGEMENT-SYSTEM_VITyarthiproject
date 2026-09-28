# Bank Account Management System
accounts = {}
def create_account():
account_no = input("Enter account number: ")
if account_no in accounts:
print("Account already exists.")
return
name = input("Enter account holder name: ")
balance = float(input("Enter initial deposit: "))
accounts[account_no] = {
"name": name,
"balance": balance
}
print("Account created successfully!")
def check_balance():
account_no = input("Enter account number: ")
if account_no in accounts:
print("Account Holder:", accounts[account_no]["name"])
print("Balance: Rs.", accounts[account_no]["balance"])
else:
print("Account not found.")
def deposit_money():
account_no = input("Enter account number: ")
if account_no in accounts:
amount = float(input("Enter deposit amount: "))
if amount > 0:
accounts[account_no]["balance"] += amount
print("Amount deposited successfully!")
print("New Balance: Rs.", accounts[account_no]["balance"])
else:
print("Invalid amount.")
else:
print("Account not found.")
def withdraw_money():
account_no = input("Enter account number: ")
if account_no in accounts:
amount = float(input("Enter withdrawal amount: "))
if amount <= 0:
print("Invalid amount.")
elif amount > accounts[account_no]["balance"]:
print("Insufficient balance.")
else:
accounts[account_no]["balance"] -= amount
print("Amount withdrawn successfully!")
print("Remaining Balance: Rs.",
else:
accounts[account_no]["balance"])
print("Account not found.")
def display_accounts():
if len(accounts) == 0:
print("No accounts found.")
return
print("\n========== ALL ACCOUNTS ==========")
for account_no, details in accounts.items():
print("Account No:", account_no)
print("Name:", details["name"])
print("Balance: Rs.", details["balance"])
print("---------------------------------")
while True:
print("\n================================")
print(" BANK ACCOUNT MANAGEMENT")
print("================================")
print("1. Create Account")
print("2. Check Balance")
print("3. Deposit Money")
print("4. Withdraw Money")
print("5. Display All Accounts")
print("6. Exit")
print("================================")
choice = input("Enter your choice: ")
if choice == "1":
create_account()
elif choice == "2":
check_balance()
elif choice == "3":
deposit_money()
elif choice == "4":
withdraw_money()
elif choice == "5":
display_accounts()
elif choice == "6":
break
print("Thank you for using our banking system!")
else:
print("Invalid choice. Please try again.")
