# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 13:04:44 2025

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],  # in million sq. km
    "population": [200.4, 143.5, 1252, 1357, 52.98]  # in million
}

df = pd.DataFrame(data)


df_sorted = df.sort_values(by="population", ascending=False)
print("Countries sorted by population:\n", df_sorted)


plt.figure(figsize=(6,6))
plt.pie(df['area'], labels=df['country'], autopct='%1.1f%%', startangle=140)
plt.title("Area occupied by each country")
plt.show()


plt.figure(figsize=(8,5))
plt.bar(df['country'], df['population'], color='yellow')
plt.xlabel("Country")
plt.ylabel("Population (millions)")
plt.title("Population of Each Country")
plt.show()


print("Country and Population:\n", df[['country', 'population']])


capital_china = df[df["country"] == "China"]["capital"].values[0]
print("Capital of China:", capital_china)


capitals_ending_a = df[df["capital"].str.endswith("a")]["capital"]
print("Capitals ending with 'a':\n", capitals_ending_a.to_list())


null_values = df.isnull().sum()
print("Number of null values in each column:\n", null_values)


smallest_country = df[df["area"] == df["area"].min()]["country"].values[0]
print("Smallest country by area:", smallest_country)
