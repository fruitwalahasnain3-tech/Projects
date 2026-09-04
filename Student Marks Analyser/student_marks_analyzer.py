name = input("Enter student name: ")
python = int(input("Enter marks of Python: "))
database = int(input("Enter marks of Data Base: "))
maths = int(input("Enter marks of Mathematics: "))
total = python + database + maths
percentage = (total/300)*100

if python < 0 or  python > 100:
    print("Invalid marks! Marks must be between 0 and 100.")
elif database < 0 or  database > 100:
    print("Invalid marks! Marks must be between 0 and 100.")
elif maths < 0 or  maths > 100:
    print("Invalid marks! Marks must be between 0 and 100.")
else:    
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"

    elif percentage >= 70:
        grade = "C"

    elif percentage >= 60:
        grade = "D"

    else:
            grade = "F"

    print("\n-----Student Marks Analyzer v1.0.-----")
    print(f"Student: {name}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage :.2f}%")
    print(f"Grade : {grade}")




