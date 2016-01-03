[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
"""
Here is the problem:

Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.
"""

"""
Building on what I did before, I read the data from 2002FemResp and its accompanying dictionary into a new database, called 'secondDb'.
I had to grab the functions for the appropriate data file from chap01soln.py.
"""



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
    print "wtf1"
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
    print "wtf2"
    preg = ReadFemResp()

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    con = MySQLdb.connect("127.0.0.1","root","aardvark123", 'secondDb')
    data = psql.write_frame(df, name='numkdhh', con=con, flavor='mysql', if_exists='fail')
    db.close()


def main():
    MakeFrames()

if __name__ == '__main__':
    main()

#Once again, I moved from my placeholder file to a clean one, to do my coding.

import MySQLdb as mdb
import numpy
import matplotlib.pyplot as plt


con = mdb.connect('localhost', 'root', 'aardvark123', 'secondDb')
with con:
    cur = con.cursor()
    #Part of the challenge here was in properly formatting the data as integers as opposed to longs, tuples, or longs in tuples.
    #First execute statement was "ALTER TABLE numkdhh ADD COLUMN kids int" to add the column we needed to recast the values from long to int.
    #Second execute statement was "UPDATE numkdhh SET kids = numkdhh" to fill the column.
    #Python, in its infinite wisdom, apparently decided to represent the things as longs even though they were cast as ints in the db,
    #which is why I had to use the following code in order to produce two lists of int values.

    cur.execute("SELECT kids from numkdhh")
    rows = cur.fetchall()
    unbiased = []
    for row in rows:
        result = row[0]
        unbiased.append(int(result))

    cur.execute("SELECT kids from numkdhh where kids != 0")
    rows = cur.fetchall()
    biased = []
    for row in rows:
        result = row[0]
        biased.append(int(result))

#Once this had been resolved, pyplot from matplotlib let me produce histograms/PDFs from the result.

unbiasedpmf = plt.hist([unbiased], bins=[0,1,2,3,4,5,6], normed=1)


biasedpmf = plt.hist([biased], bins=[1,2,3,4,5,6], normed=1)

print "The unbiased probability distribution is: " 
print unbiasedpmf
print "The biased probability distribution is: " 
print biasedpmf

"""
Results:
(array([ 0.4661782 ,  0.21405207,  0.19625801,  0.08713856,  0.02564438, 0.01072877]), array([0, 1, 2, 3, 4, 5, 6]), <a list of 6 Patch objects>)
(array([ 0.40098039,  0.36764706,  0.16323529,  0.04803922,  0.02009804]), array([1, 2, 3, 4, 5, 6]), <a list of 5 Patch objects>)
"""
#Given the small size of the data set, I decided to cut some corners and just write the things out by hand.

unbiasedMean = 0*0.4661782 + 1*0.21405207 + 2*0.19625801 + 3*0.08713856 + 4*0.02564438 + 5*0.01072877

biasedMean = 1*0.40098039 + 2*0.36764706 + 3*0.16323529 + 4*0.04803922 + 5*0.02009804

print "The unbiased mean number of children is %s" % (unbiasedMean) #1.02420514
print "The biased mean number of children is %s" % (biasedMean) #1.91862746

#As you can see, the biased mean, derived from only asking children as opposed to including those households who had none, provides
#a very different result.
