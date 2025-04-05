# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 10:58:57 2025

@author: admin
"""

import pandas as pd


data = {
    "age": [10, 22, 13, 21, 12, 11, 17],
    "section": ["A", "B", "C", "B", "B", "A", "A"],
    "city": ["Gurgaon", "Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai"],
    "gender": ["M", "F", "F", "M", "M", "M", "F"],
    "favourite_color": ["red", None, "yellow", None, "black", "green", "red"]
}

df = pd.DataFrame(data)


grouped_colors = df.groupby("city")["favourite_color"].apply(lambda x: list(x.dropna()))
print("\nGrouped colors by city:\n", grouped_colors)


cities_ending_with_i = df[df["city"].str.endswith("i")]["city"].unique()
print("\nCities ending with 'i':\n", cities_ending_with_i)


null_values = df.isnull().sum()
print("\nNull values per column:\n", null_values)


unique_cities = df["city"].unique()
print("\nUnique city names:\n", unique_cities)


gender_count = df["gender"].value_counts()
print("\nCount of males and females:\n", gender_count)


average_age_by_city = df.groupby("city")["age"].mean()
print("\nAverage age per city:\n", average_age_by_city)


total_age_by_section = df.groupby("section")["age"].sum()
print("\nTotal age per section:\n", total_age_by_section)


count_per_city = df["city"].value_counts()
print("\nNumber of persons in each city:\n", count_per_city)
