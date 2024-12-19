def calculate_student_performance():
    student_number = input("Enter student number: ")
    student_name = input("Enter student name: ")

    c = float(input("Enter marks in C: "))
    cpp = float(input("Enter marks in C++: "))
    java = float(input("Enter marks in Java: "))

    total_marks = c + cpp + java
    average_marks = total_marks / 3

    if average_marks < 70:
        result = "Fail"
        grade = "F"
    else:
        result = "Pass"
        if average_marks >= 90:
            grade = "A"
        elif average_marks >= 80:
            grade = "B"
        elif average_marks >= 70:
            grade = "C"
        else:
            grade = "D"

    print("Total Marks: " + str(total_marks))
    print("Average Marks: " + str(average_marks))
    print("Result: " + str(result))
    print("Grade: " + str(grade))


calculate_student_performance()