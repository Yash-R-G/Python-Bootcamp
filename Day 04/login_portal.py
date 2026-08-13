# Login portal

title1 = "Login Portal"
title2 = "Fixtye"

print(f"{title1:=^55}\n")

username = input("Enter Username\n : ")
password = input("Enter Password\n : ")
age = int(input("Enter Your Age\n : "))

# Admin
# Username : admin
# Password : python123

# Guest 
# Username : guest
# Password : 12345678

print("=" * 55)

if username == "admin" and password == "python123" and age >= 18:
    print("\nLogin Successfully!!")
    auth = input("Enable 2FA for security and to continue admin portal (Y/N) : ")
    if auth == "Y":
        print("=" * 55)
        print(f"\nWelcome to the {title2} Admin Panel\n") 
        print("Todo list\n\n1.Finish Guest panel work\n2.Grant auditor access to network logs\n3.Train staff on the login portal\n4.Drink water every 45 mins\n")
        print("="* 55)
    elif auth == "N":
        print("We are not here for your entertainment; kindly enable 2FA for your security.")
    else:
     print("❌ Invalid operator")

elif username == "admin" and password == "python123" and  age < 18:
    print("Login Failed\n")
    print("❌ You must be at least 18 years old.\n")
elif username == "guest" and password == "12345678":
    print("\nLogin Successfully!!")
    print(f"\nWelcome to the {title2} Guest Panel\n")
    print("Work on the Guest panel is pending, it will be available soon.")
else:
    print("❌ Invalid Username or Password!")
