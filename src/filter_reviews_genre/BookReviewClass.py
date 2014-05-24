# LING 575 Sentiment Project
# BookReviewClass.py Defines a class that represents a single BookReview
# Also provides functions for reading reviews from the file and pickling them
__author__ = 'Antariksh Bothale'

import sys, os, codecs
import cPickle as pickle

class BookReview:

    def __init__(self, listOfLines=None):
        if listOfLines is None:
            self.productID = ''
            self.title = ''
            self.price = ''
            self.userID = ''
            self.profileName = ''
            self.helpfulness = ''
            self.score = ''
            self.time = ''
            self.summary = ''
            self.text = ''
        elif len(listOfLines) != 10:
            sys.stderr.write('List of review lines must have size exactly equal to 10\n')
        else:
            self.productID = listOfLines[0][19:].strip()
            self.title = listOfLines[1][15:].strip()
            self.price = listOfLines[2][15:].strip()
            self.userID = listOfLines[3][15:].strip()
            self.profileName = listOfLines[4][19:].strip()
            self.helpfulness = listOfLines[5][19:].strip()
            self.score = listOfLines[6][14:].strip()
            self.time = listOfLines[7][13:].strip()
            self.summary = listOfLines[8][16:].strip()
            self.text = listOfLines[9][13:].strip()

    def readFile(self, file):
        with codecs.open(file, encoding='utf-8') as f:
            allReviews = []
            allLines = f.readlines()
            i = 0
            while i < len(allLines):
                reviewLines = allLines[i:i+10]
                tmp = BookReview(reviewLines)
                allReviews.append(tmp)
                i += 11

        return allReviews

    def __repr__(self):
        return '\n'.join([self.productID,
                         self.title,
                         self.price,
                         self.userID,
                         self.profileName,
                         self.helpfulness,
                         self.score,
                         self.time,
                         self.summary,
                         self.text])

    def __str__(self):
        return self.__repr__()


