"""Takes in an integer as the maximum value and prints out that value up to
number one.
"""
def Max_value(integer):
    for x in range(1,integer+1):
     print x
     
Max_value(90)

'''
This will compare two sets of lists and it will print
out the highest (numerical) value.
'''

def Compare_list(x):
  for x in list1:
    if x>list2[list1.index(x)]:
      print x
      else:
        print list2[list1.index(x)]

def Swapping_stars():
    width=input("what width?")
    height= input("what height?")
    for x in range (0,height):
        if x%2==1:
            print " * - " * width
        else:
            print ' - * '* width
       
Swapping_stars()
