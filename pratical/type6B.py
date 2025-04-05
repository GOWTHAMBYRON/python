import pandas as pd
import numpy as np

# Creating the DataFrame
data = {
    'age': [10, 22, 13, 21, 12, 11, 17],
    'section': ['A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city': ['Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender': ['M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'favourite_color': ['red', np.nan, 'yellow', np.nan, 'black', 'green', 'red']
}

df = pd.DataFrame(data)


grouped_colors = df.groupby('city')['favourite_color'].apply(list)
print("Grouped Colors According to City:\n", grouped_colors)

filtered_df = df[df['age'] < 20][['gender', 'favourite_color']]
print("\nGender and Favorite Color of Persons with Age < 20:\n", filtered_df)


df['favourite_color'].fillna('orange', inplace=True)
print("\nDataFrame after filling NaN in favorite_color:\n", df)


unique_cities = df['city'].unique()
print("\nUnique City Names:\n", unique_cities)


gender_count = df['gender'].value_counts()
print("\nCount of Males and Females:\n", gender_count)


avg_age_per_city = df.groupby('city')['age'].mean()
print("\nAverage Age Group of Each City:\n", avg_age_per_city)


total_age_per_section = df.groupby('section')['age'].sum()
print("\nTotal Age Per Section:\n", total_age_per_section)

people_per_city = df['city'].value_counts()
print("\nNumber of Persons in Each City:\n", people_per_city)
