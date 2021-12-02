#!/usr/bin/env python
""" 2020 code advent, day 9 part 1 """

# first 25 numbers are 'preamble'
# after that, every number should be the some of any two of the 25 immediately previous numbers
# now we need to find contiguous set that sum to the invalid_number


def valid_number(number, potential_parts):
    for i, e in enumerate(potential_parts):
        for j, f in enumerate(potential_parts[i + 1 : len(potential_parts)]):
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


invalid_number = -1
while current_position < len(numbers):
    if not valid_number(
        numbers[current_position],
        numbers[current_position - preamble_length : current_position],
    ):
        invalid_number = numbers[current_position]
        print("First invalid number: ", numbers[current_position])
        break
    current_position += 1


range_start = 0
range_end = 0
current_sum = 0
# invalid_number is our target sum

while range_end < len(numbers) - 1:  # this should probably be while True
    print(
        "Currently [",
        range_start,
        ":",
        range_end,
        "](",
        numbers[range_start:range_end],
        ") --> ",
        current_sum,
        " compared to: ",
        invalid_number,
    )
    if current_sum == invalid_number:  # We've done it
        print("WE DID IT:", numbers[range_start:range_end])
        print("min:", min(numbers[range_start:range_end]))
        print("max:", max(numbers[range_start:range_end]))
        print(
            "solution:",
            min(numbers[range_start:range_end]) + max(numbers[range_start:range_end]),
        )
        break
    elif (
        current_sum > invalid_number and range_start < range_end
    ):  # too big, shrink the range (and there is room to)
        print("too big, shrinking range from left")
        current_sum -= numbers[range_start]
        range_start += 1
    else:  # too small, grow the range
        print("too small, growing range to right")
        current_sum += numbers[range_end]
        range_end += 1


print("If the previous line doesn't say that we did it. we didn't do it. :(")


# print the contiguous set that sums up to this number
# add together the smalest and largest number in this range, submit as answer
