from collections import Counter, defaultdict
import re

class BpeTokenizer:
    def __init__(self):
        self.corpus = []
        self.vocab = set()

    def train(self, corpus):
        words = corpus.split(" ")
        words = [word + "_" for word in words]
        for word in words:
            self.corpus.append([c for c in word])
            for c in word:
                self.vocab.add(c)
        while True:
            most_freq_pair = self.__find_most_freq_pair()
            if most_freq_pair is None:
                break
            self.vocab.add("".join(most_freq_pair))
            self.__replace_most_freq_pair(most_freq_pair)
        print(self.corpus)
        print(self.vocab)

    def tokenize(self, word):
        word = word + "_"
        tokens = []
        pointer = 0
        while pointer < len(word):
            for i in range(len(word), pointer, -1):
                subword = word[pointer:i]
                if subword in self.vocab:
                    tokens.append(subword)
                    pointer = i
                    break
        print(f"Tokenized word: {word} -> {tokens}")
        return tokens

    def __find_most_freq_pair(self):
        pairs = defaultdict(int)
        for word in self.corpus:
            for i in range(len(word) - 1):
                pairs[word[i], word[i+1]] += 1

        if not pairs:
            return None

        return max(pairs, key=pairs.get)

    def __replace_most_freq_pair(self, most_freq_pair):
        most_freq_pair_str = "".join(most_freq_pair)
        print("Merge pair: ", most_freq_pair[0], most_freq_pair[1], " -> ", most_freq_pair_str)
        for word in self.corpus:
            index_to_remove = []
            for i in range(len(word) - 1):
                if (word[i], word[i + 1]) == most_freq_pair:
                    word[i] = most_freq_pair_str
                    index_to_remove.append(i + 1)
            for index in index_to_remove[::-1]:
                del word[index]


if __name__ == "__main__":
    tokenizer = BpeTokenizer()
    tokenizer.train("target pasta star star pasta")
    tokenizer.tokenize("tapas")
    tokenizer.tokenize("stata")
