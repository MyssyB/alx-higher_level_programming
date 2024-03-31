#!/usr/bin/python3

class Person:
    '''This class list the number of persones using this PC'''
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Hello ", self.name)

    def input_name(self):
        '''This method received input'''
        print(input("enter your name: "))

    def create_account(self):
        '''User creates and account'''
        print(input("Enter First Name: "))
        print(input("Enter Last Name: "))
        print(input("Enter email address:"))
   

person1 = Person("BEULAH")
person1.welcome()

person2 = Person("Favour")
person2.input_name()

person3 = Person("MAmmy")
person3.create_account()
#create a small method that accepts user input

