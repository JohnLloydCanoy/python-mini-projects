import pandas as pd
import numpy as np

df = pd.read_csv("sample.csv")
"""


print(df)
print(len(df["barangay_name"]))


print(df.tail())

print(df.describe())

print(df[df["classification"] == "Urban"])
"""
# Updating values in a DataFrame

df.loc[df["barangay_name"] == "Carmen", "classification"] = "Rural"
print(df)