#!/usr/bin/env python
""" 2020 code advent, day 6 part 2 """

import csv


def count_for_group(group_arr):
    chars = set(group_arr[0]) # start with the first set of yes answers
    for row in group_arr: # for each additional person, remove any from the set that they did not answer
        for char in chars.copy():
            if char not in set(row):
                chars.remove(char)
    return len(chars)

def doit():
    """ Does the work """

    group_counts = []

    with open('input.txt', 'r') as file_descriptor:
        reader = csv.reader(file_descriptor)
        agroup = []
        for row in reader:
            if not row:
                group_counts.append(count_for_group(agroup))
                agroup = []
            else:
                agroup.append(row[0])
        if agroup:
            group_counts.append(count_for_group(agroup))

    print(group_counts)
    print("total: ", sum(group_counts))

# 
doit()
