#!/usr/bin/python3

class Employee:
    def __init__(self, fname: str, lname: str, dateofbirth: int, age: int, sex: str, salary:int, email):
        print("New employee created")
        self.name = fname
        self.lname = lname
        self.dateofbirth = dateofbirth
        self.age = age
        self.sex = sex
        self.salary = salary
        self.email = fname + lname + "@gmail.com"
        print(self.name, self.lname, self.dateofbirth, self.age, self.sex, self.salary, self.email)

    def welcome(self):
        print("welcome to our organisaton ", self.name, self.lname)

emp1 = Employee("Peter", "smith", 12, 35, "male", 600, "Petersmith@gmail.com")
emp1.welcome()

emp2 = Employee("Jane", "Justin", 120198, 27, "female", 65000, "janejustine@gmail.com")
emp2.welcome()
