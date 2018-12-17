import re


# General Functions


def vaild_next_char(i,n):
    if(i == n-1):
        return 0
    else:
        return 1



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
    match = re.match('[_a-zA-Z][_a-zA-Z0-9]?',string)
    if (match):
        return 1
    else:
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
     match = re.match('[< > * () + := \- ; / ]', string)

     if string == ' ':
         return 0

     if (match):
        return 1
     else:

        return 0







class Scanner:

    tokens = []


    def classifier(self,token):
        value_type = ()  # Tuple ( value , type )

        if (reservedWords(token)):
            value_type = (token, "Reserved Word")

        elif (isSpecial(token)):
            value_type = (token, "Special Symbol")

        elif ((isIdentfier(token))):
            value_type = (token, "Identfier")

        elif ((isNumber(token))):
            value_type = (token, "Number")

        else:
            value_type = (token, "Other")

        return value_type



    # el function de btrg3 kol l tokens bs mbt2olesh no3ha eh..
    # DFA is implemented here
    def get_tokens(self,line):
        # line = re.sub('[\s+]', '', line)
        state = "start"

        token = ""
        i = 0
        char = line[i]

        no_valid_token = 0

        while (1):

            if (state == "start"):
                if (char == ' ' or char == '\t'):
                    i = i + 1
                    char = line[i]
                    continue
                if isLetter(char):
                    state = "letter"
                elif isNumber(char):
                    state = "number"
                elif isSpecial(char):
                    state = "special"
                elif char == '{':
                    state = "comment"
                else:
                    no_valid_token = 1
            if state == "letter":
                while isLetter(char) or isNumber(char):
                    token += char
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                        # no_valid_token = 0
                    else:
                        no_valid_token = 1
                        break
                state = "acceptance"
            if state == "number":
                while isNumber(char):
                    token += char
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                        # no_valid_token = 0
                    else:
                        no_valid_token = 1
                        break
                state = "acceptance"

            if state == "special":
                while isSpecial(char):
                    token += char
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                        # no_valid_token = 0
                    else:
                        no_valid_token = 1
                        break
                state = "acceptance"

            if state == "comment":
                while (char != '}'):
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                    #   no_valid_token = 0
                    else:
                        no_valid_token = 1
                        break
                state = "start"
                if (vaild_next_char(i, len(line))):
                    i = i + 1
                    char = line[i]

            if (state == "acceptance"):
                state = "start"
                _token = self.classifier(token)
                self.tokens.append(_token)
                token = ""

            if (no_valid_token and (not (vaild_next_char(i, len(line))))):
                break


    def read_lines(self,filename):
        in_file = open(filename, "r")
        lines = in_file.readlines()
        comment = False
        for line in lines:
            # lw la2et satr fady e3mlw scip
            if (line == '\n'):
                continue

            # -------> el goz2 da 3shan a handle el comment in 2 or more lines

            # x > 7 { da comment na2s
            if (line.find('{') != -1 and line.find('}') == -1):
                temp = line
                comment = True

            # da tkmlt el comment } y := 5
            if (line.find('{') == -1 and line.find('}') != -1):
                line = temp + line
                comment = False

            if (comment):
                continue
            self.get_tokens(line)
        in_file.close()

    def out_lines(self, filename):

        text_file = open(filename, "w")

        for item in self.tokens:
            text_file.write(item[0] + "----" + item[1])
            text_file.write("\n")

        text_file.close()





