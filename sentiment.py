import pandas as pd
import streamlit as st
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from torch.nn.functional import softmax
import emoji

def categorize_tweets(tweet_data, search_list, model, tokenizer):
    # Create a dictionary to store tweets for each category
    category_tweets = {keyword: [] for keyword in search_list}

    # Process each text entry in the CSV file
    for index, row in tweet_data.iterrows():
        tweet_text = row['tweet']
        added_to_category = False  # Flag to track if tweet is added to a category

        for keyword in search_list:
            if keyword in tweet_text.lower() and not added_to_category:
                # Tokenize and encode the text
                inputs = tokenizer(tweet_text, return_tensors='pt', truncation=True)

                # Forward pass through the model
                outputs = model(**inputs)

                # Get probabilities for each class (e.g., positive, negative)
                probs = softmax(outputs.logits, dim=1).detach().numpy()[0]

                # Interpret results
                sentiment_labels = ['Negative', 'Neutral', 'Positive']
                predicted_sentiment = sentiment_labels[probs.argmax()]

                # Map sentiment labels to emojis
                emoji_mapping = {
                    'Negative': '😠',
                    'Neutral': '😐',
                    'Positive': '😊'
                }

                # Get the corresponding emoji for the predicted sentiment
                predicted_emoji = emoji_mapping.get(predicted_sentiment, '')

                category_tweets[keyword].append((tweet_text, index, predicted_emoji))
                added_to_category = True

    return category_tweets

def tweet_categorization_app():
    st.title("Tweet Categorization")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # User input for range of rows
        start_row = st.number_input("Enter the starting row number", min_value=1)
        end_row = st.number_input("Enter the ending row number", min_value=start_row+1)

        # Load pre-trained RoBERTa model and tokenizer
        roberta_model = "cardiffnlp/twitter-roberta-base-sentiment"
        model = AutoModelForSequenceClassification.from_pretrained(roberta_model)
        tokenizer = AutoTokenizer.from_pretrained(roberta_model)

        tweet_data = pd.read_csv(uploaded_file, skiprows=range(1, start_row), nrows=end_row-start_row)
        st.write("File uploaded successfully!")

        # Keyword input
        keyword_input = st.text_input("Enter keyword(s) separated by space")

        if st.button("Search"):
            search_list = keyword_input.lower().split()  # Split keywords by space
            category_tweets = categorize_tweets(tweet_data, search_list, model, tokenizer)

            # Display categorized tweets with sentiments marked by emojis
            for keyword in search_list:
                st.subheader(f"Tweets related to '{keyword}': {len(category_tweets[keyword])}")
                for tweet_data in category_tweets[keyword]:
                    st.write(f"- Tweet {tweet_data[1]}: {tweet_data[0]} {tweet_data[2]}")
                st.write("---")

def main():
    tweet_categorization_app()

if __name__ == "__main__":
    main()
