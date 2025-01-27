import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import spacy

nltk.download('punkt')

nlp = spacy.load("en_core_web_sm")

sentence = "The quick brown foxes are running happily and they jumped over the lazy dogs. Only the best examples are accepted"

nltk_tokens = word_tokenize(sentence)

stemmer = PorterStemmer()

nltk_stems = [stemmer.stem(word) for word in nltk_tokens]

spacy_doc = nlp(sentence)
spacy_lemmas = [token.lemma_ for token in spacy_doc]

comparison = list(zip(nltk_tokens, nltk_stems, spacy_lemmas))

print(f"{'Word':<15}{'NLTK Stem':<15}{'spaCy Lemma':<15}")
print("-" * 45)
for word, nltk_stem, spacy_lemma in comparison:
    print(f"{word:<15}{nltk_stem:<15}{spacy_lemma:<15}")

