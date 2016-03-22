def odd_sum(input): # declares the function, the purpose of the function is to add all of the odd numbers
    total= 0 # create a variable with the value of zero
    for x in input:
        if x%2==1: # if the number has a remainder of one, then it is considered an odd number. 
            total= total+ x # add the variable "total" with the outputs of "odd_sum"
    print total # print the sum
