import csv

with open("C:\\Users\\hp\\Downloads\\mac.csv", 'r') as file:
    csvreader = csv.reader(file)
   # header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
#print(header)
print(rows)
