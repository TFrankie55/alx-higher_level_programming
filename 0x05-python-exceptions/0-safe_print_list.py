#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in my_list:
            print("The value of x")
    except IndexError:
        if my_list is empty:
            print("The list is empty")
