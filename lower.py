#!/usr/bin/env python

"""
A filter that changes upper case characters to lowercase.
"""

import fileinput
import re


def process(line):
    print(line[:-1].lower())

for line in fileinput.input():
    process(line)
