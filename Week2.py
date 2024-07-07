# Exercise-1
str1 = "John said:Let's learn Python together."
print(str1)
str2 = """ John said:Let's learn Python together."""
print(str2)
str3 = "John said, \"Let's learn Python together\"."
print(str3)
str4 = 'John said,"Let\'s learn Python together\".'
print(str4)

#Exercise-2
length = 56
width = 33
height = 30.5
volume = length*width*height
print(f"the volume of the box is {volume} cubic centimeters.")

#Exercise-3
email = "firstname.surname@unsw.edu.au"
domain_name = email.split('@')
print(domain_name[-1])

# Notes
print(6 / 2)  # Division always returns in float
f = 0.2+0.2+0.2
print(f == 0.6)  # == is for comparison and returns value in bool
print(f)

# None means null, it is not zero, False or empty
print(0 == False)
print(True == 1)

# Concatenate(+) two integers and two strings. Ex: 'dog' + 'cat'
# Can't concatenate(+) integer and string. Ex: 1+ 'dog'
# But we can multiply/duplicate string and integer. Ex: abx*3

x = str('abc')
y = str.upper(x)
print(str.upper(y)) # upper case exists in string class, just upper function will result in Error

z = 'CBA'.upper() # Other way to convert to upper case
print(z)
print(z.lower())

roh = 'hima'
print(roh.upper().lower())

# print("Hi".center(_width:30,_fillchar:"-")) ?

a = 5 # use f-string
print(f"age is {a}")

# print = 12, del(print) to return print function.
#PEP 8- Sryle guide for python

import week1
print(week1.Qantas_Stock)

#List, tuple. Append vs extend
#remove items from list: remove(), pop(), pop(3) clear()

"the exam's date is {} you will have {} minutes.format(date.mins)"

