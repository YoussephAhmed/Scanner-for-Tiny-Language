#!/usr/bin/python
import re
import os


def isChar(string):
    match = re.match('[a-zA-Z]',string)
    if (match):
        print(1)
        return 1
    else:
        print(0)
        return 0

def isNumber(string):
    match = re.match('[0-9]',string)
    if (match):
        print(1)
        return 1
    else:
        print(0)
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
    if string == "if":
        return 1
    elif string == "then":
        return 1
    elif string == "else":
        return 1
    elif string == "read":
        return 1
    elif string == "end":
        return 1
    elif string == "repeat":
        return 1
    elif string == "write":
        return 1
    elif string == "until":
        return 1    
    else:
        return 0 


   


def isSpecial(string):
     match = re.match( '[< > * () _ + := - ; / ]' , string)
     if (match):
        print(1)
        return 1
     else:
        print(0)
        return 0    




# isSpecial('safd')
# identfier("777")     
# isChar('?')
# isNumber('7')