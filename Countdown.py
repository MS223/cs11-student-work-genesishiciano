# variables
# 1. upper_bound == the highest value the user wants to use

#2.guess== the number the person guesses
# 3.name== asking the person their name
#4. tries== how many tries it took to get the answer


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
    
if tries==1:
    print name," it took you 1 try."
else:
    print name,"it took you", tries, "tries."
