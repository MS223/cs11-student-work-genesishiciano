def de_vowel(string ):
    consonants=[]
    for n in (string):
            if n!= 'a' and n!='e' and n != 'i' and n!='o' and n!='u' :
                consonants.append(n)
    print "".join(consonants)
de_vowel("hello")
#def count_vowels(string):
   # for x in (string):
