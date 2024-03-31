#!/usr/bin/python3

class Employee:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print("Hello, How are you?, My name is", self.name)

Peter = Employee('Peter')
Peter.say_hello()
#the __init__ method: is run as soon as an object of a class hs been instantiated. The method is useful to do any initialization (that is passing initial values to your object).

