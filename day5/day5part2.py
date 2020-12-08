#!/usr/bin/env python
""" 2020 code advent, day 5 part 1 """

import csv


def decode_seat(seatstring):
    """ returns the seat id """

    row_start = 0
    row_end = 127
    for char in list(seatstring[0:7]):
        if char == "F":  # take the first half.  e.g. 0,127 should become 0,63
            row_end = row_end - (((row_end - row_start) + 1) / 2)
        else:  # take the second half, e.g. 0,127 should become 64,127
            row_start = row_start + (((row_end - row_start) + 1) / 2)

    if row_start != row_end:
        print("WTF!")

    col_start = 0
    col_end = 7
    for char in list(seatstring[7:10]):
        if char == "L":  # take the first half.  e.g. 0,7 should become 0,3
            col_end = col_end - (((col_end - col_start) + 1) / 2)
        else:  # take the second half, e.g. 0,7 should become 4,7
            col_start = col_start + (((col_end - col_start) + 1) / 2)

    if col_start != col_end:
        print("WTF!")

    seat_id = row_start * 8 + col_start
    return int(seat_id)


def doit():
    """ Does the work """

    seat_ids = []

    with open("input.txt", "r") as file_descriptor:
        reader = csv.reader(file_descriptor)
        for row in reader:
            seat_ids.append(decode_seat(row[0]))

    seat_ids.sort()

    last_id = seat_ids[0]
    for aid in seat_ids:
        if aid > last_id + 1:
            return last_id + 1
        else:
            last_id = aid


# not 706
print("my seat: ", doit())
