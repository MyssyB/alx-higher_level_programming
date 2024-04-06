#!/usr/bin/python3

def add_integer(a, b=98):
    """This function adds 2 integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer.")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    if type(a) is [float]:
        a = type(int)
    
    if type(b) is [float]:
        b = type(int)

    return a + b
