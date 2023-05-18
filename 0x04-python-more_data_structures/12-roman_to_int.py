#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    num = 0
    numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i, roman in enumerate(roman_string):
        if i != 0 and numbers.get(roman) > numbers.get(roman_string[i - 1]):
            num += (numbers.get(roman) - 2 * numbers.get(roman_string[i - 1]))
        else:
            num += numbers.get(roman)
    return num
