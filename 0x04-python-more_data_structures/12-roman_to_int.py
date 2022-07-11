#!/usr/bin/python3
# 12-roman_to_int.py
# Tosin Owoeye <towoeye50@gmail.com

"""a function that converts a Roman numeral to an integer"""


def roman_to_int(roman_string):
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000'}
    number = 0
    if (not isinstance(roman_string, str)
            roman_string is None):
        return (0)
    for i in range(len(roman_string)):
        if conv.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1)) and
                conv[roman_string[i]] < conv[roman_string[i + 1]])
                num += conv[roman_string[i]] * -1

        else:
            number += conv[roman_string[i]]

    return (number)
