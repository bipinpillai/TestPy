
import datetime
x= datetime.datetime.now()
print(x)

str = "abcdefgh"
print(str.upper())
myList = ["Abc", "Def", "Ghi"]
x=myList.reverse()
print(myList)

import json
print(json.dumps(31.76))
y = json.dumps(myList)
print(y)

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%x %X %Z %a"))

import os
print(os.getcwd())

import re
str = "The rain in Spain"
x = re.split("\s", str)
print(x)

print('tea for too'.replace('too', 'two'))

import math
print(math.cos(math.pi / 4))

import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))   # sampling without replacement
print(random.random())    # random float
print(random.randrange(6))    # random integer chosen from range(6)

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(2006, 9, 26)
age = now - birthday
print(age.days)

if "abc" == "abc":
    print("yes")