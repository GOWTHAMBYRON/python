# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 18:12:52 2025

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Asha", "Harsh", "Sourav", "Hritik", "Shivansh", "Akash", "Soumya", "Kartik"],
    "Dept": ["Administration", "Marketing", "Technical", "Technical", "Administration", "Marketing", "Technical", "Administration"],
    "Type": ["Fulltime", "Intern", "Intern", "Parttime", "Parttime", "Fulltime", "Intern", "Intern"],
    "Salary": [120000, 50000, 70000, 67800, 55000, 57900, 64300, 110000],
    "Exp": [10, 2, 3, 4, 7, 3, 2, 8]
}

df = pd.DataFrame(data)

print("Number of employees in each department:\n", df["Dept"].value_counts())

parttime = df[(df["Dept"] == "Marketing") & (df["Type"] == "Parttime")]
print("\nPart-time employees in Marketing department:\n", parttime)

print("\nAverage and Total salary of each department :\n" , df.groupby("Dept")["Salary"].agg(["mean", "sum"]))

print("\n Employee with experience greater than 2 \n" , df[df.Exp > 2] )

print("\nDataset Info:")
print(df.info())

plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Exp"], color='green')
plt.xlabel("Employee Name")
plt.ylabel("Experience (Years)")
plt.title("Employee Experience")
plt.xticks(rotation=90)
plt.show()


print("\nUnique Department Names: \n",  df["Dept"].unique())