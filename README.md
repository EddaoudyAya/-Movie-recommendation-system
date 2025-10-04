# 🎬 Movie Recommendation System  

A **movie recommendation system** built with **Flask** that combines **collaborative filtering** and **NLP-based sentiment analysis** to provide personalized film suggestions.  
The project includes both the **backend logic** (Flask, machine learning models) and a **web interface** (HTML/CSS/JS).  

---

## Project Goals  
- Build a recommendation engine that suggests movies similar to the ones a user likes.  
- Use **text features** and **similarity metrics** to enhance recommendations.  
- Provide an easy-to-use **web interface** for interaction.  

---

## Features  
Movie search with autocomplete functionality.  
Top-10 personalized recommendations using collaborative filtering.  
Sentiment analysis of reviews (via pre-trained NLP models).  
Interactive web app built with Flask, HTML, CSS, and JavaScript.  

---

## Tech Stack  
- **Programming Language**: Python  
- **Framework**: Flask  
- **Machine Learning**: scikit-learn, pickle (saved models)  
- **Data Handling**: Pandas, NumPy  
- **Frontend**: HTML, CSS, JavaScript  
- **Notebooks**: Jupyter (for preprocessing, collaborative filtering, sentiment analysis, visualization)  

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
- **Data Aggregation**: Combined multiple datasets including `movie_metadata`, `credits`, and `movies_metadata` from Kaggle
- **Comprehensive Coverage**: Integrated diverse data sources to ensure robust and complete movie information
- **Cross-Referencing**: Established relationships between different data tables for comprehensive analysis

### Web Scraping for Recent Films
- **Wikipedia Integration**: Automated extraction of movie titles from Wikipedia pages for years 2016-2024
- **Dynamic Data Collection**: Implemented scraping scripts to gather up-to-date film information
- **Structured Parsing**: Converted unstructured web data into structured format for analysis

### TMDB API Enrichment
- **Data Augmentation**: Used The Movie Database API to fill missing information
- **Function Development**: Created specialized functions (`get_genre`, `get_director`, `get_actor`) to extract specific movie attributes
- **Real-time Data Access**: Leveraged API capabilities to access current and comprehensive movie data

### Data Cleaning and Preprocessing
- **Normalization**: Standardized data formats across all datasets
- **Missing Value Handling**: Implemented strategies to address incomplete or missing data
- **Feature Engineering**: Created combined features (e.g., 'comb' column) to enhance recommendation quality
- **Data Validation**: Ensured data consistency and accuracy throughout the pipeline

## 2. Recommendation Model

### Content-Based Approach Selection
- **Comparative Analysis**: Evaluated both collaborative filtering and content-based approaches
- **Performance Optimization**: Selected content-based method due to superior performance metrics
- **Cold Start Solution**: Addressed new user and new movie challenges effectively

### Cosine Similarity Matrix
- **Vectorization**: Used CountVectorizer to convert movie features into numerical vectors
- **Similarity Computation**: Implemented cosine similarity to measure movie-to-movie relationships
- **Matrix Construction**: Built comprehensive similarity matrix covering all movies in the dataset

### Feature Combination Strategy
- **Multi-dimensional Features**: Combined genre, director, actors, and other metadata
- **Feature Weighting**: Applied appropriate weights to different feature types based on importance
- **Text Processing**: Processed combined features to create meaningful movie representations

### Recommendation Function
- **Top-N Selection**: Returns 10 most similar movies for any given input film
- **Error Handling**: Includes robust error management for movies not found in database
- **Case Insensitivity**: Processes user input with case normalization for better matching
- **Duplicate Prevention**: Excludes the input movie itself from recommendations

## 3. Sentiment Analysis

### User Review Classification
- **Review Processing**: Analyzed user comments and reviews from multiple sources
- **Sentiment Categorization**: Classified reviews into positive, negative, or neutral sentiments
- **Real-time Analysis**: Implemented live sentiment analysis for user-generated content

### Naïve Bayes Implementation
- **High Accuracy**: Achieved 98.77% accuracy in sentiment classification
- **Model Training**: Used multinomial Naïve Bayes classifier for text classification
- **Performance Validation**: Tested model on separate datasets to ensure generalizability

### TF-IDF Feature Extraction
- **Text Vectorization**: Applied Term Frequency-Inverse Document Frequency for text processing
- **Feature Importance**: Weighted terms based on their importance in distinguishing sentiments
- **Dimensionality Reduction**: Focused on most relevant features for efficient classification
- **Vocabulary Optimization**: Built comprehensive vocabulary from movie review corpus

### Model Integration
- **Pickle Serialization**: Saved trained models and transformers for efficient deployment
- **Real-time Processing**: Enabled immediate sentiment analysis for user interactions
- **Scalable Architecture**: Designed system to handle increasing volumes of user reviews

---
## Screenshots

**Home Page of the Application**  
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
- [Bnyiche Mouna](https://github.com/itsmawna) 
- [Ahnin Chaimaa](https://github.com/chaimaa-101) 
- [Eddaoudy Aya](https://github.com/EddaoudyAya) 
- [El Alami Nihad](https://github.com/nihadel7) 

---
## Have Fun!

Have fun trying it out! Feel free to reach out if you have any questions, suggestions, or just want to chat about the project. 

