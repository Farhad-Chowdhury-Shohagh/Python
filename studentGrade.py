# Student Grade Management System using Functions

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


def calculate_grade(average):
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "A-"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"


def display_result(name, marks, average, grade):
    print("\n----- Student Result -----")
    print("Student Name:", name)
    print("Marks:", marks)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)


def main():
    print("Student Grade Management System")
    name = input("Enter student name: ")
    marks = []
    subjects = int(input("Enter number of subjects: "))

    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    display_result(name, marks, average, grade)

main()
