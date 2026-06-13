import streamlit as st
import pickle

import requests

# Load data
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

movies_list = movies['title'].values

st.header("Movies Recommender System")

# Dropdown for movie selection
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

# API_KEY = "c66ec16a34d3689c86820c72fc7a22ec"

# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     data = requests.get(url)
#     data = data.json()
#     poster_path=data['poster_path']
#     full_path= "https://image.tmdb.org/t/p/w500" + poster_path['poster_path']
#     # full_path= "https://image.tmdb.org/t/p/w500" + poster_path
#     return full_path

def fetch_poster(movie_id):
    api_key = "c66ec16a34d3689c86820c72fc7a22ec"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

# def fetch_poster(movie_id):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500" + poster_path
#         else:
#             return "https://via.placeholder.com/300x450?text=No+Poster"
#     except Exception as e:
#         print(f"Error fetching poster: {e}")
#         return "https://via.placeholder.com/300x450?text=Error"



# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster=[]
    for i in distance[1:6]:  
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie,recommend_poster

# Show recommendations
if st.button("Show Recommend"):
    movie_name,movie_poster = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
