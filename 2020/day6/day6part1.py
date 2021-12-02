#!/usr/bin/env python
""" 2020 code advent, day 6 part 1 """

import csv


def count_for_row(group_string):
    return len(sorted(set(group_string))) - 1


def doit():
    """ Does the work """

    counts = []

    with open("input.txt", "r") as file_descriptor:
        reader = csv.reader(file_descriptor)
        accumulator = ""
        for row in reader:
            if not row:
                counts.append(count_for_row(accumulator))
                accumulator = ""
            else:
                accumulator = accumulator + " " + row[0]
        if accumulator:
            counts.append(count_for_row(accumulator))
    print(counts)
    print("total: ", sum(counts))


# 7225 is too high.
doit()
