import time

balance = 5000
transaction_count = 0
current_password = "Python123"

title1 = "Login System"
title2 = "Secure Access"
title3 = "XH Bank Menu"

# --- LOGIN ---
while True:
    print(f"\n{title1:=^55}\n")
    print(f"{title2:>22}\n")
    username = input("Enter username\n: ")
    password = input("Enter Password\n: ")

    if password == current_password:
        print("=" * 55)
        print(f"Welcome, {username}")
        break
    else:
        print("=" * 55)
        print("Username and password not found")
        quit = input("Do you want to quit (Y/N): ")
        if quit.upper() == "Y":
            exit()
        else:
            continue

time.sleep(1)
print(f"\n{title3:=^54}\n")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Change Password")
print("5. Exit")

# --- MENU ---
while True:
    num = int(input("Enter the number: "))
    
    if num == 1:
        print("fetching balance.")
        time.sleep(1)
        print("fetching balance..")
        time.sleep(1)
        print("fetching balance...\n")
        print("=" * 55)
        print("Balance fetched successfully!")
        print(f"Current Balance : ₹{balance:,.2f}")
        print(f"Total Transactions: {transaction_count}")
        print("=" * 55)

    elif num == 2:
        time.sleep(1)
        print("=" * 55)
        print("Connected to the XH Bank server")
        print(f"Transaction Count : {transaction_count}")
        deposit = float(input("Enter amount to deposit: ₹"))
        if deposit > 0:
            print(f"₹{deposit:,.2f} deposited successfully.")
            balance += deposit
            transaction_count += 1
        else:
            print("Deposit amount can't be zero")

    elif num == 3:
        time.sleep(1)
        print("=" * 55)
        print("Connected to the XH Bank server")
        print(f"Transaction Count : {transaction_count}")
        withdraw = float(input("Enter withdrawal amount: ₹"))
        
        if withdraw == 0:
            print("Withdrawal amount can't be zero")
        elif withdraw > balance:
            print("Insufficient funds!")
        else:
            time.sleep(1)
            print("Processing withdrawal.")
            time.sleep(1)
            print("Processing withdrawal..")
            time.sleep(1)
            print("Your digital money got green\n")
            print(f"You have withdrawn ₹{withdraw:,.2f}")
            balance -= withdraw
            transaction_count += 1
            print(f"Remaining Balance: ₹{balance:,.2f}")

    elif num == 4:
        time.sleep(1)
        print("=" * 55)
        print("Connected to the XH Bank server")
        
        current_input = input("Enter current password\n: ")
        if current_input == current_password:
            new_password = input("Enter new password\n: ")
            
            has_digit = False
            has_upper = False
            has_lower = False
            
            for char in new_password:
                if char.isdigit(): has_digit = True
                if char.isupper(): has_upper = True
                if char.islower(): has_lower = True
            
            if len(new_password) < 8:
                print("Needs at least 8 characters!")
            if not has_digit:
                print("No numbers? Did you think this would protect you? Add a number!")
            if not has_upper:
                print("Where is the capital letter? Are you afraid of the Shift key?")
            if not has_lower:
                print("Are you yelling on your password? You need some lowercase letters too...")
            
            if len(new_password) >= 8 and has_digit and has_upper and has_lower:
                current_password = new_password
                print("Password changed successfully!")
                transaction_count += 1
            else:
                print("Password not changed. Try again.")
        else:
            print("Wrong current password.")

    elif num == 5:
        print("Exiting...")
        break
    else:
        print("Invalid option.")   
