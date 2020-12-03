import csv

# which 2 numbers in input.txt sum to 2020

# what is their product?

numbers = []

with open('input.txt', 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    numbers.append(int(row[0]))

for num1 in numbers:
   for num2 in numbers:
     if 2020 == num1 + num2:
        print(num1 * num2)
        break  

