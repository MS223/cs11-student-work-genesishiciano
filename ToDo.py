activity= raw_input("What do you want to do?").capitalize()
Day= raw_input("What  day do you want to do this?")
Days_in_week={
'Sunday': [],
'Monday':[],
'Tuesday':[],
'Wednesday':[],
'Thursday':[],
'Friday':[],
'Saturday':[],
}
print Days_in_week
def add():
 for x in activity:
     Days_in_week[x]=activity.append(x)# I don't know what's going on here...
print Days_in_week


 #should get our action variable and add it to our dictionary -
# with the key day.

