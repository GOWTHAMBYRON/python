# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 17:06:05 2025

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt

# Creating the dataframe
data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

df = pd.DataFrame(data)

df_sorted = df.sort_values(by="population", ascending=False)
print("\nCountries sorted by population:\n", df_sorted)


plt.figure(figsize=(7, 7))
explode = [0, 0, 0.1, 0, 0]  
plt.pie(df["area"], labels=df["country"], autopct='%1.1f%%', startangle=140, explode=explode)
plt.title("Area Occupied by Each Country")
plt.show()


plt.figure(figsize=(7, 5))
plt.bar(df["country"], df["population"], color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Country")
plt.ylabel("Population (millions)")
plt.title("Population of Each Country")
plt.show()


#df_slice = df[["country", "population"]]
df_slice = df.loc[:,["country", "population"]]
print("\nCountry and Population:\n", df_slice)


#capital_russia = df[df["country"] == "Russia"]["capital"].values[0]
capital_russia =df.loc[df["country"] == "Russia", "capital"].iloc[0]

print("\nCapital of Russia:", capital_russia)


#capitals_with_a = df[df["capital"].str.endswith('a')]["capital"].tolist()
capitals_with_a = df.loc[df['capital'].str.endswith('a'), 'capital'].tolist()
print("\nCapitals ending with 'a':", capitals_with_a)


#smallest_country = df.loc[df["area"].idxmin(), "country"]
smallest_country =df.loc[df["area"].sort_values().index[0], "country"]
print("\nThe smallest country by area is:", smallest_country)


large_countries = df.loc[df["area"] > 7, "country"].tolist()
print("\nCountries with area above 7:", large_countries)
