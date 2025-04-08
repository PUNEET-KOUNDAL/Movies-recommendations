# Movies-recommendations

A recommendation system that suggests movies based on user preferences using machine learning and collaborative filtering techniques

![Screenshot 2025-04-08 203126](https://github.com/user-attachments/assets/a59b50ee-d471-4e3b-954a-b6d6ebe8519f)


.

## Project Overview

This project provides a recommendation system for suggesting movies to users based on their historical ratings and preferences. It uses a dataset of movies and ratings to build a model that predicts movies a user might like. The recommendation system can be used in various movie-streaming platforms to enhance user experience by suggesting personalized content.

## Features

- **Personalized Movie Recommendations**: Provides movie suggestions based on user preferences and rating history.
- **Collaborative Filtering**: Implements a collaborative filtering model using user-item interactions.
- **Movie Data**: Uses a dataset with movie information (title, genre, etc.) and user ratings.

## Dataset

The system uses the following datasets:
- **Movies Dataset**: Contains movie details (e.g., movie title, genres, etc.).
- **Ratings Dataset**: Contains user ratings for each movie.

The dataset used in this project can be found [[here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)] or can be replaced with any similar movie recommendation dataset.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/PUNEET-KOUNDAL/Movies-recommendations.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Movies-recommendations
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    (till now we dont have requirement.txt (v2) ,
   pip install streamlit
   
   pip install pickle5
   
   pip install sklearn
   
   pip install numpy as np
   
   pip install pandas as pd)
   
   

## Usage

1. **run**:
   
   ```bash
   streamlit run app.py

