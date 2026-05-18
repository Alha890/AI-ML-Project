import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Rahul", "Sneha", "Anjali"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print(df)

print(df.head(3))

print(df.shape)