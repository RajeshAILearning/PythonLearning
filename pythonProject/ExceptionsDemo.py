ItemsInCart = 0
# example - Expected output is 2 should be added
if ItemsInCart !=2:
    #raise Exception("products count not matching")
    pass # just moves to next line
#Assert - whenever assert method receives a false condition test case fail because conditon doesn't met
#assert(ItemsInCart == 2) # assertion error in output
assert(ItemsInCart == 0) #executed successfully
