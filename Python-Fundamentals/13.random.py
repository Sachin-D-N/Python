
#import math
#import sys 
#from math import pi
#from math import * {for all imports}


#random number
import random
random.randrange(0,10)

# find the random range
import random
#random list
random = ['a', ('a', 'b'), [3, 4]]
# index of ('a', 'b')
index = random.index(('a', 'b'))
print("The index of ('a', 'b'):", index)
# index of [3, 4]
index = random.index([3, 4])
print("The index of [3, 4]:", index)

#random.seed()
#random.seed(a, version)

import random
random.seed() 


random.seed(3)
random.random() #The random() method returns a random floating number between 0 and 1.

print(random.random())
state=random.getstate()
print(random.random())  #it weill get the random and set same random to next step
random.setstate(state)


#rand range
random.randrange(1,20,1) #gives the random integer number b/w given range

#rand int
print(random.randint(3, 9))

#rand.choice
"""The choice() method returns a randomly selected element from the specified sequence.
The sequence can be a string, a range, a list, a tuple or any other kind of sequence."""  


x = "WELCOME"

print(random.choice(x))

#rand.suffle
#random.shuffle(sequence, function)
l=['1','2','3']
random.shuffle(l)
l

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
mylist


#random sample()
#The sample() method returns a list with a randomly selection of a specified number of items from a sequnce.

mylist = ["apple", "banana", "cherry"]

print(random.sample(mylist, k=2)) #k=size


#random.uniform(a, b)
print(random.uniform(20, 60)) #print the random floating number b/w specified value

#random.triangular()
#random.triangular(low, high, mode)
print(random.triangular(20, 60, 30)) #mode=high or low direction







#to suffle the keys in random
import random

# Output: 16
print(random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())
