#!/usr/bin/python
import re
import os

words = ["if" , "then" , "else" , "read" , "end" , "repeat", "write", "until"]
typelist = []
valuelist = []
tokens=[]

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
    match = re.match('[_a-zA-Z][_a-zA-Z0-9]?',string)
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
    match = re.match('[< > * () _ + := \- ; / ]', string)
    if (match):
        return 1
    else:
        return 0 
def vaild_next_char(i,n):
    if(i == n-1):
        return 0
    else:
        return 1

def classify(list_of_okens):
    return type

def get_tokens(line):
   # line = re.sub('[\s+]', '', line)
    state="start"

    token=""
    #                       while len(line)!=0:
    i=0
    char=line[i]
    while(1):
        if(state=="start"):
            if (char==' '):
                i=i+1
                char = line[i]
                continue


            if isChar(char):
                state="1"
                while isChar(char)or isNumber(char):
                    token+=char
                    if(vaild_next_char(i,len(line))):
                        i=i+1
                        char=line[i]
                state="acceptance"

            elif isNumber(char):
                state = "2"#number
                while isNumber(char):
                    token += char
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                state = "acceptance"
            elif isSpecial(char):
                state = "3"  # number
                while isSpecial(char):
                    token += char
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                    else:
                        break
                state = "acceptance"

        if (state=="acceptance"):
            state = "start"
            print(token)
            tokens.append(token)
            token=""

        if ( not (vaild_next_char(i, len(line)))):
            break

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
    lines = fh.readlines()
    for line in lines:
        get_tokens(line)
    fh.close()

def main():
    getstr("file.txt")
    code = " read x ; x := x - 1 ;"
   # get_tokens(code)
   # print(tokens)
    classifier(tokens)
    for i in range(0,len(valuelist)):
        print(valuelist[i] + " is " + typelist[i])
main()

