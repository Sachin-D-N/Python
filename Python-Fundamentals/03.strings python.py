#******** ord () is used to convert alphabetic to ASCII values it takes character and gives numerical value
ord('c')  #65 to 90 Uppercase,97 to 122 lower case

chr(90) #it takes numerical & gives the character

#Doc string

"""In programming, a docstring is a string literal specified in source code 
that is used, like a comment, to document a specific segment of code."""

#String
s="sachin is stydying" # we can use double quotes
s

s='sachin is sleeping' #we also use single quotes

s[1] # ans = a It is by string slising

# "sachin is stydying"
# indexes starting from zero[0]

s=(r"sachin")
s="  sachin "
s * 3 #if we do string multiplication the cvalues are repeated
'a' +'b'  #if we adding the two strings they are concatinated
len(s) # it will gives the length of the particular string 

s=('sachin "s"') # using both quotes in a string
s=("sachin \'r") #\ used to print the both the quotes

p=("sachin ,\n sach") #print in new line
print(p)
s-p  #error we can't substract strings unsupported operand for s-p and s/p
 
import os #using line separator
q='p'+ os.linesep + 's'
print(q)

#type conversion
s=('2')
s=int(s) # it is converted from string to integer

s=bool(s) #int,float,string,bool are the four types of coversions

type(len("my_string")) #int type

s=('sachin')
s[0]='p'  #TypeError: 'str' object does not support item assignment because string is immutable


#python index slicing

"""+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1"""

q=("sachin loves you")
len(q)
q[1::] #start ,stop ,step

q[-5:-1]

q[1::2] #it is step size by 2 letters

a = [1,2,3,[1000,2000,3000,[100,200,300]],[3,4,5],(1,2,3),{1,2,3},{'a':1,'b':3}]
a[3]
a[3][3][2]
a[5][0]
a[5]
a[6][1] #set object is not subscriptable
a[7]['a'] #for dictinary slicing
a[7]['b']

l3=[1,2,3,4,5]
l3[   :  3] # if 'i' is omitted uses default '0'
l3[ 3 :   ] # if 'j' is omitted uses default 'len(s)'
l3[  :   ]

l3[  3: 20000]
l3[  3: 10 ]

l3[-200:200] 


l3
l3[2:8:1]
l3[2:8:2] #if start or step is more than a given size it will print the full value
l3[::-1]
l3[9:2:1]
l3[9:2:-1]
l3[7:4:2]
l3[7:4:-2]

# negative indexing.


l3[-3:-5:-1]
l3[-2]
l3[  :  :1]
l3[  :  :1]
l3[  :  :-1]
l3[-1:0:2]
l3[-1:0:-2]
l3[-1:-8:-2]



#string methods
#Python String capitalize()
"""In Python, the capitalize() method converts first character of a string to uppercase
 letter and lowercases all other characters, if any."""
 
 #string.capitalize()
p='sac hi kdc nns '
p.capitalize(a) #it can't takes arguments type error
s="SADFGHGV HDHDSH"
s.capitalize()

#Python String center()
""""The center() method returns a string which is padded with the specified character"""
""""string.center(width[, fillchar])
center() Parameters
The center() method takes two arguments:

width - length of the string with padded characters
fillchar (optional) - padding character
The fillchar argument is optional. If it's not provided, space is taken as default argument.

Return Value from center()
The center() method returns a string padded with specified fillchar. It doesn't modify the original string."""


string = "Python is awesome" # spaces and pad with some charcter

string.center(25,'$') #filled with $ starting and ending points

#string casehold()
"""The casefold() method is removes all case distinctions present in a string. It is used for caseless matching, i.e. ignores cases when comparing.

For example, German lowercase letter ß is equivalent to ss. However, since ß is already lowercase, lower() method does nothing to it. But, casefold() converts it to ss.

"""
sp=('DFGHJSJ HDHHJD CJFRHFHJRRJ')
sp.casefold()                      #converts in to lower case



#The casefold() method is removes all case distinctions present in a string. It is used for caseless matching,
# i.e. ignores cases when comparing.

#For example, German lowercase letter ß is equivalent to ss. However, since ß is 
#already lowercase, lower() method does nothing to it. But, casefold() converts it to ss.

s='ß'
s.casefold()


#string count
#string.count(substring, start=..., end=...)
#In simple words, count() method searches the substring in the given string 
#and returns how many times the substring is present in it.

#It also takes optional parameters start and end to specify the starting and 
#ending positions in the string respectively.

'''''String count() Parameters
#count() method only requires a single parameter for execution. However, it also has two optional parameters:

#substring - string whose count is to be found.
#start (Optional) - starting index within the string where search starts.
#end (Optional) - ending index within the string where search ends.
Note: Index in Python starts from 0, not 1.'''

string = "Python is awesome, isn't it?"
len(string)
sub='i'
string.count(sub ,0,28) # sub string, start , end


#string ends with()
#str.endswith(suffix[, start[, end]])
#endswith() Parameters
#the endswith() takes three parameters:

#suffix - String or tuple of suffixes to be checked
#start (optional) - Beginning position where suffix is to be checked within the string.
#end (optional) - Ending position where suffix is to be checked within the string


text = "Python programming is easy to learn."
text.endswith('.',0,36) # checks ends with with character ,if it is true returns true


#Python String expandtabs()
#string.expandtabs(tabsize)
#The expandtabs() takes an integer tabsize argument. The default tabsize is 8.
#The expandtabs() returns a string where all '\t' characters are replaced with whitespace 
#characters until the next multiple of tabsize parameter.

str = 'xyz\t12345\tabc'

# no argument is passed
# default tabsize is 8
result = str.expandtabs() # it will takes the tabs sizes , it will expand that ,the default tab size is 8
len(result) 
print(result)


#with expand size
str = "xyz\t12345\tabc"
print('Original String:', str)  #default tabsize is 8. The tab stops are 8, 16 and so on.

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))#ou set the tabsize to 2. The tab stops are 2, 4, 6, 8 and so on. 

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))#tabsize to 3. The tab stops are 3, 6, 9 and so on. For 'xyz', the tab stop is 6, and for '12345', 
#the tab stop is 12. Hence, there are 3 spaces after 'xyz' and 1 space after '12345'.

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))

#Python String find()
#str.find(sub[, start[, end]] )
#The find() method returns the index of first occurrence of the substring (if found). 
#If not found, it returns -1.

s=("what is the secrect of life?")
s.find('t',0,-1) #if it is in the string it will returns the index
s.find('m') #if it is not found returns -1

#rfind() 
#The rfind() method returns the highest index of the substring (if found). If not found, it returns -1.

#str.rfind(sub[, start[, end]] ) (start,end are optional)
p=('sachin sachin sachin pachin')
p.rfind('sachin')  #it will reurns highest index of the string

#Python String encode()
#The string encode() method returns encoded version of the given string.
#For efficient storage of these strings, the sequence of 
#code points are converted into set of bytes. The process is known as encoding.
#utf-8, ascii,  methods

#string.encode(encoding='UTF-8',errors='strict')

#errors (responses when encoding fails)
#there are six types of errors()

""""strict - default response which raises a UnicodeDecodeError exception on failure
ignore - ignores the unencodable unicode from the result
replace - replaces the unencodable unicode to a question mark ?
xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
backslashreplace - inserts a \uNNNN espace sequence instead of unencodable unicode
namereplace - inserts a \N{...} escape sequence instead of unencodable unicode"""
s=("dear")
s.encode() #default encoding "utf-8"
s.encode("ASCII","ignore")

#string format
#two ways positional parameters & keyword parameters
#template.format(p0, p1, ..., k0=v0, k1=v1, ...) p0,p1 are positional arguments 
#w.r.t k0,k1 are keywords arguments
#positional arguments
"hello {0},your balance is{1:9.3f}".format("sachin",230.25689) # 9 is width .3 is it will round the value to 3 digits

#keyword arguments
"hello {name},your balance is{blc:9.3f}".format(name="sachin",blc=230.25689) #name & blc are the arguments


#number formating
#(d	=Decimal integer
#c=Corresponding Unicode character
#b= Binary format
#o =	Octal format
#x =	Hexadecimal format (lower case)
#X  = Hexadecimal format (upper case)
#n =	Same as 'd'. Except it uses current locale setting for number separator
#e =	Exponential notation. (lowercase e)
#E =	Exponential notation (uppercase E)
#f =	Displays fixed point number (Default: 6)
#F =	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
#g =	General format. Rounds number to p significant digits. (Default precision: 6)
#G =	Same as 'g'. Except switches to 'E' if the number is large.
#% =	Percentage. Multiples by 100 and puts % at the end.)
                                                                
("hai ,{m:d} , {m:f}".format(m=123)) #integer and float
("hai,{0:b},{0:o},{0:x}".format(123)) #binary,octal,hexadecimal

"""""Arguments as format codes using format()
You can also pass format codes like precision, alignment, fill character as positional 
or keyword arguments dynamically.Example  Dynamic formatting using format()"""""

# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align='<', width=8, precision=2))


#string format to dictinaries
person={'name':'sachin','age':23}
("{p[name]},{p[age]}".format(p=person)) 

#bymapping method
("{name},{age}".format(**person)) 

#classes
class Person:
    age = 23
    name = "Adam"

# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))


#allign (<,>,^,=)
("{g:5},{g:^5},{g:>},{g:=6}".format(g=-456)) #when = used - or + is there it will goes to left side


#padding
("{g:-^15.3}".format(g='cattgreger')) #padding of any thing you want

#string index()
#str.index(sub[, start[, end]] )
#returns the value of the index if it is doesn't exist it will shows value error
 
s=('what can i do for you?')
s.index('1') # if it is not found shows value error 

#String isalnum(),string isalpha(),String isdecimal(), String isdigit(),String isidentifier()
#String islower(),String isnumeric(),String isprintable(),String isspace()


name="sachin 123 "

name.isalnum() #if it isnumber it will print true other wise false

name = "M0n1caG3ll3r"

if name.isalnum() == True:
   print("All characters of string (name) are alphanumeric.")
else:
    print("All characters are not alphanumeric.")
    
    
    
#name.isalpha() #it doesn't take any parameters
#if all characters of the string are alphabets then prints true otherwise false
p='sachin'
p.isalpha()

#isdecimal() #if all the characters in strings are decimal it will prints true
s=('012345')
s.isdecimal()

#isdegit()
s.isdigit() #all the characters of the string is degits then prints true 
p=('\u00B23455')
p.isdigit() #In Python, superscript and subscripts (usually written using unicode) are 
             #also considered digit characters. Hence, if the 
            # string contains these characters along with decimal characters, isdigit() returns True.

#isidentifier()# prints true when it's a valid character oterwise prints false
p.isidentifier()
s=('Py thon33')
s.isidentifier()

#islower()
#prints true when all the characters are in lowercase
s=('hhjjshjjjs122jjs')
s.islower()

#isupper() #all characters in the strings will uppercase it will prints true
p=('DFGHJ12256')
s.isupper()
p.isupper()

#isnumeric() 
"""In Python, decimal characters (like: 0, 1, 2..), digits (like: subscript, superscript), 
and characters having Unicode numeric value property (like: fraction, roman numerals, currency numerators)
 are all considered numeric characters."""
 
s=('1253@%@^@&')
s=('123')
s.isnumeric()

s=('/u09F4')

#isprintable 
"""The isprintable() methods returns True if all characters in the string are printable or
 the string is empty. If not, it returns False."""
 #letters and symbols
#digits
#punctuation
#whitespace
 
 
chr(14) #decimal to unicode converter
s='2+2=4'
s.isprintable()

chr(27)#\x1b

chr(97) #a

s=chr(27)+chr(97)
s.isprintable()

#isspace 
#if it is space it will print true otherwise print false
s='  njsj jsj'
s.isspace()
#True if all characters in the string are whitespace characters
#False if the string is empty or contains at least one non-printable() character
s=' s s  \ n s s '
s = '   \t'
print(s.isspace())

#s =stringlittle()

#The istitle() method returns:

#True if the string is a titlecased string
#False if the string is not a titlecased string or an empty string
s = 'Python Is Good.'
print(s.istitle())

s = 'Python is good' #if the title is look like string based title'
print(s.istitle())

s = 'This Is @ Symbol.'
print(s.istitle())

s = '99 Is A Number'
print(s.istitle())

s = 'PYTHON'

print(s.istitle())

#string.join(itwrable)
s='l o v e'
s.split()
''.join(s)

#he join() method provides a flexible way to concatenate string. It concatenates each element of an iterable (such as list, string and tuple) to the string and returns the concatenated string.

#The syntax of join() is:
#Native datatypes - List, Tuple, String, Dictionary and Set
#File objects and objects you define with an __iter__() or __getitem()__ method
s1 = 'abc'
s2 = '123'

print(s1.join(s2)+s2.join(s1)) 
#1abc2abc3a123b123c output

#for set
s={'1','2','3','1'}
p='.'
print(''.join(s))


test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))#Python->->Java->->Ruby output 

#for dict
test =  {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

test =  {'1':'mat', '2':'that'}
s = ', '

test={1:"sachin",2:"saachi"}
# this gives error
print(s.join(test)) #we can't join the values in the dictionaries #type error

#list
l=['x','d','e']
'love'.join(l)


#String ljust() #fill in the right
#The string ljust() method returns a left-justified string of a given minimum width.
#string.ljust(width[, fillchar])

""""The ljust() method takes two parameters:

width - width of the given string. If width is less than or equal
 to the length of the string, original string is returned.
fillchar (Optional) - character to fill the remaining space of the width"""

s='cat'
s.ljust(15,'*')# (width, fill char)

#String rjust()

#string.rjust(width[, fillchar]) #fill in the left 

'cat'.rjust(5,'-')


#string.lower
print('sAcin'.lower()) #if upper is present it converts into lower , if uppercase is not there it return as it is

#string.upper()
print('Sacgh'.upper())

#String swapcase()
"""The string swapcase() method converts all uppercase characters to lowercase and all lowercase
 characters to uppercase characters of the given string, and returns it."""
 
s='hhakjgadggAFHJJ' 
s.swapcase().swapcase() #original string

s.swapcase()


#String strip()

#string.strip([chars]) #it removes right & left side of the string
s='   dsg hsbhbj jhk     '
s.strip()


#Python String lstrip()
#string.lstrip([chars])
s='sachin'
s.lstrip('s') #it only removes left side

#Python String rstrip()
#string.rstrip([chars])
s='sachin'
s.rstrip('n') #it removes the right side

#String partition()
#string.partition(separator)

s='sachin'
s.partition('c') #separates which character we give 

#Python String maketrans()
#string.maketrans(x[, y[, z]])

dict={'s':'24','p':'23','l':'21'} #make tra
string='abc'
string.maketrans(dict)

#r partition
#string.rpartition(separator)

s='sachin'
s.rpartition('jsjn') #it also partition to the left


#String translate()
#string.translate(table)

# first string
firstString = "abc" #Here, the translation mapping translation contains the mapping 
                    #from a, b and c to g, h and i respectively.
secondString = "ghi" #But, the removal string thirdString resets the mapping to a and b to None.
thirdString = "ab"

string = "abcdef"#So, when the string is translated using translate(), a and b 
                 #are removed, and c is replaced i outputting idef.
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))

#string.replace()
#str.replace(old, new [, count])
"""The replace() method can take maximum of 3 parameters:

old - old substring you want to replace
new - new substring which would replace the old substring
count (optional) - the number of times you want to replace the old substring with the new substring"""

sp=('sachin and his his love') #replaces old string by new string
sp.replace('h','ser',0)# count 0 times ,default 2 times

'i love youyou sachin'.replace('youyou','you')

#String rindex()
"""rindex() method returns the highest index of the substring inside the string (if found). 
If the substring is not found, it raises an exception."""
#str.rindex(sub[, start[, end]] )

p='sachin is the'
p.rindex('i',0,5) #find index by start ,end

p.rindex('sss',0) #error
p.rindex('s',0,-1)

#string split

#str.split([separator [, maxsplit]])

s='he loves you  dds'
s.split()
print(s.split(', ', 2))

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 5))


#String rsplit() 
#right split
#str.rsplit([separator [, maxsplit]])
"same as split but right split"


#spring splitlines
#str.splitlines([keepends])
"""The splitlines() method splits the string at line breaks and returns a list of lines in the string."""

"""The splitlines() takes maximum of 1 parameter.

keepends (optional) - If keepends is provided and True, line breaks are also included
 in items of the list.By default, the line breaks are not included."""
 
s='sachin   vhsjs jsjjja'
s.splitlines(True)


#string starts with()

#str.startswith(prefix[, start[, end]])

text = "Python is easy to learn."

result = text.startswith('is easy')
# returns False
print(result)



#string.tittle
s='savbgn n nhhh   n  h' #it gives the title of the string
s.title()

#string.zfill()
#str.zfill(width)
s.zfill(25)


#string format_map()
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format(**point))


""""print function input output formats """
print('sachin', 'is' ,'a' 'bad boy',sep='*',end=' &') #we can use separator for the separation

print(1,2,3,4,5,end='   \n',1) #error syntax positional argument follows keyword argument


l=input('enter the value:') # takes the inputs from user


#s='sachin'

#s.replace('a','b',1) #replacing string


#formatting
#2 methods are there
""" 1  .format method()
    2. f-string(formatted string litrrsls)"""
    
print("sachin is ,{0} ,{0}".format('what','sa')) #.format by index of string

print("sachin is,{},{},{}".format('*12','*','sachin','*'))


print('{s},{l},{c}'.format(s='sachin',l='love',c='you'))


#float formating(value:width.precision of f)

print('{r:b}'.format(r=2.2255)) #widthd place is plases the space

#F-string method
name='sachin'

print(f"sachin is {'sachin'}") #we can directly pass the value in the f string method

print(f"He said his name is {name!a}") #it willl prints the in string format use !a or !r

#another method
print("I'm going to inject %s text here, and %s text here." %('some','more'))


print('He said his name was %s.' %'Fred') 
print('He said his name was %r.' %'Fred') #using %r fred comes with a string


print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)   #%d converts without rounding


print('Floating point numbers: %100.4f' %(13.144))#%,width,round


#allignments using the .format methods
print('{0:<11} | {1:>01}|{2:^10}'.format('Fruit', 'Quantity','love')) #left ,right,centre allignment
print('{0:1} | {1:1}'.format('Apples', 3.))
print('{0:1} | {1:1}'.format('Oranges', 10))



#taking the input from user
s=input()
print(s)

"multiples inputs by split method"

x,y,z=input('enter the values:').split()

# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print()


#by map #type casting using list
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x) 
