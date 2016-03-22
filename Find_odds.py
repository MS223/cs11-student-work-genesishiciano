list= [3,4,7,13,54,32,653,256,1,41,65,83,92,31] # made a variable with a list

def find_odds(input): # declared a function called "find_odds, the purpose of "find_odds" is to... find the odd numbers in a list.
    for x in input: 
        if x%2== 1: # if the number has a remainder of one,then it is considered an odd number.
            print x # print all of the odd numbers 

find_odds(list) # print out all of the odd numbers in the varible "list"


