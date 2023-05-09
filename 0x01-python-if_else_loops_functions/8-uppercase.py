#!/usr/bin/python3
def uppercase(str):
    for char in str:
        c = ord(char)
        if c > 96 and c < 123:
            c -= 32
        print("{}".format(chr(c)), end="")
    print("")
