def odd_sum(input):
    total= 0
    for x in input:
        if x%2==1:
            total= total+ x
    print total
