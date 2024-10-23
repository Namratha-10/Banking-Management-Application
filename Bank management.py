# Dictionary to store account information
accounts = {}

# Function to open a new account
def open_new_account():
    acc_number = input("Enter account number: ")
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    
    if acc_number not in accounts:
        accounts[acc_number] = {'name': name, 'balance': initial_deposit}
        print(f"Account created successfully for {name}.")
    else:
        print("Account number already exists.")

# Function to deposit money
def deposit():
    acc_number = input("Enter account number: ")
    
    if acc_number in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_number]['balance'] += amount
        print(f"Deposited {amount}. New balance: {accounts[acc_number]['balance']}")
    else:
        print("Account not found.")

# Function to withdraw money
def withdraw():
    acc_number = input("Enter account number: ")
    
    if acc_number in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[acc_number]['balance']:
            accounts[acc_number]['balance'] -= amount
            print(f"Withdrew {amount}. New balance: {accounts[acc_number]['balance']}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

# Function to check account details and balance
def check_details():
    acc_number = input("Enter account number: ")
    
    if acc_number in accounts:
        print(f"Account Holder: {accounts[acc_number]['name']}")
        print(f"Balance: {accounts[acc_number]['balance']}")
    else:
        print("Account not found.")

# Function to display all accounts
def show_all_accounts():
    if accounts:
        for acc_number, details in accounts.items():
            print(f"Account Number: {acc_number}, Name: {details['name']}, Balance: {details['balance']}")
    else:
        print("No accounts found.")

# Main menu
def main():
    while True:
        print("\nBanking System Menu:")
        print("1. Open New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Checking Account Details and Balance")
        print("5. Exit or Quit")
        print("6. Show All Accounts")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            open_new_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_details()
        elif choice == '5':
            print("Thank you for using the banking system.")
            break
        elif choice == '6':
            show_all_accounts()
        else:
            print("Invalid choice. Please try again.")

# Run the banking system
if __name__ == "__main__":
    main()

            
            
        
        
        
    
    
    
                
                

            
            
        
    
