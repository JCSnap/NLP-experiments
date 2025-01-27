import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download necessary NLTK data (if not already downloaded)
nltk.download('punkt')

# Example sentence
sentence = "only the best examples are accepted"

# Tokenize the sentence into words
tokens = word_tokenize(sentence)

# Initialize the stemmer
stemmer = PorterStemmer()

# Apply stemming to each word
stemmed_words = [stemmer.stem(word) for word in tokens]

# Print results
print("Original Tokens:", tokens)
print("Stemmed Words:", stemmed_words)

