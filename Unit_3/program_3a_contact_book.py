student = {}
student["name"] = input("Enter student name: ")
student["marks"] = int(input("Enter marks: "))

marks = student["marks"]
if not 0 <= marks <= 100:
    grade = "Invalid marks"
elif marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

student["grade"] = grade
print("Student:", student["name"])
print("Grade:", student["grade"])
