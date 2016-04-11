import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    return z
mystery_function(1, 2)
""" 
1)when I run the code nothing happens. I know the results 
2) the output of the function is 3 , the only thing I did was put 'print' next to the Mystery_function(1,2)
"""
