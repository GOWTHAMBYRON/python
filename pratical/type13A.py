# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:56:39 2025

@author: admin
"""

import pandas as pd


data = {
    "employee": ["Sahay", "George", "Priya", "Manila", "Raina", "Manila", "Priya"],
    "sales": [125600, 235600, 213400, 189000, 456000, 172000, 201400],
    "Quarter": [1, 1, 1, 1, 1, 2, 2],
    "State": ["Delhi", "Tamil Nadu", "Kerala", "Haryana", "West Bengal", "Haryana", "Kerala"]
}

df = pd.DataFrame(data)


states_q1 = df[df["Quarter"] == 1]["State"].unique()
print("States in Quarter 1:", states_q1)


employees_q2 = df[df["Quarter"] == 2]["employee"].tolist()
print("Employees in Quarter 2:", employees_q2)

employee_state = df[["employee", "State"]]
print("Employee Names with States:\n", employee_state)


high_sales_employees = df[df["sales"] > 200000][["employee", "sales"]]
print("Employees with Sales above 200000:\n", high_sales_employees)


state_sales = df.groupby("State")["sales"].sum()
print("State-wise Sales:\n", state_sales)


kerala_avg_sales = df[df["State"] == "Kerala"]["sales"].mean()
higher_than_kerala = df[df["sales"] > kerala_avg_sales][["employee", "sales"]]
print("Employees earning more than Kerala's average sales:\n", higher_than_kerala)

quarter_wise = df.groupby('Quarter')['sales'].agg(['mean','median',max,min,])
print(quarter_wise)

print("the total number of unique values :",df['employee'].unique().size)