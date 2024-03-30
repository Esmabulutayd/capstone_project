# Import numpy, pandas, spaCy, TextBlob libraries
import numpy as np
import pandas as pd
import spacy
from textblob import TextBlob

# Load the dataset into a pandas DataFrame
# Display the first five rows 
dataframe = pd.read_csv('C:/Users/Esma/Downloads/archive/amazon_product_reviews.csv')
dataframe.head()

# Assign reviews.text column to reviews_text
# Show total number of the reviews
reviews_text = dataframe['reviews.text']
print(reviews_text.shape)

# Check number of empty rows
reviews_text.isnull().sum()

# Drop rows where reviews are missing and show number of the reviews 
reviews_text.dropna(inplace = True, axis = 0)
print(reviews_text.shape)

# Print the reviews_text
reviews_text

# Load the spaCy simple model
nlp = spacy.load('en_core_web_sm')

# Define a function to preprocess review text
# Use the spaCy NLP library to process the cleaned text, performing tokenization
# Generate a list of lemmatized tokens from the processed text, excluding stopwords and punctuation
# Concatenates the lemmatized tokens back into a single string

def preprocess(text):
    
    doc = nlp(text.lower().strip())
    processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    
    return ' '.join(processed)

# Apply preprocess function to clean the reviews
reviews_text_processed = reviews_text.apply(preprocess)

# Show the preprocessed reviews
reviews_text_processed

# Extract reviews_text_processed into an array and assign it 'data'
data = reviews_text_processed.values
data

# Define a function for sentiment analysis using TextBlob
# This function utilizes TextBlob to compute the sentiment polarity of the input review text. 
# The polarity score is a float within the range [-1.0, 1.0] where -1.0 signifies a negative 
# sentiment, 1.0 signifies a positive sentiment, and values around 0 represent neutral sentiments.
# parameter: The review text whose sentiment polarity is to be analyzed
# return: The polarity score of the review, indicating the sentiment of the text

def analyze_polarity(text):
    
    # Analyze sentiment with TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    return polarity

# Initialize an empty list to store the sentiments of each item
# This loop iterates through each item in the 'data' iterable 
# and analyzes its polarity score using a function called 'analyze_polarity'. 
# Based on the polarity score, it determines the sentiment of the item as 'positive', 'negative', or 'neutral', 
# and appends the determined sentiment to the 'sentiments' list.

sentiments = []

for item in data: 
    # Analyze the polarity score of the item
    polarity_score = analyze_polarity(item)

    # Determine the sentiment based on the polarity score
    if polarity_score > 0:
        sentiment = 'positive'
    elif polarity_score < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    # Append the determined sentiment to the 'sentiments' list
    sentiments.append(sentiment)

    sentiments

    # count number of positive, negative and neutral sentiments
positive_count = sentiments.count('positive')
negative_count = sentiments.count('negative')
neutral_count = sentiments.count('neutral')

# Find the lenght of the list 
total = len(sentiments)

# Calculate percentage of each sentiment
positive_perc = (positive_count / total) * 100
negative_perc = (negative_count / total) * 100
neutral_perc = (neutral_count / total) * 100

# print the percentages to understand the sentiment
print(f"Positive percentage: {positive_perc:.2f}%")
print(f"Negative percentage: {negative_perc:.2f}%")
print(f"Neutral percentage: {neutral_perc:.2f}%")

# Load a larger spaCy model 
nlp = spacy.load('en_core_web_md')

# Import the random module and generate two numbers with the upper limit constrained by the length of the data
import random

index_a = random.randint(1, len(reviews_text))
index_b = random.randint(1, len(reviews_text))

# Retrieve and print the random 2 reviews based on index numbers generated by the random module.

review_a = reviews_text.iloc[index_a]
review_b = reviews_text.iloc[index_b]
print('Comparing 2 random reviews:')   
print("Review A:", review_a, '\n')
print("Review B:", review_b, '\n')

# Calculate and print the similarity score of the two reviews
doc_a = nlp(review_a)
doc_b = nlp(review_b)    
similarity_score = doc_a.similarity(doc_b)
print(f'Similarity score of the two reviews: {round(similarity_score,3)}')