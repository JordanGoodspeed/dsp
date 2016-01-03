[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

"""Here is the problem:

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.
"""

from __future__ import print_function

import math
import sys
import pandas
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


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


def Summarize(df, column, title):
    """Print summary statistics male, female and all."""

    items = [
        ('all', df[column]),
        ('male', df[df.sex == 1][column]),
        ('female', df[df.sex == 2][column]),
        ]

    print(title)
    print('key\tn\tmean\tvar\tstd\tcv')
    for key, series in items:
        mean, var = series.mean(), series.var()
        std = math.sqrt(var)
        cv = std / mean
        t = key, len(series), mean, var, std, cv
        print('%s\t%d\t%4.2f\t%4.2f\t%4.2f\t%4.4f' % t)


def CleanBrfssFrame(df):
    # clean height
    df.htm3.replace([999], float('NaN'), inplace=True)

def ReadBrfss(filename='CDBRFS08.ASC.gz', compression='gzip', nrows=None):
    """Reads the BRFSS data.

    filename: string
    compression: string
    nrows: int number of rows to read, or None for all

    returns: DataFrame
    """
    var_info = [
        ('age', 101, 102, int),
        ('sex', 143, 143, int),
        ('wtyrago', 127, 130, int),
        ('finalwt', 799, 808, int),
        ('wtkg2', 1254, 1258, int),
        ('htm3', 1251, 1253, int),
        ]
    columns = ['name', 'start', 'end', 'type']
    variables = pandas.DataFrame(var_info, columns=columns)
    variables.end += 1
    dct = FixedWidthVariables(variables, index_base=1)

    df = dct.ReadFixedWidth(filename, compression=compression, nrows=nrows)
    CleanBrfssFrame(df)
    return df

def heightInInterval():
	mu = 179.34
	sigma = 7.29
	a = norm.cdf(185.42, loc=mu, scale=sigma) - norm.cdf(177.8,loc=mu, scale=sigma)
	return a
    
def main(script, nrows=1000):
    
    nrows = int(nrows)    
    df = ReadBrfss(nrows=nrows)

    Summarize(df, 'htm3', 'Height (cm):')
    print(heightInInterval())
   
    
if __name__ == '__main__':
    main(*sys.argv)

"""
The answer is 0.381518151691% of the male population.  My numbers (from his code) are slightly different from the numbers he gives
in his solution for mean height, standard deviation, and result.  Also, discovered that my print statements didn't work for an hour
because his code, which I have liberally borrowed here, was written in Python 3.



	
