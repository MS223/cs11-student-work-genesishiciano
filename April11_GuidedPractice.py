# what does this function return ?
def print_only(x):
   y = x * 2
   print y
""" This function shows  the value of 'x' multiplied by two"""
# how is this one different ?
def return_only(x):
   y = x * 2
   return y
   """ This Function shows the value for 'x' only to the computer""" 

# let's try to use our 2 functions
print "running print_only ..."
print_only(7)
""" It prints out the final product of 7*2-which should be 14"""

print "running return_only ..."
return_only(7)
 """ This function does the same thing as the previous one- though, 
 the only difference is that the computer doesn't let the user see it"""

print "printing print_only ..."
print print_only(7)

print "printing return_only ..."
return_only(7)

print "using print_only ..."
print_only(7) + 6

print "using return_only ..."
return_only(7) + 6
""" The 'return' function only declares the value to the computer without showing it to the user .On the other hand, the 'print' function 
shows the user the output of the function.
"""
""" When trying to add to a function, it is only possible to do so when you are using a 'return' function. You cannot add an integer randomly when you 
use  'print'.
"""
