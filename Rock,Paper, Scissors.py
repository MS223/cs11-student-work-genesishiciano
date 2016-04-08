"""Variable:
    *name ===name of the person
    *ask == asks whether they want to play rock paper  scissors
    *
    *p
    *S


    """
import random
name=raw_input("what is your name?")
Question=raw_input("do you want to play rock ,paper,scissors?")
while  Question!= "yes":
    Question=raw_input("Choose either rock,paper, or scissors?")
else:
    print "ok",name,"let's play!"
list=["rock","paper","scissors"]
(random.choice(list))
if Question == "rock" and               """ This statement will only work while the the statements are true,
    random.choice(list)=="scissors"
or 
    Question == "paper" and 
    random.choice(list)=="rock"
or 
    Question == "scissors" and 
    random.choice(list)=="paper"
else:
question 
