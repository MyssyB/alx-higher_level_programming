#!/usr/bin/python3

def add_integer(a, b=98):
    """This function adds 2 numbers,
    one has already been given by the function.
    a must be an integer.
    >>> add_integer(2, 98)
    100

    a must be a float
    >>> add_integer(2.3, 98)
    100.3

    Numbers <= 0 are not accepted

    >>> add_integer(-1, 98)
    Traceback (most recent call last):
        ...
    TypeError: number must be an integer or float

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer.")
    """a must be first casted into an integer if its a float"""
    a = int(a)
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    """b must be first casted into an integer if its a float"""
    b = int(b)

    return a + b
    """Return value must be an integer"""
