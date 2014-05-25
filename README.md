Maria Antoniak & Antariksh Bothale
LING 575 Sentiment, Subjectivity, and Stance with Prof. Gina Levow
Spring 2014

Goal: Genre classification through use of aspect information gleaned from Amazon book reviews.

Steps:
-- Get Amazon book reviews.
-- Filter reviews (keep only those that have high helpfulness ratings).
-- Filter reviews (keep only those that have ISBNs).
-- Scrape ranked lists of genres from GoodReads for each ISBN.
-- Filter reviews (keep only those for which we found genres).


LDA Mallet Commands
-------------------

mallet import-file --input lda_vectors.txt --output lda_vectors.mallet --keep-sequence --remove-stopwords

mallet train-topics --input lda_vectors.mallet --num-topics 10