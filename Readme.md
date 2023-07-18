# Movie Recommender System

## Overview

This Movie Recommender System is built using Python and Streamlit. It recommends similar movies based on user input and utilizes a dataset of movies along with their tags and features.

## Dataset

The dataset used for this project is the TMDB Movie Metadata, which contains information about thousands of movies, including their titles, genres, keywords, cast, crew, and overview.

## Getting Started

To run the Movie Recommender System locally, follow these steps:

1. Clone the repository:
   ```shell
   git clone https://github.com/arpitya/movie-recommender-system.git

2. Install the required ```dependencies```:
   ```shell
   Python 3.x
   pandas
   numpy
   scikit-learn
   nltk
   Streamlit

3. Run the Streamlit app ```app.py``` by executing the following command:
    ```
    streamlit run app.py 
    ```
4. Once the app is launched, you will see a dropdown menu to select a movie. Type the name of your favorite movie or choose one from the list.

5. Click on the "Show Recommendation" button to get a list of five recommended movies based on similarity.

6. The recommended movies will be displayed along with their posters, fetched using the TMDB API.


4. Once the app is launched, you will see a dropdown menu to select a movie. Type the name of your favorite movie or choose one from the list.

5. Click on the "Show Recommendation" button to get a list of five recommended movies based on similarity.

6. The recommended movies will be displayed along with their posters, fetched using the TMDB API.

## Dataset

The dataset used for this Movie Recommender System consists of movie information, including title, overview, genres, keywords, cast, and crew. The data is loaded from two CSV files: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`. [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv) from Kaggle.

## Data Preprocessing

The data is preprocessed to clean and transform the relevant features. The following steps are performed:

1. The genres, keywords, cast, and crew columns are extracted and converted to a more readable format.
2. Unnecessary columns are removed to create a consolidated dataset.
3. Text data (tags) is converted to lowercase and tokenized for vectorization.

## Text Vectorization

The text data (tags) is vectorized using the `CountVectorizer` from scikit-learn, converting text into numerical features to be used in similarity calculations.

## Similarity Calculation

Cosine similarity is used to calculate the similarity between movies based on their tags. The similarity matrix is saved as a pickled file for faster retrieval during recommendation.

## Recommendations

Based on the selected movie, the app retrieves similar movies from the similarity matrix and displays their titles and posters.

## API Key

Please note that the app uses the TMDB API to fetch movie posters. An API key is required to access the TMDB API. Make sure to replace the placeholder API key in `fetch_poster()` function in `app.py` with your valid API key. 



## Acknowledgements

The Movie Recommender System is developed as a personal project.

## Created by 

[Arpitya Kumar Singh](https://www.github.com/arpitya)

