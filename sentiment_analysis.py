# import pandas as pd
# import nltk
# nltk.download('vader_lexicon')
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# # Load the CSV file into a pandas dataframe
# df = pd.read_csv('Asia.csv')

# # Create a new column for sentiment score
# df['sentiment_score'] = 0

# # Initialize the sentiment analyzer
# analyzer = SentimentIntensityAnalyzer()

# # Iterate over the rows of the dataframe and perform sentiment analysis
# for index, row in df.iterrows():
#     # Parse the date string into a datetime object
#     date = pd.to_datetime(row['Date'], format='%Y-%m-%d %H:%M:%S%z')
#     # Extract the month from the date column
#     month = date.strftime('%B')
#     # Perform sentiment analysis on the tweet using the analyzer
#     sentiment = analyzer.polarity_scores(row['Tweet'])['compound']
#     # Update the sentiment score for the row
#     df.at[index, 'sentiment_score'] = sentiment
#     # Print the sentiment score for debugging
#     print(f"Sentiment score for {row['Tweet']} is {sentiment} for {month}")

# # Group the dataframe by month and calculate the average sentiment score for each month
# month_groups = df.groupby(pd.Grouper(key='Date', freq='M'))
# for month, group in month_groups:
#     avg_sentiment = group['sentiment_score'].mean()
#     print(f"Average sentiment score for {month.strftime('%B %Y')} is {avg_sentiment}")


# import pandas as pd
# from textblob import TextBlob

# # Load CSV file
# df = pd.read_csv('Oceania.csv')

# # Clean up tweets by removing URLs, mentions, and hashtags
# df['clean_tweet'] = df['Tweet'].str.replace('http\S+|www.\S+|@\S+|#\S+', '', case=False)

# # Calculate sentiment score for each tweet
# df['sentiment'] = df['clean_tweet'].apply(lambda tweet: TextBlob(tweet).sentiment.polarity)

# # Calculate overall sentiment score for all tweets
# overall_sentiment = df['sentiment'].mean()

# print("Overall sentiment score:", overall_sentiment)


import pandas as pd
from textblob import TextBlob

# Load CSV file
df = pd.read_csv('Europe.csv')

# Convert 'Date' column to a datetime object and extract month
df['month'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m')

# Clean up tweets by removing URLs, mentions, and hashtags
df['clean_tweet'] = df['Tweet'].str.replace('http\S+|www.\S+|@\S+|#\S+', '', case=False)

# Calculate sentiment score for each tweet
df['sentiment'] = df['clean_tweet'].apply(lambda tweet: TextBlob(tweet).sentiment.polarity)

# Calculate overall sentiment score for each month
monthly_sentiment = df.groupby('month')['sentiment'].mean()

print(monthly_sentiment)






