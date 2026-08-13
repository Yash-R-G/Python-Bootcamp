# Task Manager CLI 
import time

title = " Task Manager "
task = ""
completed = False
completed_tasks = 0

while True:
    taskm = input("Do you want to open Task Manager (Y/N) :")
    if taskm.upper() == "Y":
        break
    elif taskm.upper() == "N":
        print("=" * 55)
        print("Have a great day")
        print("=" * 55)
        exit()
    else:
        print("Invaild operator")
    
time.sleep(1)
print("Loading.")
time.sleep(1)
print("Loading..\n")

print(f"{title:=^53}\n")

print("1. Add Task")
print("2. View Tasks")
print("3. Complete Task")
print("4. Show Progress")
print("5. Exit\n")

print("=" * 55)

while True:
    choice = int(input("Enter the number : "))
    if choice == 1:
        task = input("Enter your task : ")
        completed = False 
        print("=" * 55)
        print(f"Your current task : \n . {task}")
        print("=" * 55)
    elif choice == 2:
        print("=" * 55)
        print("Here is the list of the task")
        print("=" * 55)
        if task == "":
            print("Nothing here to see, no task found.")
            print("=" * 55)
        else:
            print(f"{task}")
            status = "Completed" if completed else "Pending"
            print(f"Status: {status}")
            print("=" * 55)
    elif choice == 3:
        if task == "":
            print("Nothing to complete.")
        elif completed:
            print("Task is already completed.")
        else:
            completed = True
            completed_tasks += 1
            print("=" * 55)
            print("Task Completed!")
            print("Great Job!")
            print("Consistency is the key for success")
            print("=" * 55)
    elif choice == 4:
        print("=" * 55)
        print("Progress")
        progress = "100%" if completed else "0%"
        print(f"{progress}")
        print("=" * 55)
    elif choice == 5:
        print("=" * 55)
        print("Goodbye!")
        print(f"Total Tasks Completed : {completed_tasks}")
        print("=" * 55)
        break
    else:
        print("Invalid choice. Please choose 1-5.")
