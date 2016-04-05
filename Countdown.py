# variables
#1.upper_bound == the highest value the user wants to use
#2.guess== the number the person guesses
#3.name== asking the person their name
#4.tries== how many tries it took to get the answer

name=raw_input(" What's your name?") # ask the user what their name is
Upper_bound =input("What is the highest value you want to use?") #I switched from 'raw_input'
#to 'input '. raw input gives me a string not a integer.
tries= 0 # starts the equation for "how many tries" the user took
import random # tells the computer how to import from the library the function called 'random'
guess= input(" what number do you think it is?") # asks the reader what they think the answer is
answer=random.randint(0,Upper_bound) # makes the computer input any random number from 0 until the number the user chooses.
print answer # print the ACTUAL answer
while  guess != answer: """ this loop tells the computer to do print out 'too high' if the guess that the user picks is too high.
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
