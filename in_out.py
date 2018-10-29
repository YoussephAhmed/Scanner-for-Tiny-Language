def read_lines():
    lines = [line.rstrip('\n') for line in open('test.txt')]
    for line in lines:
        #get_token(line)
        print(line)
        print("----------")


if __name__ == "__main__":
    read_lines()