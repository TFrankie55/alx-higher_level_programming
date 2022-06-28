#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[0:40] + str[108:(len(str) - 18)] + str[0:6]
print(str)
