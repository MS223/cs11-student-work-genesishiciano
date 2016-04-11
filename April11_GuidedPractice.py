# what does this function return ?
def print_only(x):
   y = x * 2
   print y

# how is this one different ?
def return_only(x):
   y = x * 2
   return y

# let's try to use our 2 functions
print "running print_only ..."
print_only(7)

print "running return_only ..."
return_only(7)

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
