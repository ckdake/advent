#!/usr/bin/env python
""" 2021 code advent, day1 """

import csv

# how many times does the number increase?

numbers = []

with open("input.txt", "r") as fd:
    reader = csv.reader(fd)
    for row in reader:
        numbers.append(int(row[0]))

count = 0

for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i+1]:
        count = count + 1 

print(count)
