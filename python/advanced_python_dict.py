#Question 1

import csv

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	faculty_dict = {}
	for row in reader:
		split = row[0].split()
		last = split[-1]
		if last in faculty_dict.keys():
			faculty_dict[last].append([row[1], row[2], row[3]])
		else:
			faculty_dict[last] = [row[1], row[2], row[3]]
	for key in sorted(faculty_dict.iterkeys())[0:3]:
		print "%s: %s" % (key, faculty_dict[key])


#Question 2

import csv

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	professor_dict = {}
	for row in reader:
		split = row[0].split()
		firstLast = [split[0], split[-1]]
		fuse = tuple(firstLast)
		professor_dict[fuse] = [row[1], row[2], row[3]]
	for key in sorted(professor_dict.iterkeys())[0:3]:
		print "%s: %s" % (key, professor_dict[key])

#Question 3

import csv

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	professor_dict = {}
	for row in reader:
		split = row[0].split()
		firstLast = [split[0], split[-1]]
		fuse = tuple(firstLast)
		professor_dict[fuse] = [row[1], row[2], row[3]]
	for key in sorted(professor_dict.iterkeys(), key=lambda x: x[-1])[0:3]:
		print "%s: %s" % (key, professor_dict[key])
	
	