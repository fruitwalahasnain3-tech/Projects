try:
    name = input("Enter student name: ")
    course = input("Enter student course: ")
    semester = input("Enter student semester: ")
    marks = int(input("Enter student marks: "))
    if marks < 0 or marks>100:  
        raise ValueError("Enter marks between 0 to 100!")
    try:
        with open("studentfile.txt","w") as file:
            file.write("Name: " + name + "\n")
            file.write("Course: " + course + "\n")
            file.write("Semester: " + semester + "\n")
            file.write("Python marks: " + str(marks) + "\n")
            
        with open("studentfile.txt","r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("File not found! ")

except ValueError as e:
  print(e)
