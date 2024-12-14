import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r'C:\Data Preparation\Endterm\IMDb Top 1000 Movies\IMDB top 1000.csv'
df = pd.read_csv(file_path)

df_cleaned = df.dropna()
df_cleaned = df_cleaned.drop_duplicates()


# 1. 
total_movies = len(df_cleaned)
print(f"Total number of movies: {total_movies}")

# 2. 
average_rating = df_cleaned['averageRating'].mean()
print(f"Average rating of all movies: {average_rating:.2f}")

# 3.
movies_by_genre = df_cleaned['genres'].value_counts()
print("Number of movies by genre:")
print(movies_by_genre)

# 4.
oldest_movie = df_cleaned.loc[df_cleaned['releaseYear'].idxmin()]
print(f"The oldest movie: {oldest_movie['title']} ({oldest_movie['releaseYear']})")

# 5.
newest_movie = df_cleaned.loc[df_cleaned['releaseYear'].idxmax()]
print(f"The newest movie: {newest_movie['title']} ({newest_movie['releaseYear']})")

# 6. 
top_movies = df_cleaned.nlargest(10, 'averageRating')[['title', 'averageRating']]
print("Top 10 movies by rating:")
print(top_movies)

# 7.
total_votes = df_cleaned['numVotes'].sum()
print(f"Total number of votes: {total_votes}")

# 8.
most_voted_movie = df_cleaned.loc[df_cleaned['numVotes'].idxmax()]
print(f"The movie with the highest number of votes: {most_voted_movie['title']} ({most_voted_movie['numVotes']} votes)")

# 9. 
average_votes = df_cleaned['numVotes'].mean()
print(f"Average number of votes per movie: {average_votes:.2f}")

# 10.
average_rating_by_genre = df_cleaned.groupby('genres')['averageRating'].mean().sort_values(ascending=False).head(10)
print("Top 10 genres by average rating:")
print(average_rating_by_genre)

# 11.
movies_21st_century = len(df_cleaned[df_cleaned['releaseYear'] >= 2000])
print(f"Number of movies released in the 21st century: {movies_21st_century}")

# 12.
movies_before_1950 = len(df_cleaned[df_cleaned['releaseYear'] < 1950])
print(f"Number of movies released before 1950: {movies_before_1950}")

# 13.
average_rating_after_2010 = df_cleaned[df_cleaned['releaseYear'] > 2010]['averageRating'].mean()
print(f"Average rating of movies released after 2010: {average_rating_after_2010:.2f}")

# 14. 
most_frequent_year = df_cleaned['releaseYear'].value_counts().idxmax()
print(f"The year with the most movie releases: {most_frequent_year}")

# 15. 
df_cleaned['decade'] = (df_cleaned['releaseYear'] // 10) * 10
movies_per_decade = df_cleaned['decade'].value_counts()
print("Number of movies per decade:")
print(movies_per_decade)

# 16. 
longest_titles = df_cleaned.loc[df_cleaned['title'].str.len().nlargest(5).index]
print("Top 5 movies with the longest titles:")
print(longest_titles[['title', 'releaseYear']])

# 17. 
unique_genres = df_cleaned['genres'].nunique()
print(f"Number of unique genres in the dataset: {unique_genres}")

# 18.
highly_voted_movies_rating = df_cleaned[df_cleaned['numVotes'] > 1_000_000]['averageRating'].mean()
print(f"Average rating of movies with more than 1 million votes: {highly_voted_movies_rating:.2f}")
