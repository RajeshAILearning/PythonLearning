#Tuple is immuteable cannot modify it
#Tuple should be in () bracket
val=(1, 2, 'Rajesh', 3, 4.5)
print(val)

#try to update any value
val[2]="RAJESH"
#print(val) #TypeError: 'tuple' object does not support item assignment