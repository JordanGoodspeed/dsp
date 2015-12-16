# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are both sequences of values, which can be of any type.  The key difference between them is that tuples are immutable, while lists can be changed.  Tuples can also represent multiple values as a single one, allowing them to be used as keys in dictionaries, unlike lists (lists can still be values, though).

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

A list in Python is an ordered sequence of values, while a set is an unordered sequence of values.  Set elements must be hashable.  They cannot contain duplicates.  Because of this, sets cannot support slices, sorts, or other operations on ordered data.  They can, however, perform intersect, union, and other operations from set theory.  Sets are faster for finding a unique element, while lists are better at iterating over the whole selection.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

The lambda operator or function is a way of creating small anonymous (unnamed) functions, which are called at the moment of creation.  The syntax involves lambda, the arguments, a colon, and then the expression.  For example:

f = lambda x: x**2
	f(4)
		16
or:
a = ['Z', "a", 'E', "p"]

sorted(a)

['E', 'Z', 'a', 'p']

Sorted sorts upper case letters before lower.  Rather than write a new function in main, we can write a lambda expression just for this occasion:

sorted(a, key=lambda word: word.lower())

['a', 'E', 'p', 'Z']

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

A list comprehension is a way of creating a list without enumerating each element specifically.  You do it by creating a list, and within the square brackets you specify the operation to perform on i, the range of i, and any special methods of filtering, like so:

a = [i**2 for i in range(18) if i % 2 == 0]

This gives us the squares of the even numbers from 0 to 18 (non-inclusive).  What this is basically equivalent to is a 'map' (squaring each element) and 'filter' (selecting only even numbers) operation, like so:

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
evens = filter(lambda x: x % 2 == 0, list1)
square = map(lambda x: x**2, evens)


List comprehension is generally preferred in Python, though if you already have the function defined it is acceptable to use map().  It may be slightly faster to use map, as well, though this varies on the expression (built-in expressions are fine, lambda expressions are slower).  Map may also use less memory, as it is lazy in Python, while list comprehension is not.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





