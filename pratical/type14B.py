# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:29:38 2025

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


largest_smallest = pd.concat([df.nlargest(2, "note"), df.nsmallest(2, "note")])
print("\nLargest and Smallest based on note:\n", largest_smallest)


print("\nFirst 2 rows (name and note):\n", df.loc[:1, ["name", "note"]])

print("\nRows with note > 90:\n", df[df["note"] > 90])


print("\nNames of engineers:\n", df[df["profession"].str.contains("engineer", case=False)]["name"])

print("\nPersons whose name starts with 'J':\n", df[df["name"].str.startswith("J")])


print("\nData scientists or note > 90:\n", df[(df["profession"] == "Data scientist") | (df["note"] > 90)])


print("\nLast 3 rows - Third column (Profession):\n", df.iloc[-3:, 2])


print("\nNames in group A or C:\n", df[df["group"].isin(["A", "C"])]["name"])


print("\nNames of athletes:\n", df[df["profession"] == "Athlete"]["name"])


print("\nPersons born after 2000:\n", df[df["date_of_birth"].dt.year > 2000])
