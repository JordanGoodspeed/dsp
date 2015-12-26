from collections import Counter
import csv
import re

#Question 1
with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	results = ""
	for row in reader:
		b = re.sub("[^a-zA-Z\s]+", "", row[1])
		results += " " + b
	counts = Counter(re.findall(r"\w+", results))
	print len(counts)
	print counts

"""
Depending on the size of the dataset, it may be faster not to use regex, in which case you could use the code below:

from collections import Counter
import csv

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	list1 = []
	for row in reader:
		list1.extend(row[1].replace(".","").split())
	counts = Counter(list1)
	print counts
"""

#Question 2
from collections import Counter
import csv
import re

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	results = ""
	for row in reader:
		results += " " + re.sub("\s", "_", row[2])
	counts = Counter(re.findall("\w+", results))
	print len(counts)
	print counts

#Question 3
from collections import Counter
import csv
import re

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	results = []
	for row in reader:
		results.append(row[3])
	print results

#Question 4
from collections import Counter
import csv
import re

with open('faculty.csv', 'rb') as f:
	reader = csv.reader(f, delimiter=",")
	reader.next()
	results = []
	for row in reader:
		domain = re.search("@[\w.]+", row[3])
		results.append(domain.group())
	counts = Counter(results)
	print counts
	print counts.keys()
