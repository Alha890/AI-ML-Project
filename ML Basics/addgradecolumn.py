import pandas as pd

data = {
    "Name": ["Arun", "Meera", "Rahul", "Sneha", "Anjali"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 90 else "B" if x >= 75 else "C"
)

print(df)