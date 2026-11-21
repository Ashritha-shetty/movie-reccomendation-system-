import pandas as pd

def get_movies():

    data = {
        "Index": range(1, 11),

        "Movie": [
            "Avengers",
            "Iron Man",
            "Thor",
            "Titanic",
            "The Notebook",
            "Interstellar",
            "Inception",
            "The Dark Knight",
            "Avatar",
            "Joker"
        ],

        "Genre": [
            "Action",
            "Action",
            "Action",
            "Romance",
            "Romance",
            "Sci-Fi",
            "Sci-Fi",
            "Action",
            "Sci-Fi",
            "Crime"
        ]
    }

    return pd.DataFrame(data)