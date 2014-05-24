__author__ = 'Maria Antoniak'

import sys, pickle, nltk

OUTPUT_FILE_NAME = '/workspace/ling575_2014/abothale-riamarie/data/mallet/lda_vectors.txt'
INPUT_FILE_NAME = '/workspace/ling575_2014/abothale-riamarie/data/reviews.pickle'


def main():
    input_file = open(INPUT_FILE_NAME, 'r')
    output_file = open(OUTPUT_FILE_NAME, 'w')
    reviews = pickle.load(input_file)
    i = 0
    for review in reviews:
        if i < 1000:
            unique_id = review.productID + review.userID
            tokens = nltk.word_tokenize(review.text.lower().re.sub(r'[^\w\s]', '', review.text.lower()))
            output_file.write(unique_id + ' label ')
            for token in tokens:
                output_file.write(token + ' ')
            output_file.write('\n')
        i += 1


if __name__ == '__main__':
    main()