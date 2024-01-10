# Sentiment Analysis on Tweets
This project focuses on performing sentiment analysis on a vast dataset of tweets using various techniques and models to derive insights into the sentiment conveyed in the tweets.

# Sentiment Analysis on Tweets
This project focuses on performing sentiment analysis on a vast dataset of tweets using various techniques and models to derive insights into the sentiment conveyed in the tweets.

# Project Phases
**1. Data Preparation and Cleaning**
* Utilized a tweet dataset consisting of approximately 1.6 million tweets.
* Conducted data cleaning procedures to ensure quality and consistency for analysis.
  
**2. Initial Algorithm Testing**
Experimented with Python algorithm libraries such as TextBlob and VADER for sentiment analysis.

**3. NLP Libraries and Word Cloud Creation**
* Implemented NLTK for creating word clouds of positive and negative terms.
* Used these datasets to identify positive and negative sentiment within the tweets.

**4. Transition to Pretrained Models**
* Due to limitations with smaller datasets, shifted focus to pretraining models like BERT (uncased and cased) and other models available through Hugging Face.

**5. Fine-Tuning Pretrained Models**
* Discovered and fine-tuned models specifically trained for sentiment analysis on tweet data, such as TweetBERT and RoBERTa.
* After testing and comparison, found RoBERTa to perform exceptionally well in sentiment analysis.

**6. Validation and Accuracy Checking**
* Cross-checked sentiment manually.
* Utilized ChatGPT and passed sample tweets for additional validation, ensuring accuracy.

**7. Tweet Retrieval and Sentiment Analysis**-
* Applied regex to search the dataset for tweets relevant to specific keywords.
* Utilized RoBERTa model for sentiment analysis on the filtered dataset.

# Achievements
* Successfully processed and analyzed a vast dataset of tweets for sentiment analysis.
* Employed a multi-stage approach, integrating traditional NLP techniques and state-of-the-art pre-trained models.
* Validated results through multiple means, ensuring high accuracy in sentiment classification.
* Identified and implemented RoBERTa as the optimal model for accurate sentiment analysis on Twitter data.

# How to Use
**1. Clone the Repository**
> git clone <repository-url>
> cd <repository-name>

**2. Environment Setup**
* Ensure Python (version x.x) and required dependencies are installed. Use a virtual environment for isolation if preferred.
> pip install -r requirements.txt

**3. Dataset Preparation**
* The original dataset can be found at https://www.kaggle.com/datasets/kazanova/sentiment140.
* Follow instructions in data_preparation.md to preprocess and clean the dataset.

**Running Sentiment Analysis**
* Refer to sentiment_analysis.py for an example of how to utilize the RoBERTa model for sentiment analysis on tweets.

**Contributing**
Contributions are welcome! Please feel free to fork this repository and submit pull requests or open issues for discussion.

**License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
