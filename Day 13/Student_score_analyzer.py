#  Student score analyzer

title = "Student Score Analyzer"
width = 55

print("=" * width)
print(f"{title:-^55}")
print("=" * width)
print()

names_list = []
scores_list = []
records_list = []

while True:
    count_input = input("How many students do you want to add in data?\n: ")
    if count_input.isdigit() and int(count_input) > 0:
        num_students = int(count_input)
        break
    else:
        print()
        print("Enter the valid number")
        print()

for i in range(num_students):
    print(f"\n--- Student {i + 1} ---")
    print()

    name = input("Enter student Name : ").title()

    while True:

        score_input = input(f"Enter {name} score : ")
        if score_input.isdigit():
            score = int(score_input)
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        else:
            print("Please enter a valid number.")

    names_list.append(name)
    scores_list.append(score)

    student_tuple = (name, score)
    records_list.append(student_tuple)

# 1. Average Score
total_score = sum(scores_list)
average_score = total_score / len(scores_list)

# 2. Highest & Lowest Scores (Using built-in list operations)
highest_score = max(scores_list)
lowest_score = min(scores_list)

# 3. Unique Scores (Using Set)
unique_scores = set(scores_list)

# 4. Top Student (Finding index of highest score)
top_index = scores_list.index(highest_score)
top_student_name = names_list[top_index]

print("\n" + "=" * width)
print("ANALYSIS RESULTS")
print("=" * width)

print(f"\n1. Average Score : {average_score:.2f}")
print(f"2. Highest Score : {highest_score}")
print(f"3. Lowest Score  : {lowest_score}")
print(f"4. Unique Scores : {unique_scores}")

print("\n5. Student Records (Tuples):")
for record in records_list:
    print(f"   {record}")

print("\nBONUS:")
print(f"   Top Student : {top_student_name}")
print(f"   Score       : {highest_score}")
print("=" * width)
