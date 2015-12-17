# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

import re

def donuts(count):
    if count < 10:
        print 'Number of donuts: %s' % (count)
    else:
        print 'Number of donuts: many'

donuts(4)
donuts(9)
donuts(10)
donuts(99)

def both_ends(s):
    if len(s) > 2:
        print s[0:2] + s[-2:]
    else:
        print ' '

both_ends('spring')
both_ends('Hello')
both_ends('a')
both_ends('xyz')

def fix_start(s):
    template = s[0]
    changed_string = s[1:].replace(template, '*')
    print template + changed_string

fix_start('babble')
fix_start('aardvark')
fix_start('google')
fix_start('donut')

def mix_up(a, b):
    slice_a = a[0:2]
    slice_b = b[0:2]
    new_a = slice_b + a[2:]
    new_b = slice_a + b[2:]
    print "%s %s" % (new_a, new_b)

mix_up('mix', 'pod')
mix_up('dog', 'dinner')    
mix_up('gnash', 'sport')
mix_up('pezzy', 'firm')

def verbing(s):
    if len(s) > 2:
        if s[-3:] == 'ing':
            print s + 'ly'
        else:
            print s + 'ing'
    else:
        print s

verbing('hail')
verbing('swimming') #Spelling. ;)
verbing('do')

def not_bad(s):
    good = re.sub('not.*?bad', 'good', s) #Had another solution, but regular expressions are just so much better.
    print good

not_bad('This movie is not so bad')
not_bad('This dinner is not that bad!')   
not_bad('This tea is not hot')
not_bad("It's bad yet not")


def front_back(a, b):
    ad = (len(a) + 1) // 2 #Integer division
    bd = (len(b) + 1) // 2
    print a[:ad] + b[:bd] + a[ad:] + b[bd:]

front_back('abcd', 'xy')
front_back('abcde', 'xyz')
front_back('Kitten', 'Donut')