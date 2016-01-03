#[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
"""
Here is the problem:

Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?
"""

"""
The pregnancy data is contained in 2002FemPreg.dat.gz, which is a gzip-compressed file in ASCII plain text.  Its formatting is contained in 2002FemPreg.dict, which is a Stata file that contains the indices, variable names, and types that identify the information in the data file. The function ReadFemPreg in the nsfg2.py file reads the data, and then calls the CleanFemPreg function, which cleans the data to eliminate errors, convert some units, and provides a new column, totalweight_lb, which it computes from the birthweight_lb and birthweight_oz columns.  Within the chap02soln.py file, the author provides the code to calculate the means, variance, and Cohen D for the weight of firstborn babies versus all others.  The mean weight of firstborns is 7.20109443044lbs, while that of all other infants is 7.32585561497lbs.  The variance in the weights for firstborns is 2.01802730092lbs, and that for all others is 1.9437810259lbs.  The Cohen D for the weights was calculated within the same function (WeightDifference from the chap02soln.py) using the difference of the means above, divided by the pooled standard deviation (which itself is calculated from the variance of each, times the sample size of each (derived by calling len(column), divided by the combined sample size of firstborns versus others).  This computes to -0.0886729270726, which is greater than the provided Cohen D for differences in pregnancy lengths between firstborns and others (0.029), but smaller than, say, the 1.7 standard deviations difference in average sizes between men and women (about 1.7).

In order to understand this more fully, I chose to write the DataFrame built by pandas into a MySQLdb (as I have a little more experience with SQL than pandas, which I could then query using mysql statements.
"""

#I did this by taking the functions used to produce the DataFrame from ThinkStats, putting them into a temporary file, and appending
#a segment of code that wrote the dataframe into a MySQLdb.  I inserted print statements into his functions to help see the order in
#which they ran, and where best to put the code.

import bisect
import copy
import logging
import math
import random
import re
import cStringIO
from dateutil import parser
import MySQLdb
import pandas.io.sql as psql


from collections import Counter
from operator import itemgetter

import thinkplot

import numpy as np
import pandas 

import scipy
from scipy import stats
from scipy import special
from scipy import ndimage

from io import open

class FixedWidthVariables(object):
    def __init__(self, variables, index_base=0):
        self.variables = variables
        self.colspecs = variables[['start', 'end']] - index_base
        self.colspecs = self.colspecs.astype(np.int).values.tolist()
        self.names = variables['name']
    def ReadFixedWidth(self, filename, **options):
        df = pandas.read_fwf(filename,colspecs=self.colspecs,names=self.names,**options)
        return df

def ReadStataDct(dct_file, **options):
    print "Reading the Dict"
    type_map = dict(byte=int, int=int, long=int, float=float, double=float)

    var_info = []
    for line in open(dct_file, **options):
        match = re.search( r'_column\(([^)]*)\)', line)
        if match:
            start = int(match.group(1))
            t = line.split()
            vtype, name, fstring = t[1:4]
            name = name.lower()
            if vtype.startswith('str'):
                vtype = str
            else:
                vtype = type_map[vtype]
                long_desc = ' '.join(t[4:]).strip('"')
                var_info.append((start, vtype, name, fstring, long_desc))
    columns = ['start', 'type', 'name', 'fstring', 'desc']
    variables = pandas.DataFrame(var_info, columns=columns)
    variables['end'] = variables.start.shift(-1)
    variables.loc[len(variables)-1, 'end'] = 0

    dct = FixedWidthVariables(variables, index_base=1)
    return dct
def MakeFrames():
    print "Making Frames"
    preg = ReadFemPreg()
    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]
    
    return live, firsts, others
def ReadFemPreg(dct_file='2002FemPreg.dct', dat_file='2002FemPreg.dat.gz'):
    print "Reading the File"

    dct = ReadStataDct(dct_file, encoding='iso-8859-1')
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemPreg(df)
    return df

#Here is where I determined that the code should be written to take the cleaned data and insert it into MySQLdb.
#I also added .loc to his code to get it to run smoothly on my computer.

def CleanFemPreg(df):
    print "Cleaning the File"
    df.agepreg /= 100.0
    df.birthwgt_lb.loc[df.birthwgt_lb > 20] = np.nan
    na_vals = [97, 98, 99]
    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
    df.loc['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
    df.phase = np.nan
    con = MySQLdb.connect("127.0.0.1","root","aardvark123", 'firstDb')
    data = psql.write_frame(df, name='PregDat', con=con, flavor='mysql', if_exists='fail')
    db.close()

#Having done that, I then wrote the following code in a new file, and calculated the appropriate values by querying the database
#and performing the relevant operations on the results.  The numbers I got were basically the same, though the trailing decimals that were #well outside the likely number of significant figures for the scale were a litte bit different from his.

import MySQLdb as mdb
import numpy
import math


con = mdb.connect('localhost', 'root', 'aardvark123', 'firstDb')
with con:
    cur = con.cursor()

    #I ran a couple of execute statements first to modify the table appropriately.
    #First execute statement was "ALTER TABLE PregDat ADD COLUMN totalwgt_lb float" to add the column we needed.
    #Second execute statement was ""UPDATE PregDat SET totalwgt_lb = (birthwgt_lb + birthwgt_oz / 16.0)"" to fill the column


    cur.execute("SELECT totalwgt_lb from PregDat where birthord = 1 AND totalwgt_lb is NOT NULL")
    first = cur.fetchall()
    cur.execute("SELECT totalwgt_lb from PregDat where birthord != 1 AND totalwgt_lb is NOT NULL")
    others = cur.fetchall()

mean0 = numpy.mean(first + others)
mean1 = numpy.mean(first)
mean2 = numpy.mean(others)

var1 = numpy.var(first)
var2 = numpy.var(others)

print('Mean')
print('First babies', mean1)
print('Others', mean2)

print('Variance')
print('First babies', var1)
print('Others', var2)

diff = mean1 - mean2
n1 = len(first)
n2 = len(others)
pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
cohenD = diff / math.sqrt(pooled_var)
print('Cohen d', cohenD)
