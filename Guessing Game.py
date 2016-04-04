# variables
# 1. q == the highest value the user wants to use
# 2. numbers== is the starting point on the guessing game 
#3. 





Q=input("What is the highest value you want to use?") #I switched from 'raw_input'
#to 'input '. rax input gives me a string not a integer.
import random
numbers=0
answer=random.randint(0,Q)
print answer
if Q > answer:
