# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 13:50:42 2025

@author: admin
"""

import pandas as pd
import numpy as np


data = {
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", np.nan, "Spark", "Python"],
    'Fee': [22000, 25000, 23000, 24000, np.nan, 25000, 25000, 22000],
    'Duration': [30, 50, 55, 40, 60, 35, 45, 50],
    'Discount': [1000, 2300, 1000, 1200, 2500, 1300, 1400, 1600]
}

df = pd.DataFrame(data)


print(f"Number of rows and columns: {df.shape}")

print("\nColumn names and data types:")
print(df.dtypes)


print("\nCourses and Duration for 1,3,5 rows:")
print(df.loc[[1, 3, 5], ['Courses', 'Duration']])


print("\nCourses with discount between 1000 and 2000:")
print(df[df['Discount'].between(1000, 2000)][['Courses', 'Discount']])


df["Tutors"] = ['William', 'Henry', 'Michael', 'John', 'Messi', 'Ramana', 'Kumar', 'Vasu']
print("\nDataFrame after adding Tutors column:")
print(df)


print("\nNull values statistics:")
print(df.isnull().sum())

print("\nCourses that start with 'P':")
print(df[df['Courses'].str.startswith("P", na=False)])


print("\nCourses with Duration more than 40 days:")
print(df[df['Duration'] > 40][['Courses', 'Duration']])
