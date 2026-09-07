marks = []

name = input("Enter student name: ")

marks.append(int(input("Enter marks of Python: ")))
marks.append(int(input("Enter marks of Data Base: ")))
marks.append(int(input("Enter marks of Mathematics: ")))

valid = True

for mark in marks:
    if mark < 0 or mark > 100:
        print("Invalid marks, Enter marks between 0 to 100")
        valid = False

if valid:
    total = sum(marks)
    print("Total marks:", total)

    avg = sum(marks) / len(marks)
    print("Average marks:", avg)

    maxi = max(marks)
    print("Maximum marks:", maxi)

    mini = min(marks)
    print("Minimum marks:", mini)

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Your grade is:", grade)
    
    passed = 0
    failed = 0

    for mark in marks:
        if mark >= 50:
            passed += 1 
        else:
            failed +=1 
    print("Passed Subjects: " , passed) 
    print("Failed Subjects: " , failed)         