def Fruit_Pluralizer(list_of_strings):
   for x in (list_of_strings):

        if x[-1:] == "y":
            print x + "ies"

Fruit_Pluralizer(["berry", "banana"])
