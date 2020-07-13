#Data Structures
#lists,Tuples,sets,Dictionary these are the data structures
 
"""Lists"""
#lists are ordered ,changeble, python lists are in square brackets
#it supports Indexing and slicing
#items are separated by ,
#list are mutable

l1=[1,2,3,4,'sachin']

l1[0] #indexing

l1[4][1] #to grab the string index


l1[::] #start ,stop,step size

l1[-1][::-1] # ans :'nihcas'

a = [1,2,3,[1000,2000,3000,[100,200,300]],[3,4,5],(1,2,3),{1,2,3},{'a':1,'b':3}]

a[3][3][1]

a[5][1]

a[6][0] #type error because set does,not have any order

a[7]['a'] #for dictinary we will give the key

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


thislist[0][::-1] #o th indexing reverse

thislist[-4:-1] #negative indexing

#loop through list
l1
for i in l1:
    print(i,end=',')

#len of list
l1
len(l1) #gives the length of the list

#nested list
l1=[1,2,3,[1,2,3],[4,5,6]]
l1[3][1]

#MULTIPLICATION OF LIST
l1=[1,2,3]
l1*3 #it will repeated 3 times [1, 2, 3, 1, 2, 3, 1, 2, 3]

#adding two lists called concatenation
l2=[3]
l3=[4]
l4=(3,4)
l3+l4 #error can only concatenate list (not "tuple") to list

l2+l3 #l3 will added to the last index of l2
l3+l2 #l2 will added to the last index of l3

l1
l1[0.1] ## type error ,it only allows integer for the indexing

l4=[4,5,6] 
l4[0]=1 #change the value of the index

"""""List methods"""""

#list Aappend #use list.append()
"1.Append()"

l=[1,2,3,4,5,6]
l1=l.append(0) #it will take one arguments only it will can't store this
# in append method we can add items into the list ,but it append last index of the list

l.append([4,5]) #it will add the another list [1, 2, 3, 4, 5, 6, [4, 5]]

l.append((1,1)) #[1, 2, 3, 4, 5, 6, [4, 5], (1, 1)] tuple

l.append({1,1}) #set

"2.pop()"

"""The pop() method takes a single argument (index).
The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
If the index passed to the method is not in range, it throws IndexError: pop index out of range exception."""


l=[1,2,3,4]
l.pop() ## pop retrieves the item @ 'i' and remove from list too
l.pop()  # by default i = -1 which is always the last number.
l1=l.pop() #we can store this value ,it will returns
l.pop(1) #we can remove this by indexing

"3.Insert()"

#syntax list.insert(index, element)

#index - position where an element needs to be inserted
#element - this is the element to be inserted in the list

l=[1,2,3,4,5]
l1=l.insert(1,2) #it will not returns the value ,that's why we can't store it
type(l1)
l.insert(1,[1,2]) # insert the list

"4.Extend()"
#list1.extend(list2)
#extend() method takes a single argument (a list) and adds it to the end
l1=[1,2,3] #same as concatenation we can add the tuple to the list 
l3={1,2,3}
l2=(1,2,3)
l1.extend(l3)
l4={'a':4,'b':5} #it will extends the keys only
l1.extend(l4)
l5=[1,2,[3,4]]
l1.extend(l5)

"5.Remove()"
#list.remove(element)
#The remove() method takes a single element as an argument and removes it from the list.
#If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.

p=['sachin','family','love'] #we can remove which one want to remove in the list
s=p.remove('love') #it's not returns any value, that's why we can,t store it
type(s) #none type because it has not stored any value
p.remove() #type error because we want to pass an argument


"6. Count()"
#list.count(element)
#element - element whose count is to be found.
#The count() method returns the number of occurrences of an element in a list.

l=['a','b',1,2,3,'asasa','asasa']
l.count('a')
l[6].count('a') #it gives count of particular element
l.count(l[6][0]) #it also takes the index inside the count


"7. Reverse()"
#list.reverse()
#it will reverse the given list
#it does n't returns any value , it will update the list only

s=['sachin','Lotus'] #it will reverse only given list
s.reverse() #attribute error
p=['paddu']
p.reverse(0) #error it doesn't take any arguments

"8.sort()"
#list.sort(key=..., reverse=...) 
#sorted(list, key=..., reverse=...)
"""Simplest difference between sort() and sorted() is: sort() doesn't return any 
value while, sorted() returns an iterable list."""

#By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
#reverse - If true, the sorted list is reversed (or sorted in Descending order)
#key - function that serves as a key for the sort comparison

#for ascending
d=['sachin','ram']
d.sort()
d[0].sort() #error

vowels=['a','e','i','o','u']
vowels.sort()#or sort(reverse=false)

#for descending
vowels=['a','e','i','o','u']
vowels.sort(reverse=True)

#using key
#list.sort(key=len)  
#sorted(list, key=len) for sorted 
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3),(8,1)] #it will sort with the index
                                          #here we give the index=1 because it's sorted by the index '1'
# sort list with key
random.sort(key=takeSecond) #for descending use reverse=True

# print list
print('Sorted list:', random)


#for sorted
py_list = ['e', 'a', 'u', 'o', 'i']
sorted(py_list)

"9. copy()"
#A list can be copied with = operator
#The copy() method returns a shallow copy of the list.

s=[1,2,3,4] #both memory locations are diffrent
p=s.copy()

#another way
w=[1,1,1]
z=w #id( both are same)

w[0]=4 #in this the problem is if u change one list the copied list also change

w={1,2,3}
p=w.copy() #set allows copy but tupple does't allow

#another way using slicing
lis=[1,2,3]
new=lis[:]

id(lis)
id(new)

#list constructor
l=list((1,2,3))

"10. index()"
w=[1,2,3,4]
w.index(1) #to find the index of particular element

#list construct using range
l=list(range(0,5))

"11. clear()"
#list.clear()
#clears the list

sp=[1,2,3,4]
sp.clear() #it doesn't return anything

"12. del"
thislist = ["apple", "banana", "cherry"]
del thislist[0] #it doesn't return anything ,so we can't store the value 
print(thislist) 

del thislist #delete the complete list 
#print(thislist) #name error


#List Comprehension
pow2 = [2 ** x for x in range(10)] #using for


number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)  #using if condition

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list) #nested if condition

["Even" if i%2==0 else "Odd" for i in range(10)] #both if and else


#using without list comprehension
l=[1,2,3,4,5,6,7]
for i in l:
    print(i**2)
    
l=[]
for i in range(10):
    if (i**2%2)==0:
        l.append(i)
        
' Unpacking a List'
l1=[1,2,33]
l1=list((11,22,33)) #list unpacking

a,b,c = l1
print(a,b,c)
[a,b,c]=[1,2,3]
print(a,b,c)



#List comprehension using nested lists
        
n=[[1,2,3,4],
   [5,6,7,8],
   [9,2,3,4],
   ]
s=[]
m=[]
for i in range(4):
    print(i)
    p=[]
   
    for row in n: 
        print(row)
        p.append(row[-i]) #list Transpose
    m.append(p)
print(m)
    
#using list comprehension


s="dafs hjshhj jksjs sjsjmna kjajk"
s.split()
[x for x in s.split() ]

x=[[row[i] for row in n ] for i in range(4)] #it decreses readability
   #choosing index          #choosing no of times
   
   
""""Tuple"""
       
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
"""""A tuple in Python is similar to a list. The difference between the two is that we cannot change the 
    elements of a tuple once it is assigned whereas, in a list, elements can be changed."""""
    
#creation of tuple
my_tuple = (3, 4.6, "dog")
print(my_tuple)   # Output: 3, 4.6, "dog" 

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6 
print(c)      # dog 


#creating tuple with one variable we want to use , for that
t=(3)
type(t) #it is int 

t=(1,)
type(t) #tuple

t1 = (1,2,3,'Hello World',[5])
t1
t100=(1,2)

t200=(1,)

type(t1)

#creating the tuple using paranthisis
t1 = tuple((2,3,4))
t1

t1 = tuple(1,2,3) #type error we want to use paranthisis
l2=[1,2,3]
l3=[1,4,3]
t2=tuple(l2)
t2
t3=tuple((l2,l3))
t3=tuple(  (l2,l3)  )
t3
t3=tuple(  [l2,l3]  )
t1 = (1)
t1
type(t1)

t4 = (1,2,3)
t4[0:2]
t4[0]=6 #tuple is immutable we can't change the value

t5  = 1,2,3
t5

#tuple packing ,unpacking
x=("Brian",36,"Male",True) #packing
(name,age,gender,Married)=x #unpacking
type(("Brian",36,"Male",True))

#In packing, we place value into a new tuple while in unpacking we extract those values back into variables
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
   

str1="hello world"

t8=tuple(str1) #conversion
t8

list(str1)

t9 = eval(input("enter a sequence of values: "))
type(t9) #it will converts to int

len(t8)
t8[0]

t7 = 'D', #tuple
t1=(1,2,3,(1,2))
t1[3][0] #indexes
t4=(1,2,3,(4,5,6))
t4[0][0]=3

t1 + t3 #tuple concatination
t1

t1=t1+t2
t1

t1 * 2 #tuple multiplication

a,b,c,d=t4 #un pack

l1 = ('hello','world')

'*'.join(l1)

#we can't add or remove items to the tuple ,but we can delete whole tuple 

tt=(1,2,3,4,5,6)
del tt[0] #we can't delete single value

del tt

#in tuple two methods are there

"count(),index()"
t4=(1,2,3,(4,5,6))
t4.count(1)
t4.index(1)


#We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
#iterating through tuple is faster than with list. So there is a slight performance boost.because tuple are immutable
#Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
#f you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

"sets"
#sets are un ordered 
#Every element is unique (no duplicates) and must be immutable (which cannot be changed).
#the set itself is mutable. We can add or remove items from it.
#In Python sets are written with curly brackets.


s={'sachin',1,2,3}

#we can't access to change the value from set

s[0]=1 #unindexed and un ordered shows error

#set doesn't have key value pair

#set doesn't allow dupplicate 
s={1,2,2,3,4}
s

#using set() constuctorv
set()

a=set((1,2,1,3))

#adding the elements to the set
#for singe element adding we want to use (add())
a.add(0)
a

a.add([6]) #we can't add single element of list 

#adding the multiple elements by the update() method

a={1,4,5,6}
a.update([8,9],(10,12,12))
a.update(1,8,'4') #we can't addte multiple ()eliment in lst #type error

#to remove the elements using  remove () and discrard () method
"remove()"
#removes the particular element
a
b=a.remove(10) #it doesn't returns the numbes ,so we can't store the number
a.remove() #we want to give arguments

"Discard()"
a
b=a.discard(12) # it also doesn't returns number
a.discard(12)
print(b)
#The only difference between the two is that, while using discard() if the item does not exist in the set, it remains unchanged. 
#But remove() will raise an error in such condition.
#to delete the whole list we can use clear()

"delete ()"
"it deletes the complete set"
w={1,2,3,4}
del w #it will deletes completly

"pop()"
#pop removes the element by randomly or from first index
s={1,2,3,4,5}
b=s.pop() #we can store this it will returns the value
b

a.clear() #it gives the empty set
a

#set operations
"union, intersection, difference and symmetric difference. We can do this with operators or methods."
#set union
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#Union of A and B is a set of all elements from both sets.
#Union is performed using | operator. Same can be accomplished using the method union().

A|B

#using union function
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A.union(B) 
B.union(A)

#Set Intersection
"""Intersection of A and B is a set of elements that are common in both sets.
Intersection is performed using & operator. Same can be accomplished using the method intersection()"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A&B
 
#using Intersection function
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A.intersection(B)
B.intersection(A)


#set difference
"""Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly, 
B - A is a set of element in B but not in A.Difference is performed using - operator. Same can be accomplished using the method difference()."""
#using - operator
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A-B
#using difference method
A.difference(B)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

B-A
B.difference(A)

#Set Symmetric Difference
"""Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference()"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

A^B  #for symmetric difference use ^ operator ,it will eleminates common elements in both sets ,and gives the combining of both sets

#use symmetric_difference function on A
A.symmetric_difference(B)
B.symmetric_difference(A)


#set Methods

"Method	           Description"
#add()	          Adds an element to the set
A={1,2,3,4,5}
A.add(2)

#clear()	      Removes all elements from the set
A={1,2,3,4,5,6}
A.clear()

#copy()	          Returns a copy of the set

A={1,2,3,4,5,6}

A=B #in this if change the A ,B is also modified


C=A.copy() #in this A is modified , B can't modified

#difference()	Returns the difference of two or more sets as a new set
R=A.difference(B)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

B-A
B.difference(A)

#symmetric_difference()	Returns the symmetric difference of two sets as a new set
#pop()	                Removes and returns an arbitary set element. Raise KeyError if the set is empty
#remove()	            Removes an element from the set. If the element is not a member, raise a KeyError
#discard()	            Removes an element from the set if it is a member. (Do nothing if the element is not in set)
#intersection()	        Returns the intersection of two sets as a new set
#union()	            Returns the union of sets in a new set


#difference_update()    Removes all elements of another set from this set
#result will be None
#A will be equal to A-B
#B will be unchanged

R=A.difference_update(B)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
R=B.difference_update(A)


R=A.difference_update(A) #set is becomes empty


#intersection_update()	Updates the set with the intersection of itself and another
"""This method returns None (meaning, absence of a return value). 
It only updates the set calling the intersection_update() method.

Suppose,

result = A.intersection_update(B, C)
When you run the code,

result will be None
A will be equal to the intersection of A, B and C
B remains unchanged
Cremains unchanged"""

#A.intersection_update(*other_sets) (* is used to take no of arguments)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
R=A.intersection_update(B)

#symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
"""result will be None
A will be equal to the intersection of A, B and C
B remains unchanged
Cremains unchanged"""

A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }
result = A.symmetric_difference_update(B)

#update()	Updates the set with the union of itself and others
#A.update(iterable)
#A.update(iter1, iter2, iter3)  
#Here, the elements of iterables iter1, iter2, and iter3 are added to set A.

A = {'a', 'b'}
B = {1, 2, 3}
result = A.update(B)
print('A =', A)
print('result =', result)

#isdisjoint()	Returns True if two sets have a null intersection
# sets are said to be disjoint sets if they have no common elements.
#set_a.isdisjoint(set_b)
#it will gives true or false only

A={1,2,3,4}
B={6,7,8,9}
A.isdisjoint(B)

#issubset()	Returns True if another set contains this set
#Set A is said to be the subset of set B if all elements of A are in B .
#A.issubset(B)
"""True if A is a subset of B
False if A is not a subset of B"""

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))

# Returns False
print(A.issubset(C))

# Returns True
print(C.issubset(B))
    
#issuperset()	Returns True if this set contains another set
"""#The issuperset() method returns True if a set has every elements of another 
set (passed as an argument). If not, it returns False."""

#A.issuperset(B)
#True if A is a superset of B
#False if A is not a superset of B

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

# Returns True
print(C.issuperset(B))

#membership operators
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)


"Frozen sets"
#these are the immutable sets 
#we can't add or removing the set value
"""Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. """
x=[1,2,3,4,5,6]
s=frozenset(x) #we can't add the items
s.frozenset()
frozenset({1, 2, 3, 4, 5, 6})

s.add(7) #frozen set doesn't have add error



"Dictionaries"
#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.
#no two data on same key

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


sachin={'name':'sachin','age':'23','role':'studying','goal':'love or life','like':'143'}

sachin['name'] #access value by key
sachin.get('name') #access the value by get method

#dictionaries are mutable so we can change ,the value of the dictionary

sachin['name']=['sachi']

#delete or removing value in Dictinary
#using pop()
#using popitem()
#clear()

sachin['place']='mandya' #adding the elements to the dictionary
sachin

#using pop() you can delete the particular element

sachin
a=sachin.pop('age') #we can store using pop it will returns the value

sachin.pop('143') #we can pop by key otherwise it throws error

#popitem() removes the the randomly in dictionary

b=sachin.popitem() #it will also returns and stores value

del sachin ['age'] #delete for particular element
del sachin # for delete whole dictionaries

"dictionary methods"
#Python Dictionary clear()
#to empty the dict use clear
sachin.clear()

#Python Dictionary copy()
l={1:'sachin',2:'paddu'} #to copy the original dictionary
l1=l.copy()

#Python Dictionary fromkeys()
"dictionary.fromkeys(sequence[, value])" #it also removes duplicate elements
s=[1,2,3,4,1,1,2]
dict.fromkeys(s)

dict=({1,2,3,4,5,1})

keys = {'a', 'e', 'i', 'o', 'u' } #create the dict using values
value = 'vowel'
value.split('')
vowels = dict.fromkeys(keys, value[0])
print(vowels)

#Python Dictionary get()
#dict.get(key[, value]) 

s={1:'2'}
s.get(2,0.2) # if value is not specified

#Python Dictionary items()
"dictionary.items()" #to view the items in the dictionaries
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.items())

sales.values()
sales.keys()

#Python Dictionary keys()
"""The keys() returns a view object that displays a list of all the keys.

When the dictionary is changed, the view object also reflect these changes."""
#dict.keys()

#Python Dictionary popitem()
"dict.popitem()"
#Python Dictionary setdefault()

"dict.setdefault(key[, default_value])"
#The setdefault() method returns the value of a key (if the key is in dictionary).
 #If not, it inserts key with a value to the dictionary.
person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)

#when key is not in dictionaries
person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age) 

#Python Dictionary pop()
"dictionary.pop(key[, default])"

#Python Dictionary values()
"dict.values()"

#Python Dictionary update()
"""The update() method adds element(s) to the dictionary if the key is not in the dictionary. 
If the key is in the dictionary, it updates the key with the new value."""
#dict.update([other])
#It doesn't return any value (returns None).

s={1:2, 3:4}
p={0:1}
s.update(p)

#using iterable

s={1:2, 3:4}
s.update(x=9, z=8)
s

#to get all available artributes of dict
d={}
dir(d)
l=[]
dir(l)


d={'a':2,'b':3}
for pair in d.items():
    print(pair)
    
d1={ k:v for k,v in d.items()}
d2={k+'c':v+2 for k,v in d.items( )}

squares = {}
for x in range(6):
   squares[x] = x*x
   
#cmp() copares two dictionaries
   
s={'k':1,'j':2}
p={2:2}


"""Hash Table"""
#the keys are processed to produce a new index that maps to the required element. This process is called hashing.

#it used to store key value items

#compound data structures

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

elements['helium'].values()


""""
Data Structure	Ordered	Mutable	Constructor	Example
List	Yes	     Yes	[ ] or list()	[5.7, 4, 'yes', 5.7]
Tuple	Yes	      No	( ) or tuple()	(5.7, 4, 'yes', 5.7)
Set	      No	Yes	{}* or set()	{5.7, 4, 'yes'}
Dictionary	No	No**	{ } or dict()	{'Jun': 75, 'Jul': 89}
* You can use curly braces to define a set like this: {1, 2, 3}. However, if you leave the curly braces empty like this: {} Python will instead create an empty dictionary. So to create an empty set, use set().
** A dictionary itself is mutable, but each of its individual keys must be immutable."""


d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)


from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d = defaultdict(set)


#ordering dict
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
   print(key, d[key])
   
   
#sorting dict
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}


prices_sorted = sorted(zip(prices.values(), prices.keys()))
   