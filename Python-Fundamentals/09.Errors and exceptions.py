#errors
#syntax is error is caused by not following by proper structure

for i in x#invalid syntax

1/0 #zero devision error because integer division by zero

open('test.txt') #file not found error
open('example.txt')

dir(__builtins__) #list of errors

#some important error in python
"""
Exception            Cause of Error

AssertionError	     Raised when assert statement fails.
AttributeError	     Raised when attribute assignment or reference fails.
EOFError	         Raised when the input() functions hits end-of-file condition.
FloatingPointError	 Raised when a floating point operation fails.
GeneratorExit	     Raise when a generator's close() method is called.
ImportError	         Raised when the imported module is not found.
IndexError	         Raised when index of a sequence is out of range.
KeyError	         Raised when a key is not found in a dictionary.
KeyboardInterrupt	 Raised when the user hits interrupt key (Ctrl+c or delete). 
MemoryError	         Raised when an operation runs out of memory.
NameError	         Raised when a variable is not found in local or global scope.
NotImplementedError	 Raised by abstract methods.
OSError	             Raised when system operation causes system related error.
OverflowError	     Raised when result of an arithmetic operation is too large to be represented.
ReferenceError	     Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError	     Raised when an error does not fall under any other category.
StopIteration	     Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError	         Raised by parser when syntax error is encountered.
IndentationError	 Raised when there is incorrect indentation.
TabError	         Raised when indentation consists of inconsistent tabs and spaces.
SystemError	         Raised when interpreter detects internal error.
SystemExit	         Raised by sys.exit() function.
TypeError	         Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError	 Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	     Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	 Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	 Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
ValueError	         Raised when a function gets argument of correct type but improper value.
ZeroDivisionError	 Raised when second operand of division or modulo operation is zero."""


#exception handling

"""We can handle these built-in and user-defined exceptions in Python using try, except and finally statements. """


#Python program using try, except and finally statements.
lst=['b',0,2]
for entry in lst:
    r=(1/int(entry))#value error
    

lst=['s',0,2]
import sys             
for entry in lst:
    try:                   #try block
        print('entry is ',entry)
        r=(1/int(entry))#value erro
    except:           #exception block
        print(sys.exc_info()[0])
        print('next entry')
        print('****************')
print('entry is ',r)



lst=['s',0,2]
import sys             
for entry in lst:
    try:                   #try block
        print('entry is ',entry)
        r=(1/(entry))#value erro
    except(ValueError):           #exception block
        print('this is value error')
    except(ZeroDivisionError):
        print('this is zero devision error')
    except:
        print('some other error')
print('entry is ',r)

#finally
#finally block runs always
try:
    x=int(input('enter the value'))
    y=2/x
except:
    print('error',sys.exc_info()[0])#prints the which error we having
    x=int(input('enter correct'))
finally:
    print('bye')
    
    
#Raising Exceptions
raise KeyboardInterrupt
Traceback (most recent call last):

KeyboardInterrupt

raise MemoryError("This is an argument")
Traceback (most recent call last):
...
MemoryError: This is an argument

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
   

class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")


#debugger
import pdb
seq=5
for i in seq:
    print(i)
    
    
    
