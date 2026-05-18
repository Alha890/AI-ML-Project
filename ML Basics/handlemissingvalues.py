import pandas as pd
import numpy as np

data = {
    "Name": ["Arun", "Meera", "Rahul", "Sneha", "Anjali"],
    "Age": [20, np.nan, 19, 22, np.nan],
    "Marks": [85, 90, np.nan, 92, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

print("Missing Values")
print(df.isnull())

filled_df = df.fillna({
    "Age": df["Age"].mean(),
    "Marks": df["Marks"].mean()
})

print("Filled Missing Values")
print(filled_df)

dropped_df = df.dropna()

print("Rows After Removing Missing Data")
print(dropped_df)