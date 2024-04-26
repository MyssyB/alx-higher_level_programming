#!/usr/bin/python3

"""Function that reads a text file"""


def read_file(filename=""):
    """reading a text file UTF8 and prints to stdoutput"""
    with open(filename, "r") as f:
        print(f.read())
