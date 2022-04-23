#!/usr/bin/python

import sys
import random

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print(f'{random.random()}\t{word}')
