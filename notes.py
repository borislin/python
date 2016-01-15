# Notes taken when I learnt Python on tutorialspoint.com
# From Jan 14, 2016 to Present
# Borui Lin
# University of Waterloo


======= Tuples =======

- immutable Python objects
- enclosed by parentheses, separated by commas
- for a tuple containing a single value, we have to include a comma, like: tup1 = (50,)
- access values in tuples: use square brackets
- delete an entire tuple: del tup
- basic operations: len(), +, *, in, iteration
- any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples
- built-in functions: cmp(tuple1, tuple2), len(tuple), max(tuple), min(tuple), tuple(seq)

======= Dictionary =======

- each key is separated from its value by a colon
- values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples
- enclosed by curly braces
- del dict['Name'] # remove entry with key 'Name'
- dict.clear() # remove all entries in dict
- del dict # delete entire dictionary
- when duplicate keys encountered during assignment, last assignment wins
- built-in functions: cmp(dict1, dict2), len(dict), str(dict), type(variable), dict.clear(), dict.copy() | returns a shallow copy, dict.fromkeys(seq, value) | value parameter is optional, dict.get(key, default=None), dict.has_key(key), dict.items() | returns a list of dict key-value tuple pairs, dict.keys(), dict.setdefault(key, default=None) | similar to get(), but will set dict[key]=default if key is not already in dict, dict.update(dict2) | add dict2 into dict, dict.values()

======= Date & Time =======

- import time
- time.time() | returns the current system time in ticks since 12:00am, Jan 1, 1970
- time.localtime(time.time()) | current time represented in time-tuple
- time.asctime(time.localtime(time.time())) | human readable format
- built-in functions: time.altzone, time.asctime([tupletime]),
					  time.clock() | returns the current CPU time as a floating-point number of seconds. To measure computational costs of different approaches, the value of time.clock is more useful than that of time.time(),
					  time.ctime([secs]) | like asctime(localtime(secs)),
					  time.gmtime([secs]), time.localtime([secs]), time.mktime(tupletime), time.sleep(secs), time.strftime(fmt[,tupletime]), time.strptime(str,fmt='%a %b %d %H:%M:%S %Y'), time.time(), time.tzset()
- import calendar
- calendar.month(2008, 1)
- ...

======= Functions =======

- all arguments in Python are passed by reference
- however, if the argument is assigned a new reference inside the called function, values in the calling function stay unchanged
- assignment operator always creates a new Python object | ******IMPORTANT******
- keyword argument: printme( str = "My string" ) | manually match argument value with the corresponding parameter
- default arguments
- variable-length arguments: def printinfo(arg1, *vartuple): ... return;
- lambda functions: return just one value in the form of an expression, like: sum = lambda arg1, arg2 : arg1 + arg2;

======= Modules =======

- each module is a individual file
- a module is loaded only once, regardless of the number of times it is imported
- from fib import fibonacci
- from fib import *
- Python assumes that any variable assigned a value in a function is local
- global Money: tells Python Money is a global variable, do not treat it as a local variable
- The dir() built-in function returns a sorted list of strings containing the names defined by a module
- globals(), locals() | both return a dictionary
- reload(module_name) | reload(hello) instead of reload("hello")
- import Phone | importing a whole package rather than a single module
- in Phone/__init__.py: from Pots import Pots, from Isdn import Isdn, from G3 import G3

======= Files I/O =======

- print: print to screen, can take zero or more expressions separated by commas
- raw_input(): reads one line from standard input and returns it as a string (removing the trailing newline)
- input(): equivalent to raw_input, except that it assumes the input is a valid Python expression and returns the evaluated result to you
- file object = open(file_name, access_mode, buffering) # open a file, default access_mode is read(r)
- file.closed, file.mode, file.name, file.softspace
- file.close(), file.read([count]) | passed parameter is the number of bytes to be read, if missing, read the entire file, file.write()
- file.readline([count])
- file.tell(): tells the current position within the file
- file.seek(offset, from): file.seek(0, 0) moves the pointer to the beginning of the file. When from = 1, means "current position". When from = 2, means "end of the file".
- import os
- os.rename(current_file_name, new_file_name)
- os.remove(file_name)
- os.mkdir(new_dir_name)
- os.chdir(new_dir_name)
- os.getcwd() # give location of the current directory
- os.rmdir(dir_name)

======= OOP =======

- class variable: similar to static variable in C++, shared among all objects of the same class
- instance variable: defined inside a method
- __init__(): class constructor
- first argument to each method is self
- can add, remove, or modify attributes of classes and objects at any time: emp1.age = 7 or del emp1.age
- Python has Garbage Collection: it runs when an object's reference count reaches zero'
- __del__(): class destructor
- inheritance: class Child(Parent): ...
- a child class can have multiple parent classes
- issubclass(sub, sup), isinstance(obj, Class)
- __add__(self, other): override the plus operator
- __str__(self): printable string representation
- __secretCount: private member of the class, Python internally changes the name to _className__attrName, so can still be accessed using the right name
- 