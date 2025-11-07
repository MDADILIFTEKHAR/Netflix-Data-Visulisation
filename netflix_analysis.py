import os
import pandas as pd
import matplotlib.pyplot as plt

# Path / load
csv_path = 'netflix_titles.csv'   # change if file is elsewhere
print("Working dir:", os.getcwd())
df = pd.read_csv(csv_path)

# Quick checks
print("Rows, cols:", df.shape)
print("Columns:", df.columns.tolist())
print("Type values:", df['type'].unique())
print("Rating values sample:", df['rating'].unique()[:10])

# Drop rows missing required columns
df = df.dropna(subset=['type', 'release_year', 'rating', 'duration'])

# ---- Bar chart: Movie vs TV Show counts ----
type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue','orange'])
plt.title('Number of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('Movies_vs_TVShows.png', bbox_inches='tight')
plt.show()
plt.close()

# ---- Pie chart: content rating distribution ----
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')   # keep pie circular
plt.title('Percentage of Content Rating')
plt.tight_layout()
plt.savefig('content_Rating_pie.png', bbox_inches='tight')
plt.show()
plt.close()

# ---- Histogram: movie duration distribution ----
# Ensure the 'type' exact string matches your data (check above)
movie_df = df[df['type'].str.lower() == 'movie'].copy()  # case-insensitive filter
# Extract digits safely (handles '90 min', '95 min', etc.)
movie_df['duration_int'] = movie_df['duration'].str.extract(r'(\d+)').astype(int)

# Basic stats to help interpretation
print(movie_df['duration_int'].describe())

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, edgecolor='black')  # color optional
plt.title('Distribution of Movie Duration (minutes)')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('Movie_duration_histogram.png', bbox_inches='tight')
plt.show()
plt.close()
