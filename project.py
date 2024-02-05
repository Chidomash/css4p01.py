# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:03:39 2024

@author: Chido
"""

import pandas as pd
df = "Data Frame"

df = pd.read_csv("C:/Users/Chido/Downloads/movie_dataset.csv")

print(df)

#cleaning data 
df.columns = df.columns.str.replace(' ', '')

pd.set_option('display.max_rows', None)

print(df)

#removing the NANs
x = df["Revenue(Millions)"].mean()

df["Revenue(Millions)"].fillna(x, inplace=True)

x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace = True) 
print(df)

#Question 1
df.sort_values(by="Rating", ascending=False, inplace=True)


#Question2
df = df["Revenue(Millions)"].mean()
print(df)


#Question 3
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]     
print(df)
print(df.describe())

#Quesion 4

df= df[df['Year'] == 2016].shape[0]
print(df)


#Question 5
count_rows= (df['Director'] == 'Christopher Nolan').sum()
print(count_rows)

#Question 6
high_rating_count = len(df[df['Rating'] >= 8.0])
print(high_rating_count)

#Question 7
df= df[df['Director'] == 'Christopher Nolan']['Rating'].median()
print(df)

#Question 8
average_ratings_by_year = df.groupby('Year')['Rating'].mean()
print(average_ratings_by_year)


#Question 9   
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016] 

# Calculate the number of movies in each year
count_2006 = len(movies_2006)
count_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100
print(f"The percentage increase in the number of movies between 2006 and 2016 is: {percentage_increase:.2f}%")

#Question 10

#Split the multiple actor names in the Acrors colunmn and create the list of all actors
all_actors = df['Actors'].str.split(',').explode()


# Find the most common actor
most_common_actor = actors_series.mode().iloc[0]

# Display the result
print(f"The most common actor in all movies is: {most_common_actor}")


#Question 11
# Split the genres string and create a set of unique genres
unique_genres = set('|'.join(df['Genre'].astype(str)).split('|'))

# Remove empty strings from the set (if any)
unique_genres.discard('')

# Calculate the number of unique genres
num_unique_genres = len(unique_genres)

# Display the result
print(f"The number of unique genres in the dataset is: {num_unique_genres}")

#Question 12
numerical_features = df.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
correlation_matrix = numerical_features.corr()

# Display the correlation matrix
print(correlation_matrix)
