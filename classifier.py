 #!/usr/bin/python
from in_out import get_tokens
import re
import os

words = ["if" , "then" , "else" , "read" , "end" , "repeat", "write", "until"]
 
tokens = ['read' , 'x' , ':=' , '3' , ';']

typelist = []
valuelist = []

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
        return 1
    else:
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
                typelist.append("Identifier")
                valuelist.append(mylist[i])
            elif (reservedWords(mylist[i])):
                typelist.append("a Reserved word")
                valuelist.append(mylist[i])
            elif (isSpecial(mylist[i])):
                typelist.append("Special character")
                valuelist.append(mylist[i])
            elif (isNumber(mylist[i])):
                typelist.append("a Number")
                valuelist.append(mylist[i])


#def printit(valuetup,typetup):
def getstr(input):
    fh = open(input,"r")
    for line in fh:
        get_tokens(line)
    fh.close()

def main():
    getstr("scan.txt")
    classifier(tokens)
    for i in range(0,len(valuelist)):
        print(valuelist[i] + " is " + typelist[i])
main()

