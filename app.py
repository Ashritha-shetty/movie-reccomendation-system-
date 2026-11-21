import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from index import get_movies

# Page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# Load CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Load dataset
movies = get_movies()

# Machine Learning
tfidf = TfidfVectorizer()

matrix = tfidf.fit_transform(movies["Genre"])

similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(movie_name):

    movie_index = movies[
        movies["Movie"] == movie_name
    ].index[0]

    scores = list(enumerate(similarity[movie_index]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in scores[1:6]:

        recommendations.append({
            "Index": movies.iloc[index]["Index"],
            "Movie": movies.iloc[index]["Movie"],
            "Genre": movies.iloc[index]["Genre"]
        })

    return recommendations


# Application title
st.title("🎬 Movie Recommendation System")

st.write("### Find Movies You Will Love ❤️")

st.write("---")

# Movie dataset
st.subheader("🍿 Available Movies")

st.dataframe(
    movies,
    hide_index=True,
    use_container_width=True
)

# Movie selection
st.subheader("🔍 Select Your Favorite Movie")

selected_movie = st.selectbox(
    "Choose a movie:",
    movies["Movie"]
)

# Recommendation button
if st.button("✨ Recommend Movies"):

    results = recommend(selected_movie)

    st.subheader("🎯 Recommended Movies")

    for movie in results:

        st.markdown(
            f"""
            <div class="movie-card">
                <h3>🎥 {movie['Index']}. {movie['Movie']}</h3>
                <p>Genre: {movie['Genre']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

st.caption("Built with Python | Machine Learning ❤️")