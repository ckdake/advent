#!/usr/bin/env python
""" 2021 code advent, day1 """

import csv

hpos = 0
vpos = 0

with open("input.txt", "r") as fd:
    reader = csv.reader(fd)
    for row in reader:
        row = row[0].split(' ')
        print(row)
        if (row[0] == "forward"): # one of forward, down
            hpos = hpos + int(row[1])
        elif (row[0] == "down"):
            vpos = vpos - int(row[1])
        elif (row[0] == "up"):
            vpos = vpos + int(row[1])

print(hpos * vpos)
