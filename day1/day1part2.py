#!/usr/bin/env python
""" 2020 code advent, day1, part 2 """

import csv

# which 2 numbers in input.txt sum to 2020

# what is their product?

numbers = []

with open('input.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        numbers.append(int(row[0]))

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
                break
