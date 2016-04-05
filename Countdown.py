# variables
# 1. q == the highest value the user wants to use
# 2. numbers== is the starting point on the guessing game
#3.guess== the number the person guesses
# name== asking the person their name
# tries== how many tries it took to get the answer


name=raw_input(" What's your name?")
Upper_bound =input("What is the highest value you want to use?") #I switched from 'raw_input'
#to 'input '. raw input gives me a string not a integer.
tries= 0
import random
guess= input(" what number do you think it is?")
answer=random.randint(0,Upper_bound)
print answer
while  guess != answer:
    if guess>answer:
        print "too high"
        tries= tries+1
    elif guess<answer:
        print"too low"
    guess= input(" what number do you think it is?")
    print name,"it took you",tries,"try."
print name +"!","You got it right! it's",answer
