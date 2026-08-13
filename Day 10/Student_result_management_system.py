# Student Result Management System
import time

title1 = "Selu School"
title2 = "Result Management System"

total_students = 0
pass_count = 0
fail_count = 0
total_marks = 0
highest_marks = -1
lowest_marks = 101
top_student = ""

print("=" * 55)
print(f"{title1:^55}")
print("=" * 55)

print("\n1. Student Portal")
print("2. Teacher Portal\n")
print("=" * 55)

while True:
    login_choice = input("Enter the number you want to login as : ")
    if login_choice == "1":
        print("This login client is under maintenance")
        exit()
    elif login_choice == "2":
        break
    else:
        print("Invalid operator...")

print("Welcome to the login page")

while True:
    Username = input("Enter Name\n: ")
    password = input("Enter Password\n: ")
    if password == "Python123":
        break
    else:
        print("Name and Password are invalid")

print("=" * 55)
time.sleep(1)
print("Loading.")
time.sleep(1)
print("Loading..")
time.sleep(1)
print("Loading...")
print("=" * 55)

print(f"\nHello Mr/Ms {Username}\n")
print("=" * 55)
print("\n* We have added a new system (Result Management)\n")

while True:
    print("1. Teacher list")
    print("2. Time table")
    print("3. Todo list")
    print("4. Result Management")
    print("5. Exit\n")
    print("=" * 55)

    choice = input("Enter the Number : ")
    
    if choice == "1":
        print("We are sorry to inform you")
        print("This page is still under maintenance")
        print("=" * 55)
        
    elif choice == "2":
        print("Time Table")
        print("Mon-Fri: 9:00 AM - 3:00 PM")
        print("=" * 55)
        
    elif choice == "3":
        print("=" * 55)
        print("Todo List")
        print("- Check assignments")
        print("- Update records")
        print("=" * 55)
        
    elif choice == "4":
        
        print("=" * 55)
        print("--- RESULT MANAGEMENT ---")
        print("=" * 55)

        count_input = int(input("How many students do you want to enter?\n "))
                

        print("-" * 40)

        for i in range(count_input):
            print(f"\n--- Student {i + 1} ---")
            name = input("Student Name: ")
            
            while True:
                marks = int(input("Marks (0-100): "))
                if 0 <= marks <= 100:
                    break
                else:
                    print("Invalid Marks")
                    print("Please enter marks between 0 and 100.")

            if marks >= 90:
                grade = "A"
                status = "Pass"
                pass_count += 1
            elif marks >= 75:
                grade = "B"
                status = "Pass"
                pass_count += 1
            elif marks >= 60:
                grade = "C"
                status = "Pass"
                pass_count += 1
            elif marks >= 35:
                grade = "D"
                status = "Pass"
                pass_count += 1
            else:
                grade = "F"
                status = "FAIL"
                fail_count += 1

            
            total_students += 1
            total_marks += marks

            if marks > highest_marks:
                highest_marks = marks
                top_student = name
            
            if marks < lowest_marks:
                lowest_marks = marks

            print(f"\n{name}")
            print(f"Marks : {marks}")
            print(f"Grade : {grade}")
            print(f"Status : {status}")
        
        print("\nBatch Processing Complete!")
        print("=" * 55)

    elif choice == "5":
        print("Thanks for using Selu Cli")
        print("Have a great day...")
        if total_students > 0:
            print(f"\nFinal Stats:")
            print(f"Total Students: {total_students}")
            print(f"Pass: {pass_count} | Fail: {fail_count}")
            print(f"Top Student: {top_student} ({highest_marks})")
        exit()
        
    else:
        print("Invalid operator...")
        print("=" * 55)   
