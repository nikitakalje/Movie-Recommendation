import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

from matplotlib import *
import sys
import pylab as pl

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
path = 'ratings.tsv'

df = pd.read_csv(path, sep='\t', names = column_names)
df.head()

movie_titles = pd.read_csv('movieTitles.csv')
movie_titles.head()

data = pd.merge(df,movie_titles,on='item_id')
data.head()

#write what you are doing the grouping by, in this case title
data.groupby('title')['rating'].mean().sort_values(ascending=False).head()
data.groupby('title')['rating'].count().sort_values(ascending=False).head()

ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of rating'] = pd.DataFrame(data.groupby('title')['rating'].count())


ratings.head()


movieContent = data.pivot_table(index='user_id', columns='title', values='rating')
movieContent.head()


#sort values 
ratings.sort_values('num of rating', ascending=False).head(10)

#wonderland_user_ratings = movieContent['Wonderland (1997)']

toyStory_user_ratings = movieContent['Toy Story (1995)']
dalmatians_user_ratings = movieContent['101 Dalmatians (1996)']
#toyStory_user_ratings = movieContent['Star Wars (1977)']

#starwars_user_ratings.head()
toyStory_user_ratings.head()

#dalmations_user_ratings.head()

#print(movie_titles)
#print(data)
#print(ratings)

#checking correlation similar to the toy story movie
similar_to_toyStory = movieContent.corrwith(toyStory_user_ratings)

#checking correlation similar to the 101dalmatians movie
similar_to_dalmatians = movieContent.corrwith(dalmatians_user_ratings)

corr_toyStory= pd.DataFrame(similar_to_toyStory, columns=['Correlation'])
corr_toyStory.dropna(inplace = True)

corr_toyStory.head()

corr_toyStory.sort_values('Correlation',ascending=False).head(10)
corr_toyStory=corr_toyStory.join(ratings['num of rating'])

corr_toyStory.head()

#should be over than 100 because we are picking a good quality movie
corr_toyStory[corr_toyStory['num of rating'] > 500].sort_values('Correlation', ascending=False).head()

#print(toyStory_user_ratings)
print(corr_toyStory)

#VISUALIZATION part
sns.set_style('whitegrid')
#%matplotlib inline


#sort by average rating
data.groupby('title')['rating'].mean().sort_values(ascending=False).head()
print(data)
#print(movie_titles)

#data.head()

#sort by the amount of ratings
data.groupby('title')['rating'].count().sort_values(ascending=False).head()
#print(ratings)
print(data)

ratings=pd.DataFrame(data.groupby('title')['rating'].mean())
ratings.head()
print(ratings)

ratings['num of ratings']=pd.DataFrame(data.groupby('title')['rating'].count())
ratings.head()
print(ratings)

#histograms
#plt.figure(figsize=(10,4))
f=pl.Figure(figsize=(10,4))
ratings['num of ratings'].hist(bins=70)

#showing the graph
pl.show()


f=pl.Figure(figsize=(10,4))
ratings['rating'].hist(bins=70)
pl.show()

sns.jointplot(x='rating',y='num of ratings', data=ratings, alpha=0.5)
pl.show()
