students = {
    "Arun": 85,
    "Rahul": 92,
    "Anu": 78,
    "Meera": 95
}
highest_marks = 0
top_student = ""
for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = name
print("Highest Scorer:", top_student)
print("Marks:", highest_marks)