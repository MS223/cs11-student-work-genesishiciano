text_input= raw_input("Write your text here") # The text that you are going to use
user_choice= raw_input("what word do you want to find? ") # the word that the person is looking for
text_input=text_input.lower()# change all of the inputs into lower case
text_input=text_input.replace(".", " ")# changes all of the '.' into spaces- so it won't affect the code
text_input= text_input.replace(",", " ")# changes all of the ',' into spaces - same reason as above
text_input=text_input.replace(";"," ")# changes all of the ';' into spaces - same reason as previously stated
text_input=text_input.split() # breaks apart the text that is given into a list

My_dictionary={} # empty list- in this list the values for Text_input will be inserted
for x in text_input:# This is a loop- which reapeated
    My_dictionary[x]=text_input.count(x)
print My_dictionary[user_choice]
