# activity= raw_input("What do you want to do?").capitalize()
# Day= raw_input("What  day do you want to do this?")
Days_in_week={
'Sunday': [],
'Monday':[],
'Tuesday':[],
'Wednesday':[],
'Thursday':[],
'Friday':[],
'Saturday':[],
}

def add():
    user_choice=""

    while user_choice!= 'done'  :
        user_choice=raw_input("What do you want to do?")
        if user_choice=="done":
            return None
        Day=raw_input("what day?")
    Days_in_week[Day].append(user_choice) # finish Appending
add()
print Days_in_week













 #should get our action variable and add it to our dictionary -
# with the key day.

