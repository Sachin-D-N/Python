# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:00:02 2020

@author: Dell
"""
#Python Fundamentals

'''To know the system version'''
import sys
sys.version # attribute. ans '3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]'


"""It gives the directory of the my software"""
import os
os.getcwd()  # method.

#to change the directory
os.chdir('C:/Users/Dell/Desktop/Python programs')

#to know the keywords in python
import keyword;
print(keyword.kwlist)  # total keywords in the python
#output
"""['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', \ 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', \ 
'except', 'finally', 'for', 'from', 'global', 'if', 'import', \
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', \
'return', 'try', 'while', 'with', 'yield'] """
 
   

'''Identifiers''' #Identifiers are the name to entities like class ,function ,variables in python

abc_c=12;   # right form

1abc=12    #invalid syntax can't starts with number 

''' *** keywords cannot be used as identifier's'''
 
 # lambda=1; SyntaxError: invalid syntax


# we can't use the specials symbols as identifiers
 
# Indentation error
# if we miss the spaces in a Block it gives a indentation error
 
for i in range(5):
print(i)          #expected an indented block

# single line statement 
 
a=1;

# multi line statement
 """ for multiline statement we use \ """
 b=1+2+3+4 +\
   6+7+8+9 \
   # output Out[17]: 40
   
# otherwise we can also use ()
a=(1+2+3+
   6+7+8+9+
   10)

# multi statements in single line using ;
a=10; b=20; c=30

# variable assignments
 
a=10 ;
b=1.5;
c="sachin";

# multi assignments

a,b,c = 10,20,"sachin";


# storage locations 

x =7 ; y=7
print (id(x))  # If x and y values are same it will store at the same memory location
print(id(y))

x="ab" ; y="b"
print (id(x)) # If x and y values are different it will store separate location
print(id(y))

# to get the type of variale use type()
a=5;
print(type(a))  #<class 'int'>

x=1+2j;
print(type(x)) # <class 'complex'>

# isinstance method to find the  datatype
print(isinstance (2 , int)) #True

#Boolean type
a = True;
print(type(a))  #<class 'bool'>


#stings 
# strings are the sequence of unicode characters
"""Unicode. Unicode is a universal character encoding standard. \ 
  It defines the way individual characters are represented in text files, \
  web pages, and other types of documents. ... While ASCII only uses one byte \
  to represent each character, \Unicode supports up to 4 bytes for each character """
  
#''' or """ used to multi line strings
  
  a=''' sachin
  @ 143 '''
  
# string indexing 
# In python sting index always start from zero
  
  s='sachin loves his family';
  s[-1]   #string indexing
print(s[len(s)-1]) #another method of string indexing

#string slicing
#s(start:stop :step)

s[:5] # it will slice from starting point to fifth character


#array
# it's have several functions 
#list = it will in the form of array with in the square bracket
#key features of the list
#it's ordered sequence of elements 
#strings are mutable (mutable means we can change or modify  the data types)

l1=[2,3,4]
l1[0]=3 # output updated with [3, 3, 4]

#in a list we can have multiple datatypes 

l1=[1,'sachin', 0.5] 
list=[1,2,3]

#list constructor 
l1=list((1,2,3)) #output=[1, 2, 3]

#error because it () not support for item assignment
list[0]=2

# it can be done by 
l1[0]=2;


#Tupple
# It as ordered sequence but it is immutable
# It comes with curly () brackets 
#we can't add items to the tuple

t1=(1,2,3)

t1[0]=3 #error 'tuple' object does not support item assignment

t1=(1,'sachin',2)
#Tuple constructor 
tuple((1,2,3)) 

#set
#we use the {} brackets for set
#set is unordered collection of elements 
#sets are unique values

s={1,2,3,1} #out {1, 2, 3} only one time 1 is printed because it is unique
s[0]  #set is does't have any order #set' object is not subscriptable


#Python Dectinaries
#unordered collection of Key value pair

d={'key':'apple'}  
d.values()

#conversion of data types
float(5)

int(5.555)

str('10')

int('10p')  #ValueError: 

#converting list into set
list1=[1,2,3,4]
s=set(list1)
type(list1)
type(s)
list("Hello")


#Standard input and Standard outputs
# .format method

a=2
b=4;

print("the value is a is {} the value of b is {}".format(a,b))

print("the value is a is {a} the value of b is {b}".format(a=8,b=8))

#F - string method 

print(f"hello ,{'name'}, {'10'}")

#python input
h=input('enter the number')

#operators 
#Airthmatic operators
#comparision (relational ) operators
#logical operators(boolean operators)
#bitwise operators
#Assignment operators
#Special operators

#Airthmatic operators
2 + 3 #(2,3 are operands , + is operator )
x=-15
y=2
x+y; #addittion
x-y; #Substraction
x*y; #Multiplication
x/y; #Devision
x//y; #Floor (THe closed integer will printed)
#(if the values are negative it will takes the closed value to that negative value -7.5 closed value is 8)
x%y; #modulo (The remainder will be printed)
x**y #exponent (x pow y)


#comparision operators (these operators are used to compare the values)
x =2;
y=5;

x>y; #checks the if x is greter than y if true it will print true otherwise print False
x<y; #checks the if x is lesser than y 
x=y; #checks the if x is equal than y 
x!=y; #checks the if x is not equal than y 
x<=y; #checks the if x is less than equal to  y 
x>=y #checks the if x is greter than or equal toy 


#logical operators
#and, or , not are the logical operators
a=1; b=0
(a and b);
(a or b)
(not a)

a=2&2

#bitwise operators
#Bitwise or,bitwise and ,bitwise xor , bitwise right shift , bitwise lefe shift
a=15; #it is converted in to binary 1111
b=9; #                      binary 1001
print(a&b)
print(a|b)
print(~a) # in this it will returns -(x+1) or (2's complement of a)
print(a^b) # Sets each bit to 1 if only one of two bits is 1
print (b<<2)# left shift is Gaining of two zero  bits in the right side or left operands value is moved left by the number of bits specified by the right operand. 
print(b>>3);# right shift is the lossing of 3 starting bits in right side The left operands value is moved right by the number of bits specified by the right operand.
print(a>>4)

#Assignment operators
a=15;
#Substract and
a-=10; #15-10=5
#addition and
a+=5; #5+5=10
#multiplication and
a*=5; #10*5=50
#devision and
a/=5; #50/5=10
#modulus and
a%=5; #10%5=0
#floor devision and
a//=10; #15//10=1

"""special operators"""
#Python Identity operators
"""Is ,is not """
a=10;
b=5;
# to find the memory location
#(-5,256 have numbers have same memory location otherwise different memory location)
a=10
b=10
id(a)
id(b)

c=257
d=257
id(c)
id(d)

d=c #when we using this it will be same
id(c)
id(d)


print(a is b); # a is not equal to b ,false
print(a is not b) # true
s1=[1,2,3]
s2=[1,2,3]
print(s1 is s2) # false because list ,tuple, dectionaries, set objects stores in different memory location
"""Python membership operators"""
"""x in y , x not in y"""
a=[2,2,1]
b=2;
print(b in a) # weather the values in a prints true otherwise prints false
print(2 not in a)
dicty={"name":2}
print("name"in dicty) # in dictionaries it will print true only value in the key , it will not consider the value
dicty.values() # it will show the values in the dictionary
dicty.keys() # it will show the keys in the dictionary

"""contro flow statements"""
""" In python 0, None, False consider as False , and everything consider as true"""
#The if…elif…else statement is used in Python for decision making
#syntax
"""if test expression:

    statement(s)"""
#ex: 
num = 10

# try 0, -1 and None
if num > 10:
    print("Number is positive")
print("This will print always")      #This print statement always print

#If else
"""if ... else Statement
Syntax:
if test expression:

    Body of if

else: 

    Body of else """
 #example
num = 10
if num > 0:
    print("Positive number")
else:
    print("Negative Number")
    
#if ,elif , else statement
""" Syntax:
if test expression:

    Body of if
elif test expression:

    Body of elif
else: 

    Body of else """
    
#example
num = 10.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("ZERO")
else:
    print("Negative Number")
    
#Nested if Statements¶
#We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming.
num = 10.5

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative Number")
    
#while loop
    #we can run something over again and again
"""The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

Syntax:
while test_expression:

    Body of while
    
The body of the loop is entered only if the test_expression evaluates to True.

After one iteration, the test expression is checked again.

This process continues until the test_expression evaluates to False."""

#example
#Find product of all numbers present in a list

lst = [10, 20, 30, 40, 60]

product = 1
index = 0

while index < len(lst):
    product *= lst[index]
    index += 1

print("Product is: {}".format(product))

#For loop
#The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.

#Iterating over a sequence is called traversal.

"""Syntax:
for element in sequence :

    Body of for """
   # Here, element is the variable that takes the value of the item inside the sequence on each iteration.

    #Loop continues until we reach the last item in the sequence.
#example
   #Find product of all numbers present in a list

lst = [10, 20, 30, 40, 50]

product = 1
#iterating over the list
for ele in lst:
    product *= ele

print("Product is: {}".format(product))


#range function in for loop
#We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

#We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.

#This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.
#print range of 10
for i in range(10):
    print(i)
#print range of numbers from 1 to 20 with step size of 2
for i in range(1, 20, 2):
    print(i)
    
"""Break and Continue """ 
#Break 
"""Loops iterate over a block of code until test expression is false, but sometimes we wish to terminate the current iteration or 
even the whole loop without cheking test expression."""

#Python break Statement
#Syntax:

break

#Example

numbers = [1, 2, 3, 4]
for num in numbers:          #iterating over list
    if num == 4:
        break
    print(num)
else:
    print("in the else-block")
print("Outside of for loop")


#continue
#Python Continue Statement
#syntax:

continue

#Example
#print odd numbers present in a list
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
else:
    print("else-block")
