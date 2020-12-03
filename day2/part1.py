import csv

# for each line, understand the password policy

# how many are passing?

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

# line 1 means that the password must contain 1,2, or 3 occurances of 'a'

valid_count = 0

with open('input.txt', 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    parts =  row[0].split(' ')

    (min_count,max_count) = map(int, parts[0].split('-'))
    seek_char = parts[1].split(':')[0]
    candidate_string = parts[2]

    the_count = 0

    for char in list(candidate_string):
      if char == seek_char: 
        the_count += 1    

    if the_count >= min_count and the_count <= max_count:
        valid_count += 1

print(valid_count)

