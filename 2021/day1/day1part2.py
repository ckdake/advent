#!/usr/bin/env python
""" 2021 code advent, day1 """

import csv

# how many times does the number increase?

numbers = []

with open("input.txt", "r") as fd:
    reader = csv.reader(fd)
    for row in reader:
        numbers.append(int(row[0]))

windows = []

for i in range(len(numbers) - 2):
    windows.append(numbers[i] + numbers[i+1] + numbers[i+2])

count = 0

for i in range(len(windows) - 1):
    if windows[i] < windows[i+1]:
        count = count + 1 

print(count)
