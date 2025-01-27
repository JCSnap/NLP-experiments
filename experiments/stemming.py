import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')

sentence = "only the best examples are accepted"

tokens = word_tokenize(sentence)

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in tokens]

print("Original Tokens:", tokens)
print("Stemmed Words:", stemmed_words)

