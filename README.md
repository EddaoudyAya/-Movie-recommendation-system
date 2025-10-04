# 🎬 Movie Recommendation System

A **movie recommendation system** built with **Flask** that combines **collaborative filtering** and **NLP-based sentiment analysis** to provide personalized film suggestions.
The project includes both the **backend logic** (Flask, machine learning models) and a **web interface** (HTML/CSS/JS).

---

## Project Goals

* Build a recommendation engine that suggests movies similar to the ones a user likes.
* Use **text features** and **similarity metrics** to enhance recommendations.
* Provide an easy-to-use **web interface** for interaction.
* Integrate **sentiment analysis** for richer insights into user reviews.
* Enrich movie data dynamically using **web scraping** and the **TMDB API**.

---

## Features

* Movie search with autocomplete functionality.
* Top-10 personalized recommendations using collaborative filtering and content-based filtering.
* Sentiment analysis of reviews (via pre-trained NLP models).
* Visual exploration of data (genre distribution, actor frequency, ratings).
* Interactive web app built with Flask, HTML, CSS, and JavaScript.
* Actor exploration (view actor profiles and related films).
* Robust error handling (case insensitivity, missing movies, duplicate prevention).

---

## Tech Stack

* **Programming Language**: Python
* **Framework**: Flask
* **Machine Learning**: scikit-learn, pickle (saved models)
* **Data Handling**: Pandas, NumPy
* **Visualization**: Matplotlib, Seaborn (used in analysis)
* **Frontend**: HTML, CSS, JavaScript
* **Notebooks**: Jupyter (for preprocessing, collaborative filtering, sentiment analysis, visualization)

---

## Sources of the Datasets

1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
3. [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data?select=tmdb_5000_movies.csv)
4. [List of American Films of 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
5. [List of American Films of 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
6. [List of American Films of 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)
7. [List of American Films of 2021](https://en.wikipedia.org/wiki/List_of_American_films_of_2021)
8. [List of American Films of 2022](https://en.wikipedia.org/wiki/List_of_American_films_of_2022)
9. [List of American Films of 2023](https://en.wikipedia.org/wiki/List_of_American_films_of_2023)
10. [List of American Films of 2024](https://en.wikipedia.org/wiki/List_of_American_films_of_2024)

---

# Methodology

## 1. Data Preparation

### Multi-Dataset Collection and Integration

* **Data Aggregation**: Combined multiple datasets including `movie_metadata`, `credits`, and `movies_metadata` from Kaggle.
* **Comprehensive Coverage**: Integrated diverse data sources to ensure robust and complete movie information.
* **Cross-Referencing**: Linked data tables for deeper analysis.

### Web Scraping for Recent Films

* **Wikipedia Integration**: Automated scraping of film lists (2016–2024).
* **Dynamic Updates**: Ensures coverage of the latest releases.
* **Structured Parsing**: Converted scraped HTML tables into structured datasets.

### TMDB API Enrichment

* **Data Augmentation**: Filled missing attributes (genres, directors, actors).
* **Function Development**: Implemented helper functions (`get_genre`, `get_director`, `get_actor1/2/3`).
* **Real-time Data Access**: Updated missing metadata directly from TMDB.

### Data Cleaning and Preprocessing

* **Normalization**: Standardized columns (genres, runtime, votes).
* **Missing Value Handling**: Strategies for empty fields.
* **Feature Engineering**: Created a combined text column (`comb`) merging title, director, actors, and genre.
* **User IDs Simulation**: Integrated synthetic user identifiers for collaborative filtering experiments.

---

## 2. Recommendation Models

### Collaborative Filtering

* **User-Based**: Finds users with similar tastes, recommends what they liked.
* **Item-Based**: Finds items similar to those rated highly by the user.
* **Limitations**: Cold-start problem, requires user history.

### Content-Based Filtering

* **Selected Approach**: Outperformed collaborative filtering in this project.
* **Cosine Similarity**: Computed on text vectors (CountVectorizer).
* **Top-N Recommendations**: Returns 10 most similar films.
* **Advantages**: Works even for new users (no rating history).

### Feature Combination Strategy

* **Multi-dimensional Metadata**: Genre, director, actors.
* **TF-IDF**: Applied for weighting review text.
* **Weighted Features**: Adjusted contributions of actors vs. genres.

---

## 3. Sentiment Analysis

* **Dataset**: `reviews.txt` with labeled user reviews.
* **Preprocessing**: Stopword removal, TF-IDF vectorization.
* **Model**: Multinomial Naïve Bayes.
* **Accuracy**: ~98.77% on test sets.
* **Integration**: Stored via Pickle for real-time predictions in Flask.
* **User Interface**: Visualizes sentiment distribution (positive/negative/neutral).

---

## 4. Application Workflow

* **Homepage**: Search bar with autocomplete.
* **Movie Details Page**: Displays description, runtime, rating, votes, actors.
* **Actor Pages**: Dedicated actor profiles with filmography.
* **Recommendation Loop**: Suggested movies can themselves be clicked for further exploration.
* **Sentiment Visualization**: Displays opinions with emoji-based analysis.

---

## 5. Visualizations

* Top-10 Director Frequency (Spielberg, Eastwood dominate).
* Top-10 Genre Distribution (Drama, Comedy, Action most common).
* Actor Frequency (Robert De Niro, Bruce Willis, Morgan Freeman lead).
* Top Movies by Rating.
* Longest Movies by Runtime.
* Trends in Ratings Over Time.
* Count of Movies Released Per Year.
* Genre Distribution by Top Directors.

---

## Screenshots

**Home Page**
![Home Page](static/screenshots/Home%20Page.png)

**Movie Suggestions (Autocomplete)**
![Movie Suggestions](static/screenshots/Movie%20Suggestions.png)

**Description of the Searched Movie**
![Movie Description](static/screenshots/Movie%20Description.png)

**Actors of the Movie**
![Actors](static/screenshots/Actors.png)

**Actor Information**
![Actor Info](static/screenshots/Actor%20Info.png)

**User Reviews Analysis**
![Reviews Analysis](static/screenshots/Reviews%20Analysis.png)

**Recommendation Result**
![Recommendation Result](static/screenshots/Recommendation%20Result.png)

---

## Contributors

* [Bnyiche Mouna](https://github.com/itsmawna)
* [Ahnin Chaimaa](https://github.com/chaimaa-101)
* [Eddaoudy Aya](https://github.com/EddaoudyAya)
* [El Alami Nihad](https://github.com/nihadel7)

---

## Conclusion

This project demonstrates how combining **content-based recommendation**, **collaborative filtering exploration**, and **sentiment analysis** can yield a **robust, user-friendly movie recommendation app**. By leveraging multiple datasets, web scraping, and API augmentation, the system provides up-to-date, personalized film discovery.

---

## Have Fun!

Try it out and feel free to reach out for questions, suggestions, or discussions about the project.
