import pandas as pd

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

