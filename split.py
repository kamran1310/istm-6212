#!/usr/bin/env python

"""
A filter that extracts words from sentences.
"""

import fileinput
import re


def process(line):
    #words = re.findall('\w{2,}',line)
    words = re.sub("[^\w]", " " , line).split()
    words = [x for x in words if len(x)>1]
    for p in words: print (p)
    

for line in fileinput.input():
    process(line)
