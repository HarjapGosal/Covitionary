# CLC 12 - Capstone Project (Harjap Gosal)
# Covitionary: Development of a Covid Vocabulary using Text-Mining

# import covitionary.covitionary_helpers as h

# Output file declarations
fw = open('./data/Output-Vocab-COVID-Bigrams(7 Freq)-April2021.tsv', 'w')  # Main output file

# Reading the input corpus file
with open('./data/covid-literature-input.csv', 'r', encoding="utf-8") as f:
    input_data = f.read()


# gets different n-grams and tokens with frequency

# gets bigrams with required frequency
frequent_bigram_list = h.get_frequent_bigrams(input_data,2,7)

# gets trigrams with required frequency
#frequent_trigram_list = h.get_frequent_bigrams(input_data,3,7)

# gets quadgrams (4-grams) with required frequency
#frequent_quadgram_list = h.get_frequent_bigrams(input_data,4,7)

# gets tokens with frequency of occurence
frequency_dict_selected = h.get_frequent_token(input_data,2)

# prints tokens with frequency of occurence
# for key, value in frequency_dict_selected.items():
#     fw.write(key+"\t" + str(value) + "\n")

# prints bigrams/ trigrams or quadgrams
for value in frequent_bigram_list:
    fw.write(value+"\n")

fw.close()