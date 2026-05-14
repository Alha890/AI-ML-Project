class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
    def calculate_average(self):
        average = sum(self.marks) / len(self.marks)
        print("Average Marks:", average)
student1 = Student("Arun", 101, [85, 90, 88])
student1.display_details()
student1.calculate_average()