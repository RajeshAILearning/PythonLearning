str = "RajeshkumarAcademy.com"
str1 = "Muthu"
str2 = "Rajesh"

print(str[1]) #a

print(str[0:5]) #Rajes

print(str+str1) #two string concatenation RajeshkumaMuthu

#To check word is presented in the given string returns true or false
print(str2 in str)

#Split
#break with .
var = str.split(".")
print(var)
print(var[0])
print(var[1])

#Trim to remove whote space use strip method in python
str4 = " Great "
print(str4.strip())

#to remove begining whitespace or left whitespace
print(str4.lstrip())

#to remove end whitespace or right whitespace
print(str4.rstrip())