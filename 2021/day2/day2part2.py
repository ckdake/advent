#!/usr/bin/env python
""" 2021 code advent, day1 """

import csv

hpos = 0
vpos = 0
aim = 0

with open("input.txt", "r") as fd:
    reader = csv.reader(fd)
    for row in reader:
        row = row[0].split(' ')
        print(row)
        if (row[0] == "forward"): 
            hpos = hpos + int(row[1])
            vpos = vpos + (int(row[1]) * aim)
        elif (row[0] == "down"):
            aim = aim + int(row[1])
        elif (row[0] == "up"):
            aim = aim - int(row[1])

print(aim)
print(hpos)
print(vpos)
print(hpos*vpos)
