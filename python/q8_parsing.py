import csv

with open('football.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	difference = 1000
	team = ''
	for row in reader:
		if abs(int(row[5]) - int(row[6])) < difference:
			difference = abs(int(row[5]) - int(row[6]))
			team = row[0]
	print difference
	print team
		