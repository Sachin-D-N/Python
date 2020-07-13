"""Classes"""

"""Classes and Objects. Object − Objects have states and behaviors. 
Example: A dog has states - color, name, breed as well as behaviors – wagging the tail, barking, eating.
 An object is an instance of a class."""
 
"""Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects."""

#object have two parameters
"""attributes
behavior"""

#example
"""Parrot is an object,

name, age, color are attributes
singing, dancing are behavior"""


"""The concept of OOP in Python focuses on creating reusable code. 
This concept is also known as DRY (Don't Repeat Yourself)."""

""" Object is simply a collection of data (variables) and methods (functions) that act on those data.
 And, class is a blueprint for the object.""" 
 
class MyClass:
  x = 5

print(MyClass)

#self is a method that is used to connect to the class

#function in oops called methods

"class is a design or blueprint for object"
"object is a instance of class"

class sachin:
    def love(self):
         print('sachin')
        
sac=sachin() #creating object
sac.love()
#sachin.love(sac)  it will work like this 
sac1=sachin()
sac1.love()

#init
class sachin:
    def __init__(self):
         print('love')
        
    def love(self):
          print('sachin')

sac=sachin() #when we use init we don't want to call init method it will automatically call itself
sac.love()
sac1=sachin()


class comp:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print(cpu)
        print(ram)
        

comp1=comp('sachin','14.5')



class comp:
    def lap(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print(cpu)
        print(ram)
        print('143')
        

lap1=comp()
lap1.lap('12',143)


class comp:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print(cpu)
        print(ram)
    def sac(self):
        print(self.cpu)

lap2=comp('12','14')
lap2.sac()


"constructor"
#all the global variables are stored in heap memory
#every time we created object it will takes new space
class sp:
    pass

ps=sp()
id(ps)
ssp=sp()
id(ssp)  #different adresses


"self"
#self is reffering to the object
#it connect methods to the class
"""The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, 
but it has to be the first parameter of any function in the class:"""


"comparing" 

#syntax
"compare(who is calling ,whom to compare)" #it is not a inbuilt method we want to create it

class people:
    def __init__(self):
        self.name=12
        self.age=23
        
    def compare(self,other):
        if self.name==other.name:
            return True
        else:
            return False
            
p=people()    
print(p.name)        #we can also change outside this is the advantage of class over functions

p1=people()
p1.name=25   

if p.compare(p1):
    print('they are same')
else:
    print('they are different')

p1.compare(p)


"variables"
#2 types
"1. Instance variables"
"2.static variables/class variables"

#Instance variables
"we can change the value of the variables"

class car:
    def __init__(self):
        self.name=5
        
c=car()
c.name #5
c.name=20 #we can change here


#static variables

class car:
    wheels=10 #class variables
    def __init__(self):
        self.name=5
    def a1(self,name):
        self.name=6
        print(self.name)

c=car()
print(c.name,c.wheels)
print(c.name,c.wheels)

car.wheels=15 #we can change using the class name for class variables

c.a1(5)


"types of methods"
#3 types
"1. instance methods"
"2. static methods"
"3. class methods"

#Instance Methods
"1. Accessor Methods(Getters)"
"2. Mutator Methods(setters)" #used to modify the variables

#aceessor Methods
"used to fetch the value"

class car:
    wheels=10 #class variables
    def __init__(self):
        self.name=5
    def a1(self,name):
        self.name=6
        print(self.name)
    def get_ml(self):  #getters
        return self.name
    def set_ml(self,value): #setters
        self.name=value
c=car()
c.get_ml()

c.name #accessors /getters

c.name=6 #setters/mutators


#class methods
"we are working with class methods"
class school:
    name='sachin'
    @classmethod #we use the class method
    def sp143(cls):#we used cls method
        return cls.name
    
    
s=school()
s.sp143()

#static methods
#we can work with nothing
"we want to use static"

class school:
    name='sachin'
    @staticmethod #we use the class method
    def sp143():#we used cls method
        return ('hai i love you')
s=school()
s.sp143()


"class inside a class"
#you can create object of inner class inside the outer class 
"or"
#outside the outer class provided you use outer class name to call it

class Mandya:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.mal=self.malavalli() #we want to call the class
        
    class malavalli:
        def __init__(self):
            self.name='sachin'
            self.age=23
            
m=Mandya('paddu',2)
m.name
m.age    

m.mal.name
m.mal.age   
#               "or"

class Mandya:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    class malavalli:
        def __init__(self):
            self.name='sachin'
            self.age=23
            
m1=Mandya.malavalli()
m1.name
m1.age            

m=Mandya('paddu',2)
m.name
m.age  

#delete
class ate:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
a=ate('sachin','paddu')
a.name
a.age

del a.age
del a


"OOPS Concept" #Object Oriented Programming

#Inheritance  	:A process of using details from a new class without modifying existing class.
#Polymorphism	:A concept of using common operation in different ways for different data input.one name many forms
#Abstraction    :Abstraction means hiding the complexity and only showing the essential features of the object
#Encapsulation	:Hiding the private details of a class from other objects.

"1.Inheritance"
#Relation between the two objects
#The child class inherited from the parent class
#using the exising feature of the class in another class

class DBN:
    def Nagaraju(self,name): #super class or Parent class
        self.name=name
        print(name)
        
    def Devajamma(self,name):
        self.name=name        #"single level Inheritance"
        print(name)
        
DB=DBN()
DB.Nagaraju('Nagaraju')

DB.Devajamma('devajamma')
        
class Sachin(): #mention in the bracket sub class or Child Class Sachin is sub class of DBN
    def Sachi(self,name): #DBN is super class of Sachin
        self.name=name
        print(name)
        
Sa=Sachin()            #we can use all the features of the class DBN
Sa.Sachi('sach')
Sa.Nagaraju('12')
Sa.Devajamma('devja')


class sahana(Sachin):
    def sahana(self,name):  #multi level inheritance
        self.name=name
        print(name)


sah=sahana()
sah.sahana('143')
sah.Sachi('143')

class sahana(DBN,Sachin):
    def sahana(self,name):  #multi level inheritance
        self.name=name
        print(name)

sah=sahana()
sah.Nagaraju('1')  #Multi level inheritance
sah.sahana(2)
  
#"sahana" is subclass of "DBN" &'sachin'

"contructor in inheritance"
class a():
    def __init__(self):
        print('hai')
    def sp(self):
        print('in love')
A=a()       
  #if there is an init present in b it will call the b init, 
  #if there is no init in b then it will call the init of a
class b(a):
    def __init__(self):
        print('hello')
    def ps(self):
        print(ate)
A=b()


#using super call the init of a also
class c:
    def __init__(self):
        print('sachin loves you')
a=c()
        
class D(c):
    def __init__(self):  
        super().__init__()  #using super call the c's init method first it will call the c then it will call d's init. 
        print('paddu not speak to you')
        
a=D()

#method resolution order(MRO)
"""if there is two super class is there then we call the super to call init first it will ,
go to sub class to call init and next it will executes left to right of the super class mention in the sub class
is the Method resolution order"""

class s:
    def __init__(self):
        print('p')
    def hai(self):
        print('both')
class p():
    def __init__(self):
        print('s')
    def hal(self):
        print('are ')
        
class sp(p,s): #method resolution order call the first of the left to right only
    def __init__(self):
        super().__init__()
        print('sp')

a=sp()
a.hal()

#for methods also (using MRO)
class s:
    def __init__(self):
        print('p')
    def hai(self):
        print('both')
class p():
    def __init__(self):
        print('s')
    def hai(self):
        print('are ')
        
class sp(s,p): #method resolution order call the first of the left to right only
    def __init__(self):
        super().__init__()
        print('sp')
    def ps(self):
        super().hai() #we can also call method by super
        
c=sp()
c.hai()
c.ps()


"PolyMorphism"

#one thing Many forms
#4 ways to do the Polymorphism
"1.Duck typing"
"2.Operator overloading"
"3. Method Overloading" #overloading means same class different method
"4.Method overriding" #overriding means same method in different class

#Duck typing
"looking like a duck ,flying like a duck ,swiming like a duck is should be duck"
"so object is loking like other method it shoud be that method we don't consider class"

class family():
    def sac(self):
        print('my family loves you')
class fullfami():
    def sac(self):
        print('my family likes you')
class love():
    def marry(self,home):
        home.sac() #we don't consider class but we consider sac 
      

home=fullfami()

l=love()
l.marry(home)

home=family()
l.marry(home)

#operator overloading
"when we call the addittion ,substraction,operators overload the methods behind the seen"



"""Operator	     Expression	Internally
Addition	     p1 + p2	p1.__add__(p2)
Subtraction	     p1 - p2	p1.__sub__(p2)
Multiplication	 p1 * p2	p1.__mul__(p2)
Power	        p1 ** p2	p1.__pow__(p2)
Division	     p1 / p2	p1.__truediv__(p2)
Floor Division	 p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2	p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
Bitwise AND	     p1 & p2	p1.__and__(p2)
Bitwise OR	     p1 | p2	p1.__or__(p2)
Bitwise XOR	     p1 ^ p2	p1.__xor__(p2)
Bitwise NOT	         ~p1	p1.__invert__()"""

a=5
b=10

a+b

#behind the scene(magic methods happen)
int.__add__(a,b)


class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def __add__(self1,other):
        m1=self1.m1-other.m1   #use the operator over loading
        m2=self1.m2-other.m2
       
        
        s3=student(m1,m2)
        print(s3)
        
        return s3
        
s1=student(10,12)
s2=student(20,40)

s3=s1+s2
s3.m1
s3.m2

s1.m2
s2.m2

#method overloading
"in this we have in a class different methods"
#python doesn't support method overloading

class add1:
    def add(self,a=None,b=None):
        return(a+b)
    def add(self,a,b,c):
        return(a+b+c)
        
a=add1()
a.add(20,30)


class add1:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return(a+b+c)
        elif a!=None and b!=None:
            return(a+b)
        else:
            return a
b=add1()       
b.add(1)

#method overriding
"same method used in different class"

class s:
    def add(self,a,b):
        return a+b
class p(s):      #class p overrides the class s
    def add(self,a,b):
        return a-b
ss=s()
ss.add(5,6)
ss=p()
ss.add(5,8)

#abstraction 
"""Abstraction means hiding the complexity and only showing the essential features of the object. So in a way, Abstraction means hiding the real 
implementation and we, as a user, knowing only how to use it."""

"we don't no the back ground process,ex: we go to atm we insert the card and enter the pin and get money but we don't no about background process"

class p:
    def add(a,b):
        return(a+b)
ps=p()


p.add(2,3) #we know that it is addition adding but we don't know how it will happen


#Encapuslation"An objects variables should not always be directly accessible.
#To prevent accidental change, an objects variables can sometimes only be changed with an objects methods. 
#Those type of variables are private variables.
"""Python does not have the private keyword, unlike some other object oriented languages,
but encapsulation can be done.Instead, it relies on the convention: 
a class variable that should not directly be accessed should be prefixed with an underscore."""
#t also protects the integrity of the data 
#__ can't be seen and can't be accessed
class sachin():
   def __init__(self):
      self.a = 123
      self._b = 123
      self.__c = 123

obj = sachin()
obj.a=12
obj._b=21
obj.__c=25
obj.a
obj.__init__
obj._b
obj.__c


#Python’s private and protect member can be accessed outside the class through python name mangling.


"special method(magic/Dunder)"
#in this method we can print the object

class special():
    def __init__(self,name,age,page):
        self.name=name
        self.age=age
        self.page=page
    def __str__(self):
        return ('he is {},age is '.format(self.name,self.age))
    def __len__(self):
        return self.page
    def __del__(self):
        print ("a book is deleted")
        
b=special('sachin',23,200)
print(b)
str(b)

len(b)

del b

"""You may have noticed the self parameter in function definition inside the class but, 
we called the method simply as ob.func() without any arguments. It still worked.

This is because, whenever an object calls its method, the object itself is passed as the first argument. 
So, ob.func() translates into MyClass.func(ob).

In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an,
 argument list that is created by inserting the method's object before the first argument.

For these reasons, the first argument of the function in class must be the object itself.
 This is conventionally called self. It can be named otherwise but we highly recommend to follow the convention."""
 
 
class animal():
    def __init__(self,name):
        self.name=name
        
    def speak(self): #abstract method #we should not use in real time
        raise NotImplementedError('subclass must implement abstract')
a=animal(3)       
a.speak()



#public accessed from outside the class possible
class employee:
    def __init__(self, name, sal):
        self.name=name
        self.salary=sal
        
c=employee(1,2)
c.name
c.name=5


#protected
class employee:
    def __init__(self, name, sal):
        self._name=name
        self._salary=sal
        
c=employee(1,2)
c._salary
c._name=5
#the responsible programmer would refrain from accessing and modifying instance 
#variables prefixed with _ from outside its class.
# protected : accessible by the classes of the same package and the subclasses residing in any package

#private
#private : accessible within the same class only.
class employee:
    def __init__(self, name, sal):
        self.__name=name  # private attribute 
        self.__salary=sal # private attribute
        
e=employee(1,2)
e.__salary  # attrribute errror



#getters and setters
class person:
    def __init__(self, name="Guest"):
        self.__name=name
    def setname(self, name):
        self.__name=name
    def getname(self):
        return self.__name
    
p=person()
p.__name #error
p.getname(1) #returns the name
p.setname('boss')


#using property
"""The property() method in Python provides an interface to instance attributes. 
It encapsulates instance attributes and provides a property,"""

#The property() method takes the get, set and delete methods as arguments and returns an object of the property class.

#prop=property(getter, setter, deleter, docstring)


class person:
    def __init__(self, name="Guest"):
        self.__name=name
    def setname(self, name):
        print('set name called')
        self.__name=name
       
    def getname(self):
        print('get name called')
        return self.__name
    name=property(getname,setname)
    
p=person()
p.name
p.name

#@property decorator
"""@property decorator allows us to define properties easily without calling the property() function manually. 
Before learning about the @property decorator, let's understand what is a decorator."""

#A decorator is a function that receives another function as argument. 
#The behaviour of the argument function is extended by the decorator without actually modifying it.


class person:
    def __init__(self):
        self.__name=''
    @property
    def name(self):   #getter and setter method
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value

p=person()
p.name='sachin' #setter
p.name #getter



"""def mydecoratorfunction(some_function): # function to be decorated passed as argument
    def wrapper_function(): # wrap the some_function and extends its behaviour
        # write code to extend the behaviour of some_function()
        some_function() # call some_function
        return wrapper_function # return wrapper function"""


#decorator
def mydecoratorfunction(some_function): # function to be decorated passed as argument
    def wrapper_function(str): # wrap the some_function and extends its behaviour
        print('hello')# write code to extend the behaviour of some_function()
        some_function(str) # call some_function
    return wrapper_function # return wrapper function
    
def s(msg):
    print('hai')
    
m=mydecoratorfunction(s)
m(s)

@mydecoratorfunction
def s(msg):
    print('hai')
    
m=mydecoratorfunction(s)
m(s)
