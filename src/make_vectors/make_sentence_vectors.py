__author__ = 'Maria Antoniak'

import sys, pickle
import re, nltk


def main():
    input_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')
    reviews = pickle.load(input_file)
    j = 0
    for review in reviews:
        unique_id = review.productID + review.userID + j
        j += 1
        main_genre = review.genre.split()[0].replace(',', '')
        tokens = nltk.word_tokenize(review.text.lower())
        sentence_vectors = []
        i = 0
        for token in tokens:
            if not sentence_vectors:
                sentence_vectors.append(unique_id + str(i) + ' ' + main_genre + ' ')
                i += 1

            elif '.' in token or '?' in token or '!' in token:
                sentence_vectors[-1] += token.strip('.').strip('?').strip('!') + ' '
                sentence_vectors.append(unique_id + str(i) + ' ' + main_genre + ' ')
                i += 1
            else:
                token = re.sub(r'[^\w\s_]', '', token)
                if token:
                    sentence_vectors[-1] += token + ' '

        for vector in sentence_vectors:
            output_file.write(vector + '\n')


if __name__ == '__main__':
    main()