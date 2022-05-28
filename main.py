import csv

with open('titles.csv', 'r') as homefile:
    reader = csv.reader(homefile)
    for row in reader:
        print(row)
