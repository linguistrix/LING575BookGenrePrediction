__author__ = 'Antariksh Bothale'
import sys, os
from BookReviewClass import BookReview
import cPickle as pickle

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print "Usage: PickleBookReviews.py input_dir output_dir"
        sys.exit(0)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]


    for item in os.listdir(input_dir):
        fullname = os.path.join(input_dir, item)
        if os.path.isfile(fullname) and fullname[-4:] == '.txt':
            output_name = os.path.join(output_dir, item[:-4] + '.pickle')
            allReviews = BookReview().readFile(file)
            picklefile = open(output_name, 'w')
            pickle.dump(allReviews, picklefile)
            picklefile.close()
            print ('Written file {0}'.format(output_name))
            sys.stdout.flush()




