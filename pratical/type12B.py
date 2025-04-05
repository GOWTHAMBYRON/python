# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:34:08 2025

@author: admin
"""

import pandas as pd


data = {
    "name": ["John", "Jane", "Emily", "Lisa", "Matt"],
    "note": [92, 94, 87, 82, 90],
    "profession": ["Electrical engineer", "Mechanical engineer", "Data scientist", "Accountant", "Athlete"],
    "date_of_birth": ["1998-11-01", "2002-08-14", "1996-01-12", "2002-10-24", "2004-04-05"],
    "group": ["A", "B", "B", "A", "C"]
}

df = pd.DataFrame(data)


df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])


largest = df.nlargest(2, "note")
smallest = df.nsmallest(2, "note")
print("Largest Notes:\n", largest)
print("Smallest Notes:\n", smallest)


print("First 2 rows (name & profession):\n", df.loc[:1, ["name", "profession"]])

5
print("Rows with note > 85:\n", df[df["note"] > 85])


engineers = df[df["profession"].str.contains("engineer", case=False)]["name"]
print("Engineers:", engineers.tolist())


j_names = df[df["name"].str.startswith("J")]
print("Persons with names starting with 'J':\n", j_names)


filtered_people = df[(df["profession"] == "Data scientist") | (df["note"] > 90)]
print("Data Scientists or Note > 90:\n", filtered_people)


print("Last 3 rows, 3rd column:\n", df.iloc[-3:, 2])


born_after_2000 = df[df["date_of_birth"].dt.year > 2000]
print("People born after 2000:\n", born_after_2000)
