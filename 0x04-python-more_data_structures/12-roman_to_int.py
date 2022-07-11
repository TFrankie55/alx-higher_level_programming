#!/usr/bin/python3
# 12-roman_to_int.py
# Tosin Owoeye <towoeye50@gmail.com

"""a function that converts a Roman numeral to an integer"""


def roman_to_int(roman_string):
    if (not isinstance(roman_string, str)
            or roman_string is None):
        return (0)

    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000'}
    number = 0

    for i in range(len(roman_string)):
        if roman_dict.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1)) and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]])
                num += roman_dict[roman_string[i]] * -1

        else:
            number += roman_dict[roman_string[i]]

    return (number)
