#  day 7 
# # Password Strength Checker

title1 = "Password Strength Checker"

print("=" * 55)
print("\nWelcome to the Password Checker Session\n")

username = input("Enter your Name\n: ")
password = input("Enter the password you want to test\n: ")

print("=" * 55)
print("Our security insecptor on it way to check...")
for x in range(1, 11):
    print(x)

print("We checked your password")
print("=" * 55)

has_digit = False
has_upper = False
has_lower = False

if len(password) >= 8:
    pass
else:
    print("📏 Your password is shorter than my attention span. Needs at least 8 characters!")

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True

if has_digit:
    pass
else:
    print("No numbers? Did you think this was protect you add an number")

if has_upper:
    pass
else:
    print("Where is the capital letter? Are you afraid of the Shift key?")

if has_lower:
    pass
else:
    print("Are you yelling on your password? You need some lowercase letters too...")

print("=" * 55)
if len(password) >= 8 and has_lower and has_upper and has_digit:
    print("🏆 Congrats! Your password is strong")
else:
    print("This password is an open invitation to hackers")
    print("Please change it before someone steals your identity to buy 500 pizzas or it will be me.")
print("=" * 55)   
