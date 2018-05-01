'''Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].'''

#Declare list of subjects, verbs and objects
subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

#create list of sentences using list comprehension
lis = [[s+' '+v+' '+o] for s in subjects for v in verbs for o in objects]

#print each sentence in lis
for x in lis:
    print("".join(x))