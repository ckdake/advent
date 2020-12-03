import csv

# for each line, load it in to a [][] with true for #(tree) and false for . (notree)
# based on total number of lines, duplicate to the right so we have enough columns
#  e.g. if there are 10 lines, and we are sloping right3/down1, for each 1 line we need 3 columns
# for each row, lookup the coord at row * step 
# add these things up

map = []

with open('input.txt', 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    map.append(list(row[0]))

width = len(map[0])
trees_encountered = 0
current_column = 0

for row in map:
  print row
  if current_column > width - 1:
    current_column = current_column - width
  if row[current_column] == '#':
    trees_encountered += 1
  current_column += 3
  

print "rows:", len(map)
print "cols: ", width
print "trees: ", trees_encountered

