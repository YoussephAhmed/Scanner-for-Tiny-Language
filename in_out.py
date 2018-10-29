from functions import *

classified_tokens= ""

def vaild_next_char(i,n):
    if(i +1 > n-1):
        return 0
    else:
        return 1



def classify(list_of_okens):
    return type
def print(map):
    return
def get_tokens(line):
    state="start"

    token=""
    #                       while len(line)!=0:
    i=0
    char=line[i]
    while(1):
        if(state=="start"):
            if isLetter(char):
                state="1"
                while isLetter(char)or isNumber(char):
                    token+=char
                    if(vaild_next_char(i,len(line))):
                        i=i+1
                        char=line[i]
                state="acceptance"

            elif isLetter(char):
                state = "2"#number
                while isNumber(char):
                    token += char
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                state = "acceptance"
            elif isLetter(char):
                state = "3"  # number
                while isSpecial(char):
                    token += char
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                state = "acceptance"
        elif (state=="acceptance"):
            print(token)
        if ( not (vaild_next_char(i, len(line)))):
            break





    return map

def read_lines():
    lines = [line.rstrip('\n') for line in open('test.txt')]
    for line in lines:
        get_token(line)
        print(line)
        print("----------")


if __name__ == "__main__":
    read_lines()