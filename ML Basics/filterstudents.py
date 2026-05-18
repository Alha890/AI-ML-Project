import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Rahul", "Sneha", "Anjali"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Students with marks above 80")
print(df[df["Marks"] > 80])

print("Students whose age is above 20")
print(df[df["Age"] > 20])