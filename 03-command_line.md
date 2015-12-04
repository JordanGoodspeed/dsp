# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 

---
ls - list files in current directory
	mkdir - make a directory
	cd - change directory
	rmdir - remove a directory
	touch -create a file
	*all of these things are ones I use everyday*
	cp - copy a file
	mv - move a file, also renames it
	rm - remove a file (I use this one occasionally, too)
	pushd - Move around between directories
	popd - Takes you back to the last directory you pushed from


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ls - lists files in current directory
	ls -a - lists all files, including hidden ones (denoted by the "." at the beginning of the file name)
	ls -l - Lists all files in long form, including file type, permissions, owner, group, etc.
	ls -lh - Lists all files in long form, but the -h modifies the output to a more human-readable form
	ls -la, ls -lha are all valid combinations.  ls -ha or ls -ah doesn't really do anyting, as you are not displaying the file size.
---


---

What does `xargs` do? Give an example of how to use it.

> > xargs stands for 'execute argument'.  It takes the input you give it, and then executes it at the specified location.  This is really useful when paired with, for instance, the find command.  You can take the output of the find command as the input of xargs, and have it execute the rm -rf command on the files you specified.

---

