from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, ne_chunk_sents

# Step 1: Read the article from the file
with open("C:/Users/supawit-project/Documents/NLP/ch4/tim_cook.txt", "r") as file:
    article = file.read()

# Step 2: Tokenize the article into sentences
sentences = sent_tokenize(article)

# Step 3: Tokenize each sentence into words
token_sentences = [word_tokenize(sent) for sent in sentences]

# Step 4: Tag each tokenized sentence into parts of speech
pos_sentences = [pos_tag(sent) for sent in token_sentences]

# Step 5: Create the named entity chunks
chunked_sentences = ne_chunk_sents(pos_sentences, binary=True)

# Step 6: Loop over each sentence and chunk to test for named entities
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)
