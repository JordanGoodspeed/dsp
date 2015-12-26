import csv

emails = []

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	for row in reader:
		emails.append(row[3])

with open('emails.csv', 'wb') as f:
	writer = csv.writer(f, dialect='excel')
	for item in emails:
		writer.writerow([item])
