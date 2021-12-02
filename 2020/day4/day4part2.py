#!/usr/bin/env python
""" 2020 code advent, day 4 part 2 """

import csv
import re

# grab each passport from the data file
# sum up the valid ones
# byr, iyr, eyr, hgt, hcl, ecl, pid are all required. cid is optional


def byr_validate(string):
    """ validate birth year """
    if not 1920 <= int(string) <= 2002:
        # print("invalid:", string)
        return False
    return True


def iyr_validate(string):
    """ validate issue year """
    if not 2010 <= int(string) <= 2020:
        # print("invalid:", string)
        return False
    return True


def eyr_validate(string):
    """ validate expire year """
    if not 2020 <= int(string) <= 2030:
        # print("invalid:", string)
        return False
    return True


def hgt_validate(string):
    """ validate height """
    if string.endswith("cm") and (150 <= int(string.replace("cm", "")) <= 193):
        return True
    elif string.endswith("in") and (50 <= int(string.replace("in", "")) <= 76):
        return True
    else:
        # print("invalid:", string)
        return False


def hcl_validate(string):
    """ validate hair color """
    if not re.match("^#[0-9abcdef]{6,6}$", string):
        # print("invalid:", string)
        return False
    return True


def ecl_validate(string):
    """ validate eye color """
    if not ("amb", "blu", "brn", "gry", "grn", "hzl", "oth").count(string):
        # print("invalid:", string)
        return False
    return True


def pid_validate(string):
    """ validate password id """
    return re.match(r"^[\d]{9,9}$", string)


def checkvalid(passport):
    """ returns true if passport is valid """
    if not (
        passport
        and passport.get("byr")
        and passport.get("iyr")
        and passport.get("eyr")
        and passport.get("hgt")
        and passport.get("hcl")
        and passport.get("ecl")
        and passport.get("pid")
    ):
        return False

    return (
        byr_validate(passport.get("byr"))
        and iyr_validate(passport.get("iyr"))
        and eyr_validate(passport.get("eyr"))
        and hgt_validate(passport.get("hgt"))
        and hcl_validate(passport.get("hcl"))
        and ecl_validate(passport.get("ecl"))
        and pid_validate(passport.get("pid"))
    )


def makepassport(passportstring):
    """ truns a string into a passport dict """
    passport = {}
    for kvp in passportstring.split(" "):
        if kvp:
            (key, value) = kvp.split(":")
            passport[key] = value
    return passport


def doit():
    """ Does the work """
    passports = []

    with open("input.txt", "r") as file_descriptor:
        reader = csv.reader(file_descriptor)
        accumulator = ""
        for row in reader:
            if not row:
                passports.append(makepassport(accumulator))
                accumulator = ""
            else:
                accumulator = accumulator + " " + row[0]
        if accumulator:
            passports.append(makepassport(accumulator))

    valid_count = 0
    invalid_count = 0
    for passport in passports:
        # print(passport)
        if checkvalid(passport):
            valid_count += 1
        else:
            invalid_count += 1

    print("valid: ", valid_count)
    print("invalid: ", invalid_count)


# 10 is not right
doit()
