# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.

git version 2.5.0

### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python

Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "help", "copyright", "credits" or "license" for more information.

ipython

Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "help", "copyright", "credits" or "license" for more information.

ipython notebook

2015-12-04 11:32:14.012 [NotebookApp] Using system MathJax
2015-12-04 11:32:14.177 [NotebookApp] Serving notebooks from local directory: /home/jordan
2015-12-04 11:32:14.178 [NotebookApp] 0 active kernels 
2015-12-04 11:32:14.178 [NotebookApp] The IPython Notebook is running at: http://localhost:8888/
2015-12-04 11:32:14.178 [NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
Created new window in existing browser session.
^C2015-12-04 11:32:29.536 [NotebookApp] interrupted
Serving notebooks from local directory: /home/jordan
0 active kernels 
The IPython Notebook is running at: http://localhost:8888/

spyder

I've decided to skip a screenshot, and there is nothing from the Terminal to copy and paste, so I hope you will take my word for it that Spyder is on my computer.

```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```
jordan@jordan-HP-EliteBook-8560w:~$ ipython
Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
Type "copyright", "credits" or "license" for more information.

IPython 2.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import numpy

In [2]: import scipy

In [3]: import statsmodels

In [4]: import matplotlib

Python 2.7.10 (default, Oct 14 2015, 16:09:02) 
[GCC 5.2.1 20151010] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sklearn
>>> import pandas
>>> 


---

Did you install Python 2 or 3? Why? How can you check the version of Python installed if you happen to be on an unfamiliar computer?

>> Python 2, as it is still the standard in most places (including this bootcamp).  I confirmed this by typing python into the command line, which showed that I was running Python 2.7.10, as seen above.  You can also do python -v to get the version, and other options exist if you have multiple version of Python on your computer and want to check them all.

---


### Homebrew

If you use a Mac, install [Homebrew](http://brew.sh/) if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

N/A Am using Ubuntu.