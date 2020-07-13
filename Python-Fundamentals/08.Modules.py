#https://docs.python.org/3/py-modindex.html

"Modules"
#A file containing a set of functions you want to include in your application.
#packages are collection of modules
"""We can define our most used functions in a module and import it, instead of copying their definitions 
into different programs."""

import Example  #we want to create example.py module in local machine
Example.add(4,5)    

'Or'

from Example import add
add(22,2)


import math #import statement access the definitions of it
print("The value of pi is", math.pi)

int(math.sqrt(9))


#renaming

import math as m
m.pi


#We can import specific names from a module without importing the module as a whole.
from math import pi 
math.pi

#import all by *
from math import*
math.tan(52)

import datetime
datetime.datetime.now()

#scratch 
"""While importing a module, Python looks at several places. Interpreter first looks for a built-in module then (if not found) into a list of directories defined in sys.path. 
The search is in this order."""

#The current directory.
#PYTHONPATH (an environment variable with a list of directory).
#The installation-dependent default directory.

import sys
sys.path

import mymodule
import mymodule #only once it will be reloded

#for import again we want to reload it
#We can use the reload() function inside the imp module to reload a module. This is how its done.
import imp
imp.reload(mymodule)


dir(Example)
""">>> dir(example)
['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']"""

 # All other names that begin with an underscore are default Python
# attributes associated with the module (we did not define them ourself).
 
 
"package"
#pip install colorama (in command formaat we used to change the color)
from colorama import init
init()
from colorama import Fore
print(Fore.RED+"i jshnj js")

#packages and sub packages are the folders and subfolders in the python
#python should have the __init__ file in the package
from Main_package import some_mainscript  #creating package and importing module from package
from Main_package.Sub_package import sub_script
some_mainscript.report_main()
sub_script.sub_report()

#__name__==__class__
"when module one gets loaded, its __name__ equals 'one' instead of __main__."


import statistics
statistics.mean([2,5,6,9]) #statistics module

"Collection module"
#function returns a tuple-like object with named fields. These field attributes are accessible by lookup as well as by index.
import collections  
student=collections.namedtuple('student',['name','marks','age'])

s1=student('tahir',50,60)
s1.name
s1.age
s1[0]

#ordered dict() it will order of the keys in which they were first inserted.
import collections
d1=collections.OrderedDict()
d1['A']=65
d1['C']=67
d1['B']=66
d1['D']=68

for k,v in d1.items():
    print (k,v)
    
    
dict1=dict(age=23,name='sachi')


#deque()  
"""A deque object support appends and pops from either ends of a list. 
It is more memory efficient than a normal list object. In a normal list object, the removal of any item causes 
all items to the right to be shifted towards left by one index. Hence, it is very slow."""

import collections
q=collections.deque([0,2,4,5]) #appends the values to the left
q.appendleft(1)




#third party libraries
#IPython - A better interactive Python interpreter
#requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
#Flask - a lightweight framework for making web applications and APIs.
#Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
#Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
#pytest - extends Python's builtin assertions and unittest module.
#PyYAML - For reading and writing YAML files.
#NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
#pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
#matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
#ggplot - Another 2D plotting library, based on R's ggplot2 library.
#Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
#pyglet - A cross-platform application framework intended for game development.
#Pygame - A set of Python modules designed for writing games.
#pytz - World Timezone Definitions for Python







