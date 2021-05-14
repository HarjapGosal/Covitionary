from itertools import combinations
from nltk import word_tokenize, pos_tag, ne_chunk
import os
import csv
import nltk.chunk
from nltk import word_tokenize, pos_tag, ne_chunk
from itertools import combinations
from Bio import Entrez
import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.collocations import *
import unicodedata
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()


# To remove Special Characters
def remove_special_characters(text):
    text = re.sub('[^a-zA-Z0-9\s]', '', text)
    return text


def convert_tuple_to_str(input_tuple_list):
    output_list = []
    for value in input_tuple_list:
        value_str = str(value)
        value_str = value_str.replace("(", "")
        value_str = value_str.replace(")", "")
        value_str = value_str.replace("'", "")
        value_str = value_str.replace(",", "")
        output_list.append(value_str)
    return output_list

def get_frequent_token(input_corpus, min_frequency):
    input_corpus = remove_special_characters(input_corpus)
    tokens = nltk.word_tokenize(str(input_corpus))
    from nltk.corpus import stopwords
    stopset = set(stopwords.words('english'))
    print(str(stopset))
    # frequency_dict = collections.OrderedDict()
    frequency_dict = {}
    frequency_dict_selected = {}
    frequent_token_list = []
    for tkn in tokens:
        if tkn.lower() in frequency_dict.keys():
            tkn_freq = int(frequency_dict[tkn.lower()])
            tkn_freq += 1
            frequency_dict[tkn.lower()] = tkn_freq
        else:
            frequency_dict[tkn.lower()] = 1
    for key, value in frequency_dict.items():
        if int(value) >= min_frequency and str(key) not in stopset:
            frequent_token_list.append(key)
            frequency_dict_selected[key] = value

    return frequency_dict_selected


def get_frequent_bigrams(input_corpus, ngram_size, min_bigram_frequency):
    nltk_tokens = ""
    nltk_tokens = (word_tokenize(input_corpus))

    words = [w.lower() for w in nltk_tokens]
    print("Number of Words: ", len(nltk_tokens))

    from nltk.corpus import stopwords
    stopset = set(stopwords.words('english'))
    filter_stops = lambda w: len(w) < 3 or w in stopset
    if ngram_size == 2:
        finder = BigramCollocationFinder.from_words(words)
    if ngram_size == 3:
        finder = TrigramCollocationFinder.from_words(words)
    if ngram_size == 4:
        finder = QuadgramCollocationFinder.from_words(words)

    finder.apply_word_filter(filter_stops)
    finder.apply_freq_filter(min_bigram_frequency)
    frequent_ngram_list = finder.nbest(bigram_measures.raw_freq, 25000)
    frequent_gram_list_str = convert_tuple_to_str(frequent_ngram_list)
    return frequent_gram_list_str


ROOT = os.path.dirname(__file__)



# To remove the accented characters, if any
def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode\
        ('ascii', 'ignore').decode('utf-8', 'ignore')

    return text

