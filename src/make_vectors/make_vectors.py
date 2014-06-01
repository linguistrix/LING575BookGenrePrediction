__author__ = 'Maria Antoniak'

import sys, pickle
import re, nltk


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
        output_file.write(unique_id + ' ' + main_genre + ' ')
        for token in tokens:
            output_file.write(token + ' ')
        output_file.write('\n')


if __name__ == '__main__':
    main()