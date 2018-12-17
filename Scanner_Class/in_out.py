from scanner import *


def main():

    S = Scanner()
    S.read_lines('input.txt')
    S.out_lines('output.txt')


    for token in S.tokens:
        print("value: " + token[0] + " -> type: " + token[1])

if __name__ == "__main__":
    main()
