#!/bin/sh
mallet import-file --input sentences.train.vectors.txt --output sentences.train.vectors.mallet --keep-sequence --remove-stopwords
mallet import-file --input sentences.test.vectors.txt --output sentences.test.vectors.mallet --keep-sequence --remove-stopwords