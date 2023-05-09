#!/usr/bin/python3
for i in range(9):
    for j in range(9 - i):
        if i == 8 and j == 0:
            break
        print("{}{}".format(i, i+j+1), end=", ")
print("89")
