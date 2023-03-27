import os
import re
import util

file = open(os.path.join(os.path.dirname(__file__), "data.txt"), "r")
text = file.readline()
#text = input("Enter text: ")

print(util.number_of_sentences(text))
print(util.average_length_of_sentences(text))
print(util.average_length_of_words(text))
print(util.number_of_non_declaration_sentances(text))
print(util.top_k_repeated_ngrams(text, 1, 2))