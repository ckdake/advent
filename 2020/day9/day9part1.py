#!/usr/bin/env python
""" 2020 code advent, day 9 part 1 """

# first 25 numbers are 'preamble'
# after that, every number should be the some of any two of the 25 immediately previous numbers


def valid_number(number, potential_parts):
    print(len(potential_parts))
    print("looking for parts of:", number, " in:", potential_parts)
    for i, e in enumerate(potential_parts):
        for j, f in enumerate(potential_parts[i + 1 : len(potential_parts)]):
            print("checking:", e, ",", f)
            if e + f == number:
                return True
    return False


numbers = []
preamble_length = 25
current_position = (
    preamble_length  # the first 25 are the preamble, this is the 26th number
)

inputfile = open("input.txt", "r")
for line in inputfile:
    numbers.append(int(line))


while current_position < len(numbers):
    if not valid_number(
        numbers[current_position],
        numbers[current_position - preamble_length : current_position],
    ):
        print("First invalid number: ", numbers[current_position])
        break
    current_position += 1


# not 140900, too low.
