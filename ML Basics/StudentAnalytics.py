import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

print("\nSummary Statistics")
print(df.describe())

df["Pass/Fail"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 75 else "Fail"
)

print("\nUpdated DataFrame")
print(df)

df.to_csv("cleaned_students.csv", index=False)

department_avg = df.groupby("Department")["Marks"].mean()

plt.figure(figsize=(6, 4))
plt.bar(department_avg.index, department_avg.values)
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()

pass_fail_count = df["Pass/Fail"].value_counts()

plt.figure(figsize=(5, 5))
plt.pie(pass_fail_count.values,
        labels=pass_fail_count.index,
        autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

report = f"""
STUDENT ANALYSIS REPORT
-----------------------
Total Students : {len(df)}

Average Marks  : {df['Marks'].mean():.2f}
Highest Marks  : {df['Marks'].max()}
Lowest Marks   : {df['Marks'].min()}

Students Passed: {len(df[df['Pass/Fail'] == 'Pass'])}
Students Failed: {len(df[df['Pass/Fail'] == 'Fail'])}
"""

print(report)