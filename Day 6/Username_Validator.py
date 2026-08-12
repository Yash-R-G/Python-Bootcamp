# Username Validator

name = input("Enter your name : ")

name = name.strip()
name = name.lower()

if name[0].isdigit():
    print("Re-enter your username, username cannot start with a number.")
elif len(name) >= 5: 
    print(f"UserName Accpected : {name}")
    print("=" * 55)
    print(f"\nFirst Character : {name[0]}")
    print(f"Last Character : {name[-1]}")
    print(f"\nLength : {len(name)}")
    print(f"Uppercase : {name.upper()}")
    print("=" * 55)
    print("You have unlock the bouns path\n")
    name1 = input("\nEnter your full name for fun : ")
    print(f"Capial Name : {name1.capitalize()}")
    print(f"Occurrences of 'a' : {name1.count('a')}")
    print(f"Replacing 'a' : {name1.replace('a', '@')}\n")
    print("=" * 55)
    print("\nthanks for using the username creation")
    print("=" * 55)
else:
    print("Username too short")
