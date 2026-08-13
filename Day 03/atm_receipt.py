title = "Fast Tag ATM"

account_holder_name = input("Enter your account name : ")

print("=" * 55)
print(f"\nWelcome, {account_holder_name} Your Smart Banking Journey Starts Here.\n")

current_balance = float(input("Enter your current balance : ₹"))
withdrawal_amount = float(input("Enter the ammount you would like to withdraw : ₹"))

percentage = (withdrawal_amount / current_balance) * 100
remaining_balance = current_balance - withdrawal_amount

# print("=" * 55)

if withdrawal_amount <= 0:
    print("=" * 55)
    print("Invalid Withdrawal Amount!")
    print("=" * 55)
elif current_balance >= withdrawal_amount:
    print(f"\nYou withdrew {percentage:.2f}% of your balance")
    print("\nhere is your recipt\n")
    print(f"{title:=^55}")

    print(f"\nAccount Holder    : {account_holder_name}")

    print(f"\nCurrent Balance   : ₹{current_balance:,.2f}")
    print(f"Withdrawl Amount  : ₹{withdrawal_amount:,.2f}\n")

    print("Withdrawal Successful!")
    print(f"\nRemaining Balance : ₹{remaining_balance} ")

    print("\nThank you for banking with us!\n")

    print("=" * 55)
else:
    print("=" * 55)
    print("Insufficient Balance!")
    print("=" * 55)
