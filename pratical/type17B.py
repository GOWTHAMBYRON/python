# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 12:12:28 2025

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


print("Number of employees in each department:")
print(df["Dept"].value_counts())


print("\nPart-time employees in the Marketing department:")
print(df[(df["Dept"] == "Marketing") & (df["Type"] == "Parttime")])


print("\nAverage and total salary of each department:")
print(df.groupby("Dept")["Salary"].agg(["mean", "sum"]))


print("\nEmployees with experience greater than 2:")
print(df[df["Exp"] > 2])


print("\nSummary info of the dataset:")
print(df.info())


print("\nEmployees grouped by employment type:")
print(df.groupby("Type")["Name"].apply(list))


plt.bar(df["Name"], df["Exp"], color='green')
plt.xlabel("Employee Name")
plt.ylabel("Experience (years)")
plt.title("Employee Experience")
plt.xticks(rotation=45)
plt.show()


least_salaried = df.loc[df["Salary"].idxmin()]
print("\nLeast salaried person:")
print(least_salaried)
