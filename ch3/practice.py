# Import necessary libraries
from nltk.stem import WordNetLemmatizer
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load the file
with open("C:/Users/supawit-project/Documents/NLP/ch3/wiki_article_6.txt", "r") as f:
    article = f.read()

# Tokenize the article into words
lower_tokens = word_tokenize(article.lower())  # Convert text to lowercase and tokenize

# Define stop words
english_stops = set(stopwords.words('english'))

# Retain alphabetic words: alpha_only
alpha_only = [t for t in lower_tokens if t.isalpha()]

# Remove all stop words: no_stops
no_stops = [t for t in alpha_only if t not in english_stops]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))
