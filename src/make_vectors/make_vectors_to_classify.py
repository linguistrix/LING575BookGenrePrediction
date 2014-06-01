__author__ = 'Maria Antoniak'


import sys, pickle
import re, nltk
from collections import defaultdict


def get_word_count_dict(tokens):
    word_count_dict = defaultdict(int)
    for token in tokens:
        word_count_dict[token] += 1
    return word_count_dict


def main():
    input_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')
    reviews = pickle.load(input_file)
    j = 0
    for review in reviews:
        unique_id = review.productID + review.userID + str(j)
        j += 1
        main_genre = review.genre.split()[0].replace(',', '')
        text_without_punct = re.sub(r'[^\w\s_]', '', review.text.lower())
        tokens = nltk.word_tokenize(text_without_punct)
        word_count_dict = get_word_count_dict(tokens)
        output_file.write(main_genre + ' ')  # unique_id not needed for classifier, only lda
        for word in word_count_dict:
            output_file.write(word + ':' + str(word_count_dict[word]) + ' ')
        output_file.write('\n')


if __name__ == '__main__':
    main()
