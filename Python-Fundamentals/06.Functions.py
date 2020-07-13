"*****Functions******"
#by default return more than one value it comes with tuple
#function is a block of code it runs only when we called 
#return can store and we can use it

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(1,2)  #This is called Function call

#Function Header
"""Let's start with the function header, which is the first line of a function definition.

The function header always starts with the def keyword, which indicates that this is a function definition.
Then comes the function name (here, cylinder_volume), which follows the same naming conventions as variables. 
You can revisit the naming conventions below.
Immediately after the name are parentheses that may include arguments separated by commas (here, height and radius). 
Arguments, or parameters, are values that are passed in as inputs when the function is called, and are used in the function body. 
If a function doesn't take arguments, these parentheses are left empty.
The header always end with a colon :."""

def sachin():
    return 's'

sachin() #with out arguments 


"""Function Body
The rest of the function is contained in the body, which is where the function does its work.

The body of a function is the code indented after the header line. Here, it's the two lines that define pi and return the volume.
Within this body, we can refer to the argument variables and define new variables, which can only be used within these indented lines.
The body will often include a return statement, which is used to send back an output value from the function to the statement that called the function.
A return statement consists of the return keyword followed by an expression that is evaluated to get the output value for the function. 
If there is no return statement, the function simply returns None."""

#Print vs. Return in Functions


"One returns a value and one simply prints a value, without returning anything."

def show_plus_ten(num):
    print(num + 10)

show_plus_ten(5)
# this returns something
def add_ten(num):
    return(num + 10)
show_plus_ten(5)

#possible to pass values in two ways - by position and by name
#default arguments
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(7,11)

cylinder_volume(height=10, radius=7)  # pass in arguments by name



def readable_timedelta(days):
    weeks = days//7
    d = days%7
    return "{} week(s) and {} day(s)".format(weeks, d)

readable_timedelta(10)


#Argument   : A value we can pass to function when we call that function


#Function call :a Statement that  makes a function run


#Function :a block of code that has a name,but doesn't run untill we run


#Method: a function associated with object

#variable scope

"""If a variable is created inside a function, it can only be used within that function. 
Accessing it outside that function is not possible."""

x=10
def sachin(y):
    print(x)
    return x+y   
    


sachin(5)
x
 

#it will through error because we can't change the global variable inside the function   
egg_count = 0

def buy_eggs():
    #egg_count=0
    egg_count += 12 # purchase a dozen eggs
    return egg_count

buy_eggs() #UnboundLocalError: local variable 'egg_count' referenced before assignment


#Documentation
""" Functions are especially readable because they often use documentation strings, or docstrings
Docstrings are a type of comment used to explain the purpose of a function, and how it should be used.
 Here's a function for population density with a docstring."""
 
def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area

population_density(1,2)


#lambda Expressions
"In Python, anonymous function is a function that is defined without a name."
"""An anonymous function is a function that is not stored, but is associated with a variable. 
Anonymous functions can accept inputs and return outputs,"""

"""We can use lambda expressions to create anonymous function"""

"""especially useful for higher order functions, or functions that take in other functions as arguments."""
"""Expression yeilds a function object"""
"""these are destroyable functiom """

"it will returns default but functions are not returns"

x=(lambda x,y:x+y)(2,3)
x(2,3)

(lambda s=4,p=3:s+p)() 

(lambda s: s%2==0) (10)

(lambda s=4,p=3:s+p)(s=5,p=8) 

(lambda s: 'even ' if s%2==0 else 'odd') (2)

[lambda s: s**2 ,lambda s:s**4 ,lambda s:s**3] (2) # shows error

{'s':lambda s: s**2,'p':lambda p:p**2, 'l':lambda l:l**2}(1,2,3)# dict ,list,tuple are not callable

x=[lambda x,y:x+y] #colsed by square braket it will shows error you can take paranthisis.
x(2,3)

multiply = lambda x, y: x * y  #x ,y is argument x*y is expression

multiply(1,2)

#lambda key is used to express in lambda expression
#one or more parameters are used def myfunc(n):
#then that will separated by commas.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)

print(mydoubler(12))

#python recursion
#Recursion is the process of defining something in terms of itself.
#We know that in Python, a function can call other functions. It is even possible for the function to call itself. 
#These type of construct are termed as recursive functions.
#Following is an example of recursive function to find the factorial of an integer.

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 5
print("The factorial of", num, "is", calc_factorial(num))


"""Our recursion ends when the number reduces to 1. This is called the base condition.

Every recursive function must have a base condition that stops the 
recursion or else the function calls itself infinitely."""

#Disadvantages
"""Sometimes the logic behind recursion is hard to follow through.
Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
Recursive functions are hard to debug.
PREVIOUS"""

#scope of variables
"""A variable is only available from inside the region it is created. This is called scope."""

def var():
    var1=100
    print(var1)
    var2=200
    print(var2)
var()


#Local Scope

"""can only be used inside that function"""
x=10
def paddu():
    x=100;
    print(x)
paddu()
print(x)

#Global Scope

"""Global variables are available from within any scope, global and local."""

sachin=100;
def paddu():
 # sachin=10
  print(sachin)
  
paddu()
print(sachin)


"""If you operate with the same variable name inside and outside of a function,
 Python will treat them as two separate variables, one available in the global scope (outside the function) and 
one available in the local scope (inside the function):"""

sachin=100;
def paddu():
  sachin=10
  print(sachin)
  
paddu()
print(sachin)


#global
#If you use the global keyword, the variable belongs to the global scope:


sachin=100
def paddu():
    global sachin
    print(sachin)
    sachin=10
    print(sachin)
  
paddu()
print(sachin)

sachin=100
def paddu():
    global sachin
    print(sachin)
    sachin=5
    print(sachin)
    sachin=10
    print(sachin)
paddu()
print(sachin)



sachin=100
def paddu():
    global sachin
    
    print(sachin) #it will changes to global
    sachin=10
    print(sachin)
paddu()
print(sachin)

#non local variable

"""Nonlocal variable are used in nested function whose local scope is not defined. 
This means, the variable can be neither in the local nor the global scope."""
x=10
def outer():
    x = "local"
    
    def inner():
        #enclosing
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)
# inner() when function is inside the scope of the function inside only
outer()
print(x)
outer()
x
    
    
    
#example
x=1
def abc():
    x=5
    print(x)
    def f1():
        global x
        x=4
        print(x)
    print(x)
abc()
print(x)

#python in built functions

"1. abs() "

#it will prints negative number in positive

x=-5
abs(x)

"2. All"

#true : if all elements are iterable
#false: if one element is not iterable

x=[1,2,3,4]
all(x)


y=(1,2,0,1)
all(y)

"3.dir() "
#it will returns valid artributes of the object

n=[1,2,3,'sachin']
dir(n)
    
n={1,1}
dir(1)

p={1:2}
dir(p)

"4. divmod()"
#it will takes two numbers and gives the tuple of quotient,remainder
divmod(9,10)

divmod(19)#gives error

"5. Enumerate ()"

#it will returns the index of the given
l=[1,2,3]
for ind ,num in enumerate(l):
    print (ind,num)
    
"6. Filter()"
#map and filter applies the functions individually
#it will takes the function one argument and what we want to filter another argument
#it will return if the values  is true otherwise it is false don't return
#filter(function, iterable)
def s(a):
    if a<=0:
        return a
    
l=[0,1,2,3,4,5,6,8,9,-1,-2,-3]
list(filter(s,l))


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)


#without using function we can use None
l=[1,2,0,'0',False,True,None]
filtered=filter(None,l) #string 0 is also true
for i in filtered:
    print(i)
    

#example
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return 0

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)





# list of alphabets
alphabets = ['b', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if alphabet in vowels:
        return True
    else:
        return False
        
filteredVowels = filter(filterVowels, alphabets)

#print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)
    
    
list1=[4,5,2,6,7,0,-1,-2]
a=0

(lambda x: x>0)(a) #boolean ans is coming

list(filter(lambda x: x-2,list1))


l1=[1,2,3,4]
def f1(l):  #if we use return it is true it will return and exit
    for i in l1:
        
        return i
f1(l1)   


"8. isinstance()"
#is instance is used to check wheather the varialble belongs to the data type or not
#isinstance(obj,classinfo)

l={1:3}
isinstance(l,list)# false
isinstance(l,dict) #true


"9. map()"
#map(function, iterable, ...)
list1=[1,2,3,4]

list(map(lambda x:x**2 ,list1))


#normal method without using map
l2=[]
def f1():
    
    for i in list1:
        l2.append(i)
        #print(l2)
f1()
print(l2)


l2=[]
for i in list1:
  l2.append(i)
print(l2)


l2=[]
for i in list1:
  l2.append(i)
  print(l2)
  
""" In Python 2, the map() function retuns a list. In Python 3, however, 
the function returns a map object which is a generator object """
l1=[1,2,5,6]
list(map(lambda x:x**2 ,l1)) #normal function returns only one time in function ,after it will exit the loop,
                             #map it returns and holds ,and returns and holds
                             
def f1(x):
    return x*x

list(map(f1,l1))

s1=[1,2,3]
s2=[2,4,6]
list(map(lambda x,y:x*y ,s1,s2))


"10. reduce()"
#reduce((func, iterable[, initial]))
#reduce function applies the function to one element to another element consiquently
#it applies rolling operation on sequential unit
#to avoid for loop we used the map,filter,reduce

l=[1,2,2,5]
pro=1
for i in l:
    pro=pro*i
print(pro)    

#using reduce
#we want to import it
l=[1,2,2,5]
from functools import reduce 

reduce(lambda x,y:x*y, l) #first 1 is x and 2 is y then multiply next answer is x and next value is y that's it all working

l1=['s','a','c','h','i','n']
reduce(lambda x,y:x+y, l1)

#user defined function
"it avoids the retyping the code again and again"
"we can use this function again anad again"


def func(call):
    print('hai')
    
func('sa')

"zip"

l=[1,2,3,4,5,9]
l1=[5,6,7,8] 
l2=list(zip(l,l1))
for i in zip(l,l1): #output gives in the tuple
    print (i)
    
for i,j in zip(l,l1):
    print(i)
    
for i,j in zip(l,l1):
    print(i,j)
     

for i in zip(l,l1):
    print(i[0])
    
l3,l4=zip(*l2) #unzip

l3
l4 #outputs are in tuple

i=[1,2,3]
j=[4,5,6]
k=[7,8,9]

for i in enumerate(zip(i,j)):
    print(i)
    
for i,j in enumerate(zip(i,j,k)):
    print(i,j)
    
for i in enumerate(zip(i,j)):
    print(i[0])
    
for l,(m,n) in enumerate(zip(i,j)):
    print(l,m,n)
    
for l,(m,n,o) in enumerate(zip(i,j,k)):
    print(l,m,n,o)
        
j=8 
j.bit_length()  #1000 bit lenghth


#arbitary functions
"using *args,**kargs"
#when input is not our control we use these arbitary arguments

"""We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions."""

#*args and **kwargs make the function flexible.


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def f3(a,b):
    return a,b
f3(2,3)    

def f4(r,pi=3.14): #first we want to pass non default arguments otherwise through error
    return r*r*pi


def f5(a,b,c=10):
    return(a+b,b+c)
    
f5(a=10,4) #error positional argument follows keyword argument
f5(2,3,4)
f5(2,b=10) #no error


def add(*num ):
    print(num[0])
    
add(2,3,4,5)

def add(**num):  #it takes key value pair
    print('his name is {},last name is{}'.format(num['fname'],num['lname']))
add(fname='sachin',lname='paddu')


#**kwargs 

def intro(**data):  #it gives the dict type because key value pair
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)



def add(**num):  #it takes key value pair
    print('his name is {},last name is'.format(num))  #see the output in the dict form
add(fname='sachin',lname='paddu')





