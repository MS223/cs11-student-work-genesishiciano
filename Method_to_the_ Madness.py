class Time(object):
    def __init__ (self, hour,minute, second):#Call the function
        self.hour= hour # tells the computer what each element does
        self.minute = minute
        self.second = second
    def __str__(self): # turns all integer into strings
        return str(self.hour)+":"+str(self.minute)+":"+str(self.second)


    def __add__(self, other): #adds the strings
        return Time(self.hour+other.hour,self.minute+other.minute,self.second+other.second)




time1 = Time(5,32,0) # given time to use
time2 = Time(23,11,11)


print time1+time2 # Call to Action
print time1
print time2
