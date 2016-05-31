class Time(object):
    def __init__ (self, hour,minute, second):#Call the function
        self.hour= hour # tells the computer what each element does
        self.minute = minute
        self.second = second
    def __str__(self): # turns all integer into strings
        return str(self.hour)+":"+str(self.minute)+":"+str(self.second)


    def __add__(self, other): #adds the strings
        return Time(self.hour+other.hour,self.minute+other.minute,self.second+other.second)
# for the computer to add more 'time' into the function
# the computer needs a 'global'variable - which in this function is known as 'time'
# because it is a 'global' variable, the computer - like a child, knows that the next element should be added to the first element. 
# once this process is done, The computer repeats the same process every time a new 'time' is added.



time1 = Time(5,32,0) # given time to use
time2 = Time(23,11,11)
time3 = Time(45,6,7)
time4 =Time (5,7,8)

print time1+time2+time3+ time4 # Call to Action
print time1
print time2
