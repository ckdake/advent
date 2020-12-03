import csv

# for each line, load it in to a [][] with true for #(tree) and false for . (notree)
# based on total number of lines, duplicate to the right so we have enough columns
#  e.g. if there are 10 lines, and we are sloping right3/down1, for each 1 line we need 3 columns
# for each row, lookup the coord at row * step 
# add these things up


# part 2: 1,1 * 3,1 * 5,1 * 7,1 * 1,2


map = []
with open('input.txt', 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    map.append(list(row[0]))

def treefinder(map, right_increment, down_increment):
  width = len(map[0])
  trees_encountered = 0
  current_column = 0
  current_row = 0

  while current_row < len(map):
    if current_column > width - 1:
      current_column = current_column - width
    if map[current_row][current_column] == '#':
      trees_encountered += 1
    current_column += right_increment
    current_row += down_increment

  return trees_encountered

print treefinder(map, 1, 1)
print treefinder(map, 3, 1)
print treefinder(map, 5, 1)
print treefinder(map, 7, 1)
print treefinder(map, 1, 2)

print "product: ", treefinder(map, 1, 1) * treefinder(map, 3, 1) * treefinder(map, 5, 1) * treefinder(map, 7, 1) * treefinder(map, 1, 2)
