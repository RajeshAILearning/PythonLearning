# To print anything
from builtins import type

print("hello")

# Declared a variable a and the value in that variable is 3 a = 3
a = 3
print(a)

# String
Str = "Hello World"
print(Str)

# No colon required at the end
# b,c,d having space should look better python suggests
b, c, d = 5, 6.45, "Great"
print(b)
print(c)
print(d)

# print("Value is "+b). this is not allowed in python
# Concatenating 2 different data types example String and integer
print("{},{}".format("Value is ", b))

# concatenating 3 data types
print("{},{},{}".format("Value is ", c, d))

#Concatenating same data types string
print("value is",d)

#COncatenating String and Float
print("value is ", c)

# print a b c d
print(a,b,c,d)

# to find the data type of the variable
print(type(b))
print(type(c))
print(type(d))

#Concate same Data type example stirng and String
s = "Rajesh"
r= 'kumar'
print(s+r)
print("The name is "+s+r)
