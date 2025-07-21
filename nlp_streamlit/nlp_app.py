import streamlit as st
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
import re

nltk.download('wordnet')

# Create a GUI that takes user input for sentiment analysis
# Provide a title
st.title("Sentiment Analysis App")
st.subheader("Sentiment Analysis App")
# Define a text area for user input
text = st.text_area("Enter text for sentiment analysis:")
# Create a button analyze that will return the sentiment polarity and sentiment for the given text
analyze = st.button("Analyze")

# Process the cleaned text when the analyze button is clicked
# if st.button("Analyze"):
if analyze:
    # Keeping only Text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    # Removes Whitespaces
    text = re.sub(r"\'s", " ", text)
    # Removing Links if any
    text = re.sub(r"http\S+", " link ", text)
    # Removes Punctuations and Numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # Splitting Text
    text = text.split()
    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)

    # Create a TextBlob object
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    # Display different alerts st.success for positive sentiment, st.warning for neutral sentiment, and st.error for negative sentiment
    if sentiment_score > 0:
        custom_emoji = ':blush:'
        st.success('Happy : {}'.format(custom_emoji))
    elif sentiment_score < 0:
        custom_emoji = ':disappointed:'
        st.error('Sad : {}'.format(custom_emoji))
    else:
        custom_emoji = ':confused:'
        st.info('Confused : {}'.format(custom_emoji))
    st.success("Polarity Score is: {}".format(sentiment_score))
