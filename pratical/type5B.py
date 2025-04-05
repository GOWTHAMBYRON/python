# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 19:47:52 2025

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


print(df.loc[[0, 2, 4], ['Courses', 'Duration']])

print()
print(df[(df['Discount'] >= 1000) & (df['Discount'] <= 2000)][['Courses', 'Discount']])


df['Tutors'] = ['William', 'Henry', 'Michael', 'John', 'Messi', 'Ramana', 'Kumar', 'Vasu']
print(df)

df.rename(columns={'Fee': 'Fees'}, inplace=True)
print(df)


print(df.isnull().sum(), "\n")


print(df[df['Courses'].str.startswith('P', na=False)])


print(df[df['Duration'] > 40])

print(df.groupby('Courses')[['Discount', 'Fees']].mean())
