#methods

# using reduce to compute sum of list 
#python code to demonstrate summation  
# using reduce() and accumulate() 
  

  
# importing functools for reduce() 
lis=[1,2,3,4,5]
import functools 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 
  

""""Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. 
But there are differences in the implementation aspects in both of these.

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value. 
Whereas, accumulate() returns a list containing the intermediate results. 
The last number of the list returned is summation value of the list."""
 
# importing itertools for accumulate() 
import itertools
 #priting summation using accumulate() 
print ("The summation of list using accumulate is :",end="") 
print (list(itertools.accumulate(lis,lambda x,y : x+y))) 
 

"""Eval in python"""
#eval(expression, globals=None, locals=None)
#expression: this string is parsed and evaluated as a Python expression
#globals (optional): a dictionary to specify the available global methods and variables.
#locals (optional): another dictionary to specify the available local methods and variables.
x=1
y=2

z=eval('x+y') # in this we use the expression
type(z)

import struct
struct.pack('i', 2) #gives the structure

struct.unpack('s','11')



import calendar 
  
# using calender to print calendar of year 
# prints calendar of 2012 
print ("The calender of year 2012 is : ") 
print (calendar.calendar(2012,2,1,6)) 
  
#using firstweekday() to print starting day number 
print ("The starting day number in calendar is : ",end="") 
print (calendar.firstweekday()) 
