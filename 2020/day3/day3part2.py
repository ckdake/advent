#!/usr/bin/env python
""" 2020 code advent, day 3, part 2 """

import csv

# for each line, load it in to a [][] with true for #(tree) and false for . (notree)
# based on total number of lines, duplicate to the right so we have enough columns
# e.g. if there are 10 lines, and we are sloping right3/down1, for each 1 line we
# need 3 columns
# for each row, lookup the coord at row * step
# add these things up


# part 2: 1,1 * 3,1 * 5,1 * 7,1 * 1,2


the_map = []
with open("input.txt", "r") as fd:
    reader = csv.reader(fd)
    for row in reader:
        the_map.append(list(row[0]))


def treefinder(local_map, right_increment, down_increment):
    """ Finds the tree! """
    width = len(local_map[0])
    trees_encountered = 0
    current_column = 0
    current_row = 0

    while current_row < len(local_map):
        if current_column > width - 1:
            current_column = current_column - width
        if local_map[current_row][current_column] == "#":
            trees_encountered += 1
        current_column += right_increment
        current_row += down_increment

    return trees_encountered


print(treefinder(the_map, 1, 1))
print(treefinder(the_map, 3, 1))
print(treefinder(the_map, 5, 1))
print(treefinder(the_map, 7, 1))
print(treefinder(the_map, 1, 2))

print(
    "product: ",
    treefinder(the_map, 1, 1)
    * treefinder(the_map, 3, 1)
    * treefinder(the_map, 5, 1)
    * treefinder(the_map, 7, 1)
    * treefinder(the_map, 1, 2),
)
