from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

text = """The cat is in the box. The cat likes the box. The box is
over the cat in the house."""

tokens = [w for w in word_tokenize(text.lower()) if w.isalpha()]
print("Tokens:",tokens,"\n")
no_stops = [t for t in tokens if t not in stopwords.words('english')] #"and", "are", "is"
print("No_stops:",no_stops,"\n")
print("Counter:",Counter(no_stops).most_common(2))