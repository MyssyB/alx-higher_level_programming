#!/usr/bin/python3

class MyList(list):
    """My list class"""
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        print(list.sort(list))
