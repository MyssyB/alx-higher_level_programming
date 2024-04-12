#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """This method takes in 2 arguments and returns it. For example
    >>> say_my_name("Beulah", "Agiande")
    Beulah Agiande
    
    If input is not string, raise type error
    >>> say_my_name(2, 4)
    Traceback (most recent call last):
        ...
    TypeError: first_name and last_name must be a string
    """
    
if type(first_name) is not [str]:
    raise TypeError("first_name must be a string")

if type(last_name) is not [str]:
    raise TypeError("last_name must be a string")

print(input("My name is <first name> <last name>"))
