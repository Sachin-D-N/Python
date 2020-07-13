#iterators
"Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol."
#An object which will return data, one element at a time.
#We use the next() function to manually iterate through all the items of an iterator.


l=[1,2,3,4,5]
l1=iter(l)
l1
print(l1)

#to  iterate one by one use next()
#manually
next(l1)
 #or
 
l1.__next__() #when we reaches end it will gives stop iteration error


#auto matically
for i in l:
    print(i)
 
    
    
 #infinate iterate    
int()
inf = iter(int,5)
next(inf)
next(inf)


class infinate():
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        num=self.num
        self.num+=2
        return num

c=infinate()
c.__iter__()
c.__next__()

c=iter(infinate())
next(c)

class infinate():
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<20:
            num=self.num
            self.num+=2
            return num
        else:
            raise StopIteration

c=iter(infinate())
next(c)

#generators
"""create iterations easily using Python generators, how is it different from iterators 
and normal functions, and why you should use it."""

#in a generator we use yield insted of the return statement
#yield and return will return some value from the function

#while a return statement terminates a function entirely, 
#yield statement pauses the function saving all its states and later continues from there on successive calls.

"""A generator is a special type of function which does not return a single value, 
instead it returns an iterator object with a sequence of values."""


def myGenerator():
    print('First item') #it will pauses the function saving all it states
    yield 10

    print('Second item')#later call from the successive calls
    yield 20

    print('Last item')
    yield 30
            
    
gen=myGenerator()
next(gen)


def myGenerator():
    print('First item') #return statement terminates function entirely
    return 10

    print('Second item')
    return 20

    print('Last item')
    return 30

gen=myGenerator()
next(gen)


#using return statement

def myGenerator():
    print('First item')
    yield 10

    return 

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen=myGenerator()
next(gen)


def getSequenceUpTo(x): 
    for i in range(x):
        yield i
        
seq=getSequenceUpTo(5)
next(seq)


#shortest expression
squres = (x*x for x in range(5))
next(squres)


sum(x*x for x in range(5))


def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1,-1,-1):
        yield my_str[i]
        
rev_str("sachin")  
        


for char in rev_str("hello"):
     print(char)


"""
str='shhsh'
length = len(str)
for i in range(length -1,-1): #getting knowledge of range
     print(i)

        
a=list(range(2,8))"""


def fibanosi(n):
    a=1
    b=2
    for i in range(n):
        yield a
        a,b=b,a+b
        
for j in fibanosi(10):
    print(j)
    
#closure function
#nested function
def sachin(msg):
    def sachi():
        print('sp')
    sachi()
sachin(123)


def sachin(msg):
# This is the outer enclosing function

    def sachi():
# This is the nested function
        print(msg)

    return sachi  # this got changed

# Now let's try calling this function.
# Output: Hello
another = sachin("Hello")
another()    
        
del sachin #but it is not defined
another()  #its return

#when do have closure

"""The criteria that must be met to create closure in Python are summarized in the following points.

We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function."""


#when to use closure
"""Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solutions. 
But when the number of attributes and methods get larger, better implement a class."""


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

m=make_multiplier_of(5)
m1=make_multiplier_of(8)
m(3)
m1(8)
del make_multiplier_of

m(3)
m1(8)
m(6)

#Decorators in Python make an extensive use of closures as well.
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

m=make_multiplier_of(5)
m1=make_multiplier_of(8)
make_multiplier_of.__closure__
m1.__closure__[0]
m1.__closure__[0].cell_contents
m.__closure__[0].cell_contents



#decorators
"Decorators are gives the extra functionality to the existing code"

    
#Python has an interesting feature called decorators to add functionality to an existing code.
#This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

def first(msg):
    print(msg)    

first("Hello")

second = first
second("Hello")
del first
#first
second('143')


#Such function that take other functions as arguments are also called higher order functions.
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(fun, x):
    result = fun(x)
    return result

operate(inc,5)
operate(dec,1)


#a function can return another function.
def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

#Outputs "Hello"
new()

#Here, is_returned() is a nested function which is defined and returned, each time we call is_called().

#any object which implements the special method __call__() is termed callable.

#so, in the most basic sense, a decorator is a callable that returns a callable.

#Basically, a decorator takes in a function, adds some functionality and returns it.

def sachin(func):
    def paddu():
        print('love you')
        func()
    return paddu
def love():
    print ('good pair')
    
s=sachin(love) #sachin(love) is a decorator
s()

"""We can see that the decorator function added some new functionality to the original function. 
This is similar to packing a gift. The decorator acts as a wrapper. 
The nature of the object that got decorated (actual gift inside) does not alter. 
But now, it looks pretty (since it got decorated)."""

#Generally, we decorate a function and reassign it as,

love= sachin(love)
love()


#We can use the @ symbol along with the name of the decorator function and 
#place it above the definition of the function to be decorated.


@sachin
def love():
    print ('good pair')
    
love()
""" is equal to"""
s=sachin(love) #sachin(love) is a decorator
s()


#decoration using parameters
def divide(a, b):
    return a/b

divide(5,2)

divide(5,0) #error

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

divide(1,2)
divide(1,0)


def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        func(*args, **kwargs)
    return inner

def s(func):
   # print('sachin')
    def inner(*args,**kwargs):
        print('why i decorate it')
        func(*args, **kwargs)
    return inner
    
@works_for_all
@s
def sp(msg):
    print('ps')
sp('5')   

s=works_for_all(s(sp))
s('5')


#@property method
#we will learn about Python @property; pythonic way to use getters and setters.


class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

r=Celsius()
r.temperature=5 #setter
r.to_fahrenheit()
r.temperature #getter

"Whenever we assign or retrieve any object attribute like temperature, as show above, Python searches it in the object's __dict__ dictionary."
r.__dict__


#property(fget=None, fset=None, fdel=None, doc=None)

#frame work definition

#A framework is a type of software library that provides generic functionality which can be extended by the programmer to build applications. 
#Flask and Django are good examples of frameworks intended for web development.

"""A framework is distinguished from a simple library or API. An API is a piece of software that a developer can use in his or her application. 
A framework is more encompassing: your entire application is structured around the framework (i.e. it provides the framework around which you build your software)."""




