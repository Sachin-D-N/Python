#controlflow statements
#Conditional Statements
#Boolean Expressions
#For and While Loops
##Zip and Enumerate
#List Comprehensions

"The if…elif…else statement is used in Python for decision making."

#if test expression:
#    statement(s)
"""Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b"""

x=[1,2,3,4,5,6,7,8]
for i in x:
    if i%2==0:
       print (i)
    else: 
        print(i)
        
        
x=[1,2,3,4,5,6,7,8]
for i in x:
    if i%2==0:
       print ('even ',i)
    elif i%3==0:
        print('three',i)
    else:
       print('odd',2)
       
       
x=list(range(9))
count=0;
for i in x:
    if i==0:
        print(i)
        for i in x:
            if i==1:
                print(i)
                if i==2:
                    print(i)
                    count=count+1
                    
                    
a = 331
b = 330
print("A") if a > b else print("=") if a == b else print("B")
 

                   
x = 5

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
else:
    print("but not above 20.")




a = 33
b = 200

if b > a:
  pass 

#Complex Boolean Expressions
weight=23;
height=1;
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")
    

# Don't use True or False as conditions
if True:
    print("This indented code will always get run.")

is_cold=1;
if is_cold or not is_cold:
    print("This indented code will always get run.")
    

#Be careful writing expressions that use logical operators
""""Logical operators and, or and not have specific meanings that aren't quite the same as their meanings in plain English. 
Make sure your boolean expressions are being evaluated the way you expect them to."""

#Don't compare a boolean variable with == True or == False
#Truth Value Testing

#Here are most of the built-in objects that are considered False in Python:

"""constants defined to be false: None and False
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '"", (), [], {}, set(), range(0)"""


i=0.0
if i==True:
    print('j')
else:
    print(i)
    
    
#for loops
"""Python has two kinds of loops - for loops and while loops. A for loop is used to "iterate", or do something repeatedly, over an iterable.
An iterable is an object that can return one of its elements at a time. This can include sequence types, such as strings, lists, and tuples, 
as well as non-sequence types, such as dictionaries and files."""

count=0;
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
    count=count+1;
print("Done!")
print(count)


#steps


"""The first line of the loop starts with the for keyword, which signals that this is a for loop
Following that is city in cities, indicating city is the iteration variable, and cities is the iterable being looped over. In the first iteration of the loop, city gets the value of the first element in cities, which is “new york city”.
The for loop heading line always ends with a colon :
Following the for loop heading is an indented block of code, the body of the loop, to be executed in each iteration of this loop. There is only one line in the body of this loop - print(city).
After the body of the loop has executed, we don't move on to the next line yet; we go back to the for heading line, where the iteration variable takes the value of the next element of the iterable. In the second iteration of the loop above, city takes the value of the next element in cities, which is "mountain view".
This process repeats until the loop has iterated through all the elements of the iterable. Then, we move on to the line that follows the body of the loop - in this case, print("Done!"). We can tell what the next line after the body of the loop is because it is unindented. Here is another reason why 
paying attention to your indentation is very important in Python!"""



#using range() in for loop

for i in range(0,4):
    print(i)
    
#range(start=0, stop, step=1)
    
    
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city)
    
#or
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
    
    
#Modifing the list using len() and range function
#We can use the range() function to generate the indices for each value in the cities list
#This lets us access the elements of the list with cities[index] so that we can modify the values in the cities list in place.

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    print(index)
    cities[index] = cities[index].title()
    print(cities[index]) 
    
for i in range(1,31):
    if (i%5==0):
        print(i)
        
for i in range(5, 35, 5):
    print(i)
    
#line = line.replace(';', ':')
    
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for name in names:
    username = name.lower()
    username = username.replace("" , "*") #replace ,replace by
    usernames.append(username)
print(usernames)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")
    print(name)
print(names)




tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here

for i in range(len(tokens)):
    if tokens[i][0] == '<' and tokens[i][-1] == '>':
        count += 1
    else:
        count += 0 
print(count)


#building dictionaries using for loops

#Method 1: Using a for loop to create a set of counters
book=['sachin','family','father','mother','sister','sachin']
boook={}
for i in book:
    if i not in boook:
        boook[i]=1;
    else:
        boook[i] +=1;
boook


book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
        
#using get method()
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0)+1   
    


"Iterating Through Dictionaries with For Loops"

life={'sachin':0,'paddu':1,'sisters':2,'sisterp':3}
for keys in life:
    print(keys)
  
life={'sachin':0,'paddu':1,'sisters':2,'sisterp':3}
for keys,values in life.items():
    print(keys,values)
    

result=0;    
life={'sachin':0,'paddu':1,'sisters':2,'sisterp':3}
love={'sachin','paddu'}
for i, j in life.items():
    for z in love:
        if i==z:
            print(i)
            

#else in for loop
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")      
    
    
"while loops"
#The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
#For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. 
#This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, 

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())
hand


"""while heading line, and the condition is evaluated again. 
This process of checking the condition and then executing the loop repeats until the condition becomes false."""


#Find the factorial of a number using a while loop.

#A factorial of a whole number is that number multiplied by every whole number between itself and 
#1. For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.

number=5;

product=1;

num=1

while num<=number:
    product=num*product #while loop break when the condition becomes false
    num=num+1
    print(product)
print(product)


#using for loop
a=6
pro=1
for i in range(1,a+1):
    pro=pro*i
print(pro)

number=5
num=1
pro=1
while number>num:
    pro=pro*number
    print(pro)
    number=number-1

number=5
num=1
pro=1
while num<=number: 
    pro=pro*num
    print(pro)
    num=num+1
    
    
number=1
num=1;
count=0
while number<10:
    num=num*num
    print(num)
    number=number+1
    count=count+1
print(count)
    
    
#** for** loops are ideal when the ** number of iterations is known or finite**.

"""When you have an iterable collection (list, string, set, tuple, dictionary)
for name in names:
When you want to iterate through a loop for a definite number of times, using range()
for i in range(5):"""

#** while** loops are ideal when the ** iterations need to continue until a condition is met**.

"""Examples:

When you want to use comparison operators
while count <= 100:
When you want to loop based on receiving specific user input.
while user_input == 'y':"""


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
count_even=0
l2=[]
l3=[]
l4=[]
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd <15) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        l2.append(num_list[i])
        list_sum += num_list[i]
        l3.append(list_sum)
        count_odd += 1
    else:
        print(num_list[i])
        l4.append(num_list[i])
        count_even+=1
    i += 1
else:
    print(i)
print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The numbers of even numbers added are: {}".format(count_even))
print ("The sum of the odd numbers added is: {}".format(list_sum))
l3
l4
l2

#break and continue
"In Python, break and continue statements can alter the flow of a normal loop."
#Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the break and continue keywords, which can be used in both for and while loops.

#break terminates a loop
#continue skips one iteration of a loop

#example

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))



# Use of break statement inside loop

for val in "saching":
    if val == "i":
        break
    print(val)

print("The end")

"""n this program, we iterate through the "string" sequence. We check if the letter is "i", upon which we break from the loop. Hence, we see in our output that all the letters up till "i" gets printed.
 After that, the loop terminates."""
 
 
 #continue
 #The continue statement is used to skip the rest of the code inside a loop for the current iteration only. 
 #Loop does not terminate but continues on with the next iteration.
 
for val in "saching":
    if val == "i":
        continue
    print(val)

print("The end")
 

for i in range(1,10):
    if (i%2==0):
        continue
    else:
        print("odd",i)
        
#example break        
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
        
        
        
#pass
"""In Python programming, pass is a null statement. 
The difference between a comment and pass statement in Python is that.
 while the interpreter ignores a comment entirely, pass is not ignored."""
 
 #nothing happens when pass is executed. It results into no operation (NOP).
#we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would complain. So, we use the pass statement to construct a body that does nothing.
sp=('143')
for i in sp:
    pass




#we can use this for class also
class sachin:
    pass


"Program for prime number"

check_prime = [26, 39, 51, 53]# 57, 79, 85]
# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num-1:    
            print("{} IS a prime number".format(num))
            


"****Zip and Enumerate*******"            
#Zip function

#zip(*iterables)

#iterables	can be built-in iterables (like: list, string, dict), or user-defined iterables            
            
            
"""The zip() function returns an iterator of tuples based on the iterable objects.

If we do not pass any parameter, zip() returns an empty iterator
If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables."""

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
            
#In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

#zip sing Dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

#Unzip Tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)

#Transpose with Zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

#Enumerate
"""enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.
 You'll often use this when you want the index along with each element of an iterable in a loop."""
 
 
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
 
    
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])
    print(i,cast[i])


cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
cast = (zip(cast_names, cast_heights))
for i,cast in enumerate(cast):
    print(i,cast)
    

 
