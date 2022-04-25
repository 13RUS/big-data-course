#!/usr/bin/python

import sys
from random import randint

current_string = ""
number = 5
current_counter = randint(1, 5)
number_of_lines_for_output = 50
#f = open("hw02_mr_data_ids.txt", "a")

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    count, word = line.split('\t', 1)

    # create string
    if current_counter == 1:
        current_string = current_string + word
        current_counter = current_counter - 1
    elif current_counter > 1:
        current_string = current_string + word + ","
        current_counter = current_counter - 1

    if current_counter == 0:
        print ('%s' % current_string)
        current_counter = randint(1, 5)
        current_string = ""
