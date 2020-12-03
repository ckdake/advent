#!/usr/bin/env python
""" 2020 code advent, day 2, part 2 """

import csv

# for each line, understand the password policy

# how many are passing?

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

def whatsthecount():
    """ Does the work """
    valid_count = 0
    with open('input.txt', 'r') as file_descriptor:
        reader = csv.reader(file_descriptor)
        for row in reader:
            parts =  row[0].split(' ')

            (first_index,second_index) = map(int, parts[0].split('-'))
            seek_char = parts[1].split(':')[0]
            candidate_string = parts[2]

            the_count = 0

            candidate_array = list(candidate_string)

            if candidate_array[first_index - 1] == seek_char:
                the_count += 1
            if candidate_array[second_index - 1] == seek_char:
                the_count += 1

            if the_count == 1:
                valid_count += 1
    return valid_count

print(whatsthecount())
