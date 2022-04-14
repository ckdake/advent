#!/usr/bin/env python
""" 2021 code advent, day3 """

import csv


gamma = ''
epsilon = ''

most_common_tracker = ''
least_common_tracker = ''

with open("input.txt", "r") as fd:
    reader = csv.reader(fd)
    for row in reader:
        vals = list(row)
        print(vals)
        # row = row[0].split(' ')
        # vpos = vpos + int(row[1])

