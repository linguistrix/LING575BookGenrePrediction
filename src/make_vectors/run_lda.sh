#!/bin/sh
mallet train-topics --input train.vectors.mallet --num-topics 10 --optimize-interval 10 --output-topic-keys topics.10.txt --output-doc-topics topics.10.composition.txt