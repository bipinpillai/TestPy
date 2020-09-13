print("helloworld")
#the line below is a if statement
b="well"
if b=="well": 
    print("true")
    print("okay")
    a=5
else:
    print("not the same")
    a=3
print(a)
if 7+4!=11:# this is an if|else statement
    print("correct")
else:
    print("wrong")
x = "siya"
x = "miya"
y = "potter"
print(x)
print(y)
print(x+" "+y)
print("goodnight")
miyaage=5 
print(miyaage)
x = "thing"
print(x)
print(type(x))
z = "Siya "
print(z+ "Pillai")
a=4
b=10
print(a+b)
u=5 
y=9.4
print(type(u)) #you can see what type the variable is by using this command
print(type(y))
x=4
print (4)
print ("m")
y=str(2)
z=str(3.0)
print (y+z)
y=2
z=3.0
print (y+z)
s=("siya")
print (s[3])
b = "Hello, World!"
print(b[2:8])
print(x)
#assignment from dad starts here #all testing and actual code
import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()
print (x.year)
print (x.strftime("%A"))

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A %d %B %Y"))


# z=input("Enter a date:")
# month = int(input("Enter a month:"))
# year = int(input("Hello, enter a year:"))
# date = int(z)
# t = datetime.datetime(year, month, date)
# print (t)
# current = datetime.datetime.now()
# print(current)
# days = current-t
# print (days)
#The challenge ends HERE
# line 79 tells the computer to calculate the length of the line 
e= ("hjfdshglulher;uo hrewguopevht ueriwthvuwitrhvjktlfhddjks;ghwte;hg")
print (len(e))

y = ("     I AM JUST TESTING THIS OUT WOOOOO        ")
print(y.strip())
print ("     i am here     ".strip())# the strip method takes away all spaces in the beg. or end
print (64 % 5) #modulus gives you the remainder of the div. problem

x = 5
print(x > 3 and x < 10)

#next assignment is to calculate the mean of three numbers that the user inputs
# Python program to get average of a list 
def Average(lst): 
    return sum(lst) / len(lst) 
  
# Driver Code 
lst = [15, 9, 55, 41, 35, 20, 62, 49] 
average = Average(lst) 
  
# Printing average of the list 
print("Average of the list =", round(average, 2)) 

thislist = ["apple", "banana", "cherry"]
print(thislist) 
# z=input("Enter a number:")
# y=input("Enter a number:")
x = int(input("Enter a number:"))
z = int(input("Enter a number:"))
y = int(input("Enter a number:"))


secondlist = [z,y,x]
print(secondlist)
average = Average(secondlist)
print("Average of the list =", round(average, 2))
# End of challenge 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 
  
  fruits = ["apple", "banana", "cherry"]
for item in fruits:
  print(item) 
#   if x == "banana":
#     break
