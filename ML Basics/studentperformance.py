import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Rahul", "Sneha", "Anjali",
             "Vikram", "Neha", "Kiran", "Pooja", "Ajay"],
    
    "Department": ["CSE", "ECE", "CSE", "EEE", "ECE",
                   "CSE", "EEE", "ECE", "CSE", "EEE"],
    
    "Marks": [85, 90, 78, 92, 88,
              95, 70, 82, 89, 76],
    
    "Attendance": [80, 92, 68, 95, 72,
                   88, 60, 77, 85, 70]
}

df = pd.DataFrame(data)

print("Student DataFrame")
print(df)

topper = df[df["Marks"] == df["Marks"].max()]

print("Topper")
print(topper)

avg_marks = df.groupby("Department")["Marks"].mean()

print("Average Marks Department-wise")
print(avg_marks)

low_attendance = df[df["Attendance"] < 75]

print("Students with Attendance Below 75%")
print(low_attendance)

sorted_df = df.sort_values(by="Marks", ascending=False)

print("Students Sorted by Marks")
print(sorted_df)