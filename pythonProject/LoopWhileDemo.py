#While Loop -  Condition is true it executes the loop
it = 4
while it>1:
    print("Condition Matches")
    it=it-1
print("While Loop execution completed")

#Use condition inside while loop
it = 4
while it>1:
    if it != 3:
        print(it)
    it = it -1
print("Loop End")

#Break halt the execution
it = 4
while it>1:
    if it == 3:
        break
    print(it)
    it = it - 1
print("Loop End")

#Continue - when we want to skip current iteration and proceed to next iteration
it = 10
while it>1:
    ##======While Start============#
    if it ==9:
        it = it - 1
        continue #skips that 9 value iteration so wont be printed in the output
    #======If End==================#
    if it == 3:
        break
    #======If End==================#
    print(it)
    it = it - 1
#===========While End==============#
print("Loop End")


