import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#reading csv file
df = pd.read_csv("movies.csv")

features = ['title', 'genres']

#make everything into single column
for feature in features:
    df[feature] = df[feature].fillna("")

def combined_features(row):
    try:
        return row['title']+ " "+ row['genres']
    except:
        print("Error:", row)
    
df["combined_features"] = df.apply(combined_features, axis=1)

#make count matrix
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

cosineSim= cosine_similarity(count_matrix)

userLikes = "Toy Story (1995)"

def get_title(index):
    return df[df.index ==index]["title"].values[0]

def get_index(title):
    return df[df.title == title]["movieId"].values[0]

movieIdx = get_index(userLikes)
similarMovies = list(enumerate(cosineSim[movieIdx]))

#get similar movies in descending order of how similar
similarMoviesSorted = sorted(similarMovies, key= lambda x: x[1], reverse = True)

i=0;
for movie in similarMoviesSorted:
    print(get_title(movie[0]))
    i = i+1;
    if i>50:
        break
