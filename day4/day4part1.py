#!/usr/bin/env python
""" 2020 code advent, day 4 part 1 """

import csv

# grab each passport from the data file
# sum up the valid ones
# byr, iyr, eyr, hgt, hcl, ecl, pid are all required. cid is optional

def checkvalid(passport):
    """ returns true if passport is valid """
    return (passport and
        passport.get('byr') and
        passport.get('iyr') and
        passport.get('eyr') and
        passport.get('hgt') and
        passport.get('hcl') and
        passport.get('ecl') and
        passport.get('pid'))

def makepassport(passportstring):
    """ truns a string into a passport dict """
    passport = {}
    for kvp in passportstring.split(' '):
        if kvp:
            (key,value) = kvp.split(':')
            passport[key] = value
    return passport

def doit():
    """ Does the work """
    passports = []

    with open('input.txt', 'r') as file_descriptor:
        reader = csv.reader(file_descriptor)
        accumulator = ''
        for row in reader:
            if not row:
                passports.append(makepassport(accumulator))
                accumulator = ''
            else:
                accumulator = accumulator + ' ' + row[0]
        if accumulator:
            passports.append(makepassport(accumulator))

    valid_count = 0
    invalid_count = 0
    for passport in passports:
        print(passport)
        if checkvalid(passport):
            valid_count += 1
        else:
            invalid_count += 1

    print('valid: ', valid_count)
    print('invalid: ', invalid_count)

# 232 is not right
doit()
