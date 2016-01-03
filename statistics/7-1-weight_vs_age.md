[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)
"""
Here is the problem:

 Using data from the NSFG, make a scatter plot of birth weight versus mother’s age. Plot percentiles of birth weight versus mother’s age. Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?
"""

#This problem involved the use of the first dataset, stored on my computer as PregDat from firstDb.

import MySQLdb as mdb
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as sc
from itertools import izip


con = mdb.connect('localhost', 'root', 'aardvark123', 'firstDb')
with con:
    #These first couple of variables were for the scatter and hexbin plots, as well as for computing the Spearman's and Pearson's 
    #correlations.  All of the took me very little time at all.
    cur = con.cursor()
    cur.execute("SELECT totalwgt_lb from PregDat where totalwgt_lb is NOT NULL")
    weight = cur.fetchall()
    cur.execute("SELECT agepreg from PregDat where totalwgt_lb is not null")
    age = cur.fetchall()
    #These next two were for the calculation of the percentiles and the production of the graph.  To be honest, I did not entirely 
    #what his code did, or what he was asking for, so this took me a long, long, long time to get (hopefully) right.
    cur.execute("SELECT DISTINCT Round(agepreg) from PregDat where totalwgt_lb is not null")
    roundAge = cur.fetchall()
    cur.execute("SELECT Round(agepreg), group_concat(totalwgt_lb) from PregDat where totalwgt_lb is not null group by Round(agepreg)")
    new = cur.fetchall() 

#While the axes are not labeled, mother's age is the x-axis, and birthweight in pounds is the y-axis for both charts.

plt.scatter(age, weight)
plt.show()

plt.hexbin(age, weight)
plt.show()

#The scipy module had very handy methods for both of these.

print "Pearson's correlation is: "
print sc.stats.pearsonr(age, weight)
print "Spearman's correlation is: "
print sc.stats.spearmanr(age, weight)

#Now, the group_concat SQL query, which I used to get all of the weights for each rounded age, returns a string of all the numbers
#concatenated together, separated only by commas.  Also, each rounded age (why the people chose to record ages as floats is beyond me)
#had a varying number of values.  Like Downey, I chose to bin the ages by three, albeit in a slightly different way.

#This is the function that I defined for iterating over my lists of tuples from MySQL three at a time.
def grouped(iterable, n):
    return izip(*[iter(iterable)]*n)

#Here is the array and function used to convert the list tuples of ages and weights into lists, and then the strings with the weights
#into lists of floats.  I then concatenated every three of these into one and added it to my binnedWeightBy3 list.
binnedWeightBy3 = []

for i, j, k in grouped(new, 3):
    i = list(i)
    i[1] = i[1].replace(",", " ").split()
    a = map(float, i[1])
    j = list(j)
    j[1] = j[1].replace(",", " ").split()
    b = map(float, j[1])
    k = list(k)
    k[1] = k[1].replace(",", " ").split()
    c = map(float, k[1])
    binnedWeightBy3.append([a + b + c])

# Here is the array and function used to provide an array of averaged ages of equivalent length to the binned weights so that I could 
#plot it appropriately.

binnedAgeBy3 = []

for i, j, k in grouped(sorted(roundAge), 3):
    i = map(int, i)
    j = map(int, j)
    k = map(int, k)
    binnedAgeBy3.append((i[0] + j[0] + k[0]) / 3)

#These three arrays and final for loop were there to pick out the 25th, 50th, and 75th percentile values from the binned weights.

twentyFifth = []
fiftieth = []
seventyFifth = []

for i in binnedWeightBy3:
    twentyFifth.append(np.percentile(i, 25))
    fiftieth.append(np.percentile(i, 50))
    seventyFifth.append(np.percentile(i, 75))

#And now, after hours of work, and numerous false starts and deadends, here is the graph with the percentiles plotted.
#It is almost identical to that he provided, leading me to believe I did all this right.  *fingers crossed*.

plt.plot(binnedAgeBy3, twentyFifth)
plt.plot(binnedAgeBy3, fiftieth)
plt.plot(binnedAgeBy3, seventyFifth)
plt.show()

