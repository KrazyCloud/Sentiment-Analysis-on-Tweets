import pandas as pd
import streamlit as st

def categorize_tweets(tweet_data, search_list):
    # Create a dictionary to store tweets for each category
    category_tweets = {keyword: [] for keyword in search_list}

    # Categorize tweets based on keywords
    for index, row in tweet_data.iterrows():
        tweet_text = row['tweet']
        added_to_category = False  # Flag to track if tweet is added to a category

        for keyword in search_list:
            if keyword in tweet_text.lower() and not added_to_category:
                category_tweets[keyword].append((tweet_text, index))
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

        #tweet_data = pd.read_csv(uploaded_file).head(num_rows)
        tweet_data = pd.read_csv(uploaded_file, skiprows=range(1, start_row), nrows=end_row-start_row)
        st.write("File uploaded successfully!")

        # Keyword input
        keyword_input = st.text_input("Enter keyword(s) separated by space")

        if st.button("Search"):
            search_list = keyword_input.lower().split()  # Split keywords by space
            category_tweets = categorize_tweets(tweet_data, search_list)

            # Display categorized tweets
            for keyword in search_list:
                st.subheader(f"Tweets related to '{keyword}': {len(category_tweets[keyword])}")
                for tweet_data in category_tweets[keyword]:
                    st.write(f"- Tweet {tweet_data[1]}: {tweet_data[0]}")
                st.write("---")

def main():
    tweet_categorization_app()

if __name__ == "__main__":
    main()
