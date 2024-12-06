import re
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Load data
df = pd.read_excel(r".\\ch5\\TeamHealthRawDataForDemo.xlsx")
df["row_id"] = df.index + 1
print(df.head(10))

# Pre-process text
df_subset = df[['row_id', 'Response']].copy()
df_subset['Response'] = df_subset['Response'].str.replace("[^a-zA-Z#]", " ")
df_subset['Response'] = df_subset['Response'].str.casefold()
print(df_subset.head(10))

# Sentiment analysis
sid = SentimentIntensityAnalyzer()

# Initialize the output dataframe
t_df = pd.DataFrame(columns=['row_id', 'sentiment_type', 'sentiment_score'])

for index, row in df_subset.iterrows():
    scores = sid.polarity_scores(row['Response'])
    for key, value in scores.items():
        temp = pd.DataFrame([[row['row_id'], key, value]], columns=['row_id', 'sentiment_type', 'sentiment_score'])
        t_df = pd.concat([t_df, temp], ignore_index=True)

# Clean the output dataframe
t_df_cleaned = t_df[t_df.row_id != '99999999999']
t_df_cleaned = t_df_cleaned.drop_duplicates()
t_df_cleaned = t_df_cleaned[t_df_cleaned.sentiment_type == 'compound']
print(t_df_cleaned.head(10))

# Merge sentiment scores with the original dataframe
df_output = pd.merge(df, t_df_cleaned, on='row_id', how='inner')
print(df_output.head(10))
