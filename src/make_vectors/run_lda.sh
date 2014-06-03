#!/bin/sh
mallet train-topics --input train.vectors.mallet --num-topics 20 --optimize-interval 20 --output-topic-keys topics.10.txt --output-doc-topics topics.20.composition.txt