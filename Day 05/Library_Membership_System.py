# Library Membership System

title1 = "Library Membership Checker"
title2 = "Library Membership Portal" 


print(f"{title1:=^55}\n")

name = input("Enter your name \n: ")
age = int(input("Enter your age \n: "))
student = input("Are you a student (Y/N):")
member = input("Have you ever paid for membership (Y/N): \n")
# membership = input("Have you ")

member_type = "Student" if student == "Y" else "Regular"
discount = "20%" if student == "Y" else "0%"

print("=" * 55)

if age >= 12 and member == "Y":
    print(f"{title1:^55}")
    print("=" * 55)
    print(f"\nName : {name}")
    print(f"\nAge : {age}")
    print(f"\nMembership Type : {member_type}")
    print(f"Discount : {discount}")
    print("Status : Approved\n")
    print(f"Enjoy reading! {name}📚\n")
    print("=" * 55)
elif age >= 12 and member == "N":
    print(f"{title1:^55}")
    print("=" * 55)
    print(f"\nName : {name}")
    print(f"\nAge : {age}")
    print(f"\nMembership Type : {member_type}")
    print(f"Discount : {discount}")
    print("Status : Pending\n")
    print(f"Join us today to unlock full access, {name}! 📚\n")
    print("=" * 55)
elif age < 12:
    print(f"{title1:^55}")
    print("=" * 55)
    print(f"\nName : {name}")
    print(f"\nAge : {age}")
    print("Status : Rejected")
    print(f"Reason : Minimum age is 12\n")
    print(f"{name}, keep up your passion for learning!\n")
    print("=" * 55)
else:
    print(f"{title1:^55}")
    print("You have entered an invalid value.\n")
    print("=" * 55)
