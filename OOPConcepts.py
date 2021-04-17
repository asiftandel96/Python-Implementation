# OOP Concepts
# Creating A Class
# This is a manually code and we don't need this because we need to automate the
# process
"""
class Employee:
    pass


Emp_1 = Employee()
Emp_2 = Employee()

print(Emp_1)
print(Emp_2)

Emp_1.first = 'Asif'
Emp_1.last = 'Tandel'
Emp_1.email = 'Asif.Tandel@company.com'
Emp_1.pay = 50000

Emp_2.first = 'Test'
Emp_2.last = 'User'
Emp_2.email = 'Test.User@company.com'
Emp_2.pay = 60000

print(Emp_1.email)
print(Emp_2.email)

"""

# Creating A Class

''''
class Admission:
    def __init__(self, first, last, pay): # Creating An Instance of the Class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return '{}{}'.format(self.first, self.last)


Emp_12 = Admission('Asif', 'Tandel', '60000') 
print(Emp_12.email)
print(Emp_12.full_name())

print(Admission.full_name(Emp_12))

'''

# Creating A Class for Arithmetic Operators(+,-,*,/)
'''
class Addition:
    def __init__(self, a):
        self.a = a

    def function_num(self, c, d):
        e = c + d
        return e


Add_num = Addition(5)
print(Add_num.a)
print(Add_num.function_num(2, 5))
'''

# Normal Class Program

"""
class Total_Income:
    def __init__(self, IT_Courses, Finance_Courses):
        self.IT_Courses = IT_Courses
        self.Finance_Courses = Finance_Courses
        self.Total_Collected = IT_Courses + Finance_Courses

    def Extinct_Courses(self):
        if self.Total_Collected < 12000:
            print('The no of sales should be greater than this figures')
        else:
            print('Excellent Work')
        return bool


Fee_Structure = Total_Income(19000, 89000)
Fee_S = Total_Income(12000, 180000)
print(Fee_Structure.Total_Collected)
print(Fee_S.Extinct_Courses())
"""

# Creating A Class Variable
'''
class Employee:
    raise_amount = 1.04
    no_of_emps = 0

    def __init__(self, first, last, pay):  # Creating An Instance of the Class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emps += 1

    def full_name(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



print(Employee.no_of_emps)
Emp_12 = Employee('Asif', 'Tandel', 60000)
print(Emp_12.pay)
Emp_12.apply_raise()
print(Emp_12.pay)
Emp_12.raise_amount = 1.05
print(Employee.raise_amount)
print(Emp_12.raise_amount)
print(Employee.no_of_emps)
'''


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))



# @ClassMethod Concepts

'''
class Person:
    age = 25

    def printAge(cls):
        print("The age is:", cls.age)


Person.printAge = classmethod(Person.printAge)
Person.printAge()
'''
"""
from datetime import date


class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def FromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s.age is: " + str(self.age))


person_n = person('Adam', 19)
person_n.display()

person1 = person.FromBirthYear('John', 1985)
person1.display()


# Static Method

class Mathematics:

    def addNumbers(x, y):
        return x + y


# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))


class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if date.getDate() == dateWithDash:
    print("Equal")
else:
    print("Unequal")


class Dates_:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


class DatesWithSlashes(Dates_):
    def getDate(self):
        return Dates_.toDashDate(self.date)


date = Dates_("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if (date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")
"""