import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

g = plt.subplots_adjust(left=0.2, right=0.8) 
g= plt.xticks(rotation=45, ha='right')


input ("Hello this is a  trial system that filter what you want to knwo next movie \n based on your prefrences \n Press Enter to continue: ")
print("Welcome to Movie Analyzer!")
print("Press the following number if you want to know about:\n 1. Top Rated Movies\n 2. Movies by Genre\n 3. Movies by Year\n 4. Exit")
choice = input("Enter your choice (1-4): ")

try :
    choice = int(choice) 
    df = pd.read_csv("movie_metadata.csv")
    if choice == 1:
        top_rated = df.sort_values(by="imdb_score", ascending=False).head(10)
        sns.barplot(y='imdb_score', x='movie_title', data=top_rated, palette='viridis')
        plt.show()
    elif choice == 2:
        genre = input("Enter the genre you are interested in (e.g., Action, Comedy, Drama): ")
        genre_movies = df[df['genres'].str.contains(genre, case=False, na=False)]
        # adding limit to genre input
        genre_movies = genre_movies.sort_values(by="imdb_score", ascending=False).head(10)
        sns.countplot(y='movie_title', data=genre_movies, order=genre_movies['movie_title'].value_counts().index, palette='coolwarm')
        plt.xticks(rotation=45, ha='right')
        plt.show()
    elif choice == 3:
        year = input("Enter the release year you are interested in (e.g., 2000, 2010): ")
        year_movies = df[df['title_year'] == int(year)] # ading limit to year input 
        year_movies = year_movies.sort_values(by="imdb_score", ascending=False).head(10)
        sns.countplot(y='movie_title', data=year_movies, order=year_movies['movie_title'].value_counts().index, palette='magma')
        
        plt.show()
    elif choice == 4:
        print("Exiting the Movie Analyzer. Goodbye!")
        exit()
except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")

finally:
    print("Thank you for using the Movie Analyzer!")