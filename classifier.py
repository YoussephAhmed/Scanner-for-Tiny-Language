 #!/usr/bin/python
import re
import os

words = ["if" , "then" , "else" , "read" , "end" , "repeat", "write", "until"]
 
tokens = ['read' , 'x' , ':=' , '3' , ';']

identifiers = []
specialones=[]
numbers=[]
reserved=[]
def isChar(string):
    match = re.match('[a-zA-Z]',string)
    if (match):
        return 1
    else:
        return 0

def isNumber(string):
    match = re.match('[0-9]',string)
    if (match):
        return 1
    else:
        return 0

def isIdentfier(string):
    match = re.match('[_a-zA-Z][_a-zA-Z0-9]',string)
    if (match):
        print(1)
        return 1
    else:
        print(0)
        return 0

def reservedWords(string):
    for i in range (0,8) :
        if (string == words[i]):
            return 1
    else:
        return 0

def isSpecial(string):
     match = re.match( '[< > * () _ + := - ; / ]' , string)
     if (match):
        return 1
     else:
        return 0    

def classifier(mylist):
        for i in range(0,len( mylist)):
            if (isIdentfier(mylist[i]) and not reservedWords(mylist[i])):
                identifiers.append(mylist[i])
            elif (reservedWords(mylist[i])):
                reserved.append(mylist[i])
            elif (isSpecial(mylist[i])):
                specialones.append(mylist[i])
            elif (isNumber(mylist[i])):
                numbers.append(mylist[i])

classifier(tokens)
print('identifers:',identifiers)
print('special' , specialones)
print('numbers' , numbers)
print ('reserved' , reserved)


