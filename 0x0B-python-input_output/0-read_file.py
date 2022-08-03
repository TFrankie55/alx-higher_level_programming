#/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """reads the specified file and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as myFile:
        read_data = myFile.read()
    print(read_data, end="")
