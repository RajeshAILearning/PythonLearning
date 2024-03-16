

#FOR Loop
#declare a list
obj=[2, 3, 5, 7, 9]
#for variable in which list we want to iterate
for i in obj:
    print(i)
print("For loop is ended")

#TO print the multiples of 2 values presented in the list
for j in obj:
    print(j*2)
print("Loop Ended")

#range(x,y) -> x to y-1
for k in range(1,6) :
    print(k) # 1 2 3 4 5
print("Loop End")

#Sum of First 5 natural numbers 1+2+3+4+5=15
summation = 0
for l in range(1,6):
    summation = summation+l
print(summation)
print("Loop End")
#What if i want to increment more than 1 example i+2 declare it as a 3rd argument in range
for m in range(1,10,2):
    print(m) #1 3 5 7 9
print("Loop End")

#Print even numbers between 1 to 20
for n in range(0,21,2):
    print(n)
print("Loop End")

#What if I declare range with 1 parameter it starts from 0
for o in range(10):
    print(o)
print("Loop End")

#Print Reverse 10 to 1
for p in range(10,0,-1):
    print(p)
print("Loop End")
