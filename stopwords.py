#!/usr/bin/env python

"""
A filter that extracts words from sentences.
"""

import fileinput
import re

fh = open("stopwords.txt", "r")
contents = fh.read()
fh.close()
stopwords = contents.replace('\n',',').split(',')


def process(line):
    words = line.split()
    words = [x for x in words if x not in stopwords]
    for p in words: print (p)

for line in fileinput.input():
    process(line)
