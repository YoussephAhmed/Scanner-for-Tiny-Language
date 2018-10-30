from functions import *
import re
import os


tokens = []

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


            if isLetter(char):
                state="1"
                while isLetter(char)or isNumber(char):
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

def read_lines(filename):
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        get_tokens(line)

    file.close()





def main():
    read_lines('test.txt')

if __name__ == "__main__":
    main()
