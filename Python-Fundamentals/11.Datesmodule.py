#date

import datetime

x = datetime.datetime.now() 

print(x)
"""
2020-02-24 16:52:26.342441
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.
"""

#Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))



#Get Current Date


import datetime

date_object = datetime.date.today()
print(date_object)

#to know the inside of datetime
import datetime

print(dir(datetime))


"""
Commonly used classes in the datetime module are:

date Class
time Class
datetime Class
timedelta Class
"""


import datetime

d = datetime.date(2024, 4, 13)
print(d)


#
from datetime import date

a = date(2019, 4, 13)
print(a)


#today
from datetime import date

today = date.today()

print("Current date =", today)


#The strftime() Method
#The datetime object has a method for formatting date objects into readable strings.

#The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

#%a	Weekday, short version	Wed	
#%A	Weekday, full version	Wednesday	
#%w	Weekday as a number 0-6, 0 is Sunday	3	
#%d	Day of month 01-31	31	
#%b	Month name, short version	Dec	
#%B	Month name, full version	December	
#%m	Month as a number 01-12	12	
#%y	Year, short version, without century	18	
#%Y	Year, full version	2018	
#%H	Hour 00-23	17	
#%I	Hour 00-12	05	
#%p	AM/PM	PM	
#%M	Minute 00-59	41	
#%S	Second 00-59	08	
#%f	Microsecond 000000-999999	548513	
#%z	UTC offset	+0100	
#%Z	Timezone	CST	
#%j	Day number of year 001-366	365	
#%U	Week number of year, Sunday as the first day of week, 00-53	52	
#%W	Week number of year, Monday as the first day of week, 00-53	52	
#%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
#%x	Local version of date	12/31/18	
#%X	Local version of time	17:41:00	#%%	A % character	%	


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%D")) #06/01/18

print(x.strftime("%A")) #Friday

print(x.strftime("%Y")) #2018

print(x.strftime("%m")) #06

print(x.strftime("%a"))#Fri

#weekday short version
import datetime

x = datetime.datetime.now()

print(x.strftime("%a"))

#weekday full version
import datetime

x=datetime.datetime.now()
print(x.strftime("%A"))

#%w	Weekday as a number 0-6, 0 is Sunday

x=datetime.datetime.now()
print(x.strftime('%w'))

##%d	Day of month 01-31	31	

print(x.strftime('%d'))

#%b	Month name, short version	Dec	
#%B	Month name, full version	December

print(x.strftime('%b'))
print(x.strftime('%B'))

##%m	Month as a number 01-12	12	

print(x.strftime('%m'))

##%y	Year, short version, without century	18	
#%Y	Year, full version	2018


print(x.strftime('%y')) #20
print(x.strftime('%Y')) #2020

#%H	Hour 00-23	17	
#%I	Hour 00-12	05	

print(x.strftime('%H')) #20
print(x.strftime('%I')) #2020

#%p	AM/PM	PM	
#%M	Minute 00-59	41	
#%S	Second 00-59	08	

print(x.strftime('%p'))
print(x.strftime('%M'))
print(x.strftime('%S'))

#%f	Microsecond 000000-999999	548513	
print(x.strftime('%f'))

#%z	UTC offset	+0100	
print(x.strftime('%z'))

##%Z	Timezone	CST	
print(x.strftime('%Z'))

#%j	Day number of year 001-366	365	
print(x.strftime('%j'))

#%U	Week number of year, Sunday as the first day of week, 00-53	52	
#%W	Week number of year, Monday as the first day of week, 00-53	52	
print(x.strftime('%U'))
print(x.strftime('%W'))

##%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
#%x	Local version of date	12/31/18	
print(x.strftime('%c'))
print(x.strftime('%x'))
#%X	Local version of time	17:41:00
print(x.strftime('%X'))

###%%	A % character	%	
print(x.strftime("'%B''%c''%x'"))



"""Get date from a timestamp
We can also create date objects from a timestamp. A Unix timestamp is the number of seconds between a particular date and
 January 1, 1970 at UTC. You can convert a timestamp to date using fromtimestamp() method."""
 
 
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)
 
y=datetime.datetime.now()
x.strftime('%Z')

#rint today's year, month and day

from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#time object to represent time
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)



#print hour ,minute,second

from datetime import time

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)


#datetime.datetime
from datetime import datetime

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)


#Print year, month, hour, minute and timestamp

from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())


#Difference between two dates and time

from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)


#Difference between two timedelta objects

from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)


#Python format datetime
"""The way date and time is represented may be different in different places, organizations etc.
 It's more common to use mm/dd/yyyy in the US, whereas dd/mm/yyyy is more common in the UK.
Python has strftime() and strptime() methods to handle this."""


#Python strftime() - datetime object to string

from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)


"""
n the above program, t, s1 and s2 are strings.

%Y - year [0001,..., 2018, 2019,..., 9999]
%m - month [01, 02, ..., 11, 12]
%d - day [01, 02, ..., 30, 31]
%H - hour [00, 01, ..., 22, 23
%M - minute [00, 01, ..., 58, 59]
%S - second [00, 01, ..., 58, 59]
"""


#Python strptime() - string to datetime
#The strptime() method creates a datetime object from a given string (representing date and time).


from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)



#The strptime() method takes two arguments:

#a string representing date and time
#format code equivalent to the first argument


from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))


#time object containing current time
from datetime import datetime

now = datetime.now().time() # time object

print("now =", now)
print("type(now) =", type(now))	



# Python timestamp to datetime

from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))



