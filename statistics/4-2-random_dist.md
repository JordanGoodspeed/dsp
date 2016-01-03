[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

#This is assignment was much simpler (Thanks!), as it did not require any outside data at all.

import random
import matplotlib.pyplot as plt
import numpy as np

rand = []
for i in range(0,1000):
    rand.append(random.random())

randhist = plt.hist([rand], bins=[.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0], normed=True)

print randhist


"""Given the size of the data set, playing around with the bin size and norm can only do so much.
    It is difficult to discern the signal from the noise.  Instead, we use a cumulative distribution function instead.
"""
sorted_data = np.sort(rand)


plt.step(sorted_data, np.arange(sorted_data.size))

plt.show()

#The CDF shows, like the histogram, that the distribution is basically uniform, subject to noise.


	
