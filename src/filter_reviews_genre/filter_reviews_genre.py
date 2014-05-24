__author__ = 'Maria Antoniak'


import sys, os
from BookReviewClass import BookReview
import cPickle as pickle

GENRES_FILE_PATH = '/workspace/ling575_2014/abothale-riamarie/data/genres/genres.txt'
PICKLED_DIRECTORY_PATH = '/workspace/ling575_2014/abothale-riamarie/data/filtered_isbn/pickled/'
FILTERED_DIRECTORY_PATH = '/workspace/ling575_2014/abothale-riamarie/data/filtered_genres/'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_filtered_isbn_list():
    """
        Read in a dictionary of ISBN numbers from the genre file.
    """
    isbn_dict = {}
    infile_name = GENRES_FILE_PATH
    infile = open(infile_name, 'r')
    for line in infile:
        if len(line.strip().split()) == 1 and is_number(line.strip()) and len(line.strip()) == 10:
            isbn_dict[line.strip()] = 1
    return isbn_dict


def debug(isbn_dict):
    """
         Debug - check that the new file has the correct objects.
    """
    listing = os.listdir(FILTERED_DIRECTORY_PATH)
    for pickle_file_name in listing:
        filtered_pickle_file = open(FILTERED_DIRECTORY_PATH + pickle_file_name, 'r')
        reviews = pickle.load(filtered_pickle_file)
        for review in reviews:
            if not review.productID in isbn_dict:
                sys.stderr.write('ERROR - the wrong ISBN has been written to the filtered file!\n')


def main():

    # Read in a dictionary of ISBN numbers from the genre file.
    isbn_dict = get_filtered_isbn_list()

    # Open the pickled files and filter the reviews by the ISBNs stored in isbn_dict.
    filtered_reviews_list = []
    listing = os.listdir(PICKLED_DIRECTORY_PATH)
    for pickle_file_name in listing:
        pickle_file = open(PICKLED_DIRECTORY_PATH + pickle_file_name, 'r')
        reviews = pickle.load(pickle_file)
        for review in reviews:
            if review.productID in isbn_dict:
                filtered_reviews_list.append(review)

    # Save the filtered reviews into a single pickled file.
    filtered_pickle_file = open(FILTERED_DIRECTORY_PATH + 'reviews.pickle', 'w')
    pickle.dump(filtered_reviews_list, filtered_pickle_file)
    filtered_pickle_file.close()


if __name__ == '__main__':
    main()