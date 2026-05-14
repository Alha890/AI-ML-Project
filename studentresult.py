class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def calculate_total(self):
        return sum(self.marks)
    def calculate_average(self):
        return self.calculate_total() / len(self.marks)
    def find_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "Fail"
    def display_result(self):
        print("\nStudent Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.find_grade())
students = []
student1 = Student("Arun", 101, [85, 90, 88])
student2 = Student("Meera", 102, [95, 92, 96])
student3 = Student("Rahul", 103, [70, 75, 80])
students.append(student1)
students.append(student2)
students.append(student3)
for student in students:
    student.display_result()
topper = students[0]
for student in students:
    if student.calculate_total() > topper.calculate_total():
        topper = student
print("\nClass Topper:", topper.name)
file = open("results.txt", "w")
for student in students:
    file.write("Name: " + student.name + "\n")
    file.write("Roll Number: " + str(student.roll_number) + "\n")
    file.write("Total: " + str(student.calculate_total()) + "\n")
    file.write("Average: " + str(student.calculate_average()) + "\n")
    file.write("Grade: " + student.find_grade() + "\n\n")
file.close()
print("Results saved into file successfully.")