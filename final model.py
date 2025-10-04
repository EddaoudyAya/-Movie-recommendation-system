import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_similarity():
    data = pd.read_csv('data1.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data, similarity

def rcmd(m):
    m = m.lower().strip()  # Convert to lowercase and remove leading/trailing whitespaces
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    # Perform case-insensitive comparison and remove leading/trailing whitespaces from movie titles in the dataset
    data_titles = data['movie_title'].str.lower().str.strip()
    if m not in data_titles.unique():
        return 'Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies'
    else:
        i = data_titles[data_titles == m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        lst = lst[1:11]  # excluding first item since it is the requested movie itself
        recommended_movies = [data['movie_title'][a] for a, _ in lst]
        return recommended_movies


# Example usage
user_input = input("Enter a movie title: ")
recommendations = rcmd(user_input)
if isinstance(recommendations, str):
    print(recommendations)
else:
    print("Recommended movies for '{}':".format(user_input))
    for movie in recommendations:
        print(movie)