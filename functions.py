#!/usr/bin/python
import re
import os


def isLetter(string):
    match = re.match('[a-zA-Z]',string)
    if (match) or (string=='_'):
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
    words = ["if" , "then" , "else" , "read" , "end" , "repeat", "write", "until"]

    for i in range (0,8) :
        if string == words[i]:
            return 1
    else:

        return 0

    # if string == "if":
    #     return 1
    # elif string == "then":
    #     return 1
    # elif string == "else":
    #     return 1
    # elif string == "read":
    #     return 1
    # elif string == "end":
    #     return 1
    # elif string == "repeat":
    #     return 1
    # elif string == "write":
    #     return 1
    # elif string == "until":
    #     return 1    
    # else:
    #     return 0 


   


def isSpecial(string):
     match = re.match('[< > * () _ + := - ; / ]', string)

     if string == ' ':
         return 0

     if (match):
        return 1
     else:
        return 0

# def classifier(string):
#     if (isIdentfier):
#         if (reservedWords):
#             # pass to reserved word list
#         esle:    
#             # pass to identifiers list

#     elif (isSpecial):
#         # pass to sympols list
#     elif (isNumber):
#         #pass to numbers list 




# isSpecial('safd')
# identfier("777")     
# isChar('?')
# isNumber('7')
# reservedWords("until")



# words = ["if" , "then" , "else" , "read" , "end" , "repeat", "write", "until"]
# print(words)
# print(len(words))