def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"


if __name__ == "__main__":
    print("===== STUDENT RESULT MANAGEMENT SYSTEM =====")

    name = input("Enter student name: ")

    python_marks = float(input("Enter Python marks: "))
    dbms_marks = float(input("Enter DBMS marks: "))
    devops_marks = float(input("Enter DevOps marks: "))

    marks = [python_marks, dbms_marks, devops_marks]

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\n===== STUDENT RESULT =====")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)