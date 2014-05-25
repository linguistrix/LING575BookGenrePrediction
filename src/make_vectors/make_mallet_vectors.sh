#!/bin/sh
mallet import-file --input train.vectors.txt --output train.vectors.mallet --keep-sequence --remove-stopwords
mallet import-file --input test.vectors.txt --output test.vectors.mallet --keep-sequence --remove-stopwords