__author__ = 'Maria Antoniak'
# Edited by Antariksh
# Fixed Review Genre Split Problem (It was splitting by Space instead of Comma)
# Fixed Underscore problem
# Fixed Unique ID problem

import sys, pickle
import re, nltk


def main():
    input_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')
    reviews = pickle.load(input_file)
    for i, review in enumerate(reviews):
        unique_id = review.productID + '_' + review.userID + '_' + str(i)
        main_genre = review.genre.split(',')[0].replace(' ','-')
        text_without_punct = re.sub(r'([^\w\s]|_)', '', review.text.lower())
        tokens = nltk.word_tokenize(text_without_punct)
        output_file.write(unique_id + ' ' + main_genre + ' ')
        for token in tokens:
            output_file.write(token + ' ')
        output_file.write('\n')


if __name__ == '__main__':
    main()