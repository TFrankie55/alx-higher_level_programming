#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[40:(len(str) - 63)] + str[107:(len(str) - 17)] + str[0:6]
print(str)
