import streamlit as st
import pandas as pd
import pickle
import requests
import gdown
import os

# Function to download the similarity.pkl file from the Google Drive link
def download_similarity_file():
    url = "https://drive.google.com/uc?id=1qipLpH7FtL0dyeaV44WHqKv2tzJUzL8d"
    output_path = "similarity.pkl"
    gdown.download(url, output_path, quiet=False)

# Check if similarity.pkl exists locally, if not, download it
if not os.path.isfile('similarity.pkl'):
    download_similarity_file()

st.header('Movie Recommender System')

# Convert the dictionary to a DataFrame
movies = pd.DataFrame.from_dict(pickle.load(open('movies_dict.pkl', 'rb')))

# Load the similarity data from the downloaded file
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b2dc8a7e129cd35248f408f7764221c0&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(len(cols)):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
