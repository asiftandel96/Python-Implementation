# Any callable python object that is used to modify a function or class
# Using Function as Paramater
"""
def function1():
    print('Hi I am Function1')


def function2(func):
    print('Hi I am Function2 will call function1')
    func()


function2(function1)

"""
# Using  Simple Decorator
"""
def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()

    return inner


@str_upper
def print_str():
    return 'good morning'


print(print_str())

"""
# Using Some Example
"""
def divide_decorator(func):
    def inner(x, y):
        if y == 0:
            return "give proper input"
        return func(x, y)

    return inner


@divide_decorator
def div(a, b):
    return a / b


print(div(4, 2))

"""
# Write a Python Program to add two numbers using Decorators
"""
def decorator_Add(func):
    def inner(x, y):
        if y < 0:
            return "Sorry y should be positive"
        return func(x, y)

    return inner


@decorator_Add
def Add(a, b):
    return a + b


print(Add(1, 1))

"""
# Thing we need to consider while creating a decorator
# 1)Need to take function as a parameter
# 2)Add Functionality  to Function
# 3)Function need to return another function
"""
def Decorator_Function(func):
    print('Before Even Numbers is Starting')

    def inner(x):
        if x > 100:
            return "Numbers not approachable"
            return x
        return func(x)

    return inner


@Decorator_Function
def Even_No(a):
    return a


print(Even_No(100))
"""

# How to Use Multiple Decorators on Single Function
"""
def upper_d(func):
    def inner():
        str1 = func()
        return str1.upper()

    return inner


def split_d(func):
    def wrapper():
        str2 = func()
        return str2.split()

    return wrapper


@split_d
@upper_d
def ordinary():
    return "good morning"


print(ordinary())

"""
# How to Use Decorators with Paramaters
"""
def outer(expr):
    def upper_d(func):
        def inner():
            return func() + expr

        return inner

    return upper_d


@outer('Asif')
def ordinary():
    return 'good morning'


print(ordinary())

"""
# Use Simple Examples
"""
def Add_No(exp1, exp2):
    def upper(func):
        def inner():
            str1 = exp1 + exp2
            return str1
            return func()

        return inner

    return upper


@Add_No(1, 5)
def ordinary():
    return ordinary


print(ordinary())

"""
# Using Single Decorator on Multiple Function(General Decorator Functions)
"""
def div_decorator(func):
    def inner(*args):
        list = []
        list1 = args[1:]
        for i in list1:
            if i == 0:
                return "give proper input"
        return func(*args)

    return inner


@div_decorator
def div1(a, b):
    return a / b


@div_decorator
def div2(a, b, c):
    return a / b / c


print(div1(10, 0))
print(div2(1, 10, 1))

"""
# Solving Some Example based on Single Decorators on multiple functions
"""
def decorator_m(func):
    def outer(*args):
        List = []
        List1 = args[1:]
        for i in List1:
            if i % 2 == 0:
                return "This is an even no solution"
            elif i % 4 == 0 or i % 5 == 0:
                return "This is divisible by 4 or 5"
            else:
                return "This is a normal Solutions"
            return func(*args)

    return outer


@decorator_m
def multiply(a, b):
    return a * b


@decorator_m
def multiply_1(a, b, c):
    return a * b * c


print(multiply(11, 12))
print(multiply_1(5, 5, 5))
"""

# Doing Some Basic Examples

# Write A Python Program to find the odd no using Decorators
"""
def decorators(func):
    def inner(x):
        x = 1
        if x % 2 == 0:
            x = x + 1
            return x
        return func(x)

    return inner


@decorators
def Odd_No(a):
    return a

print(Odd_No(50))

"""

# Class Decorators
# Creating A Decorator and implementing it in the class
"""
def check_name(method):
    def inner(name_ref):
        if name_ref == 'Asif':
            print('Hey my name is also same')
        else:
            method(name_ref)

    return inner


# Implementing the decorator function in the class
class Printing:
    def __init__(self, name):
        self.name = name

    '''This is the decorator function that is implemented in the class'''

    @check_name
    def print_name(self):
        print("entered name is:", self.name)


p = Printing('Yates Sir')
p.print_name()

"""
# Now Using Class as a Decorator
"""
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        str1 = self.func()
        return str1.upper()


@Decorator
def greet():
    return "good morning"


print(greet())

"""


# Now Using Another Example to build the concepts around the decorator
"""
class Check_div:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        list = []
        list1 = args[1:]
        for i in list1:
            if args[1] == 0:
                return "You cannot divide"
            else:
                return self.func(*args, **kwargs)


@Check_div
def div(a, b):

    return a/b


def div_1(a, b, c):
    return a/b/c


print(div(10, 3))

print(div_1(10, 4, 1))


"""

# Doing some experiment
"""
def Even_no(func):
    def inner(x):
        if x % 2 == 0:
            return x

        return func(x)

    return inner


class Ma:
    def __init__(self, a):
        self.a = a

    @Even_no
    def print_i(self):
        print('the entered value is even:', self.a)


M = Ma(20)
M.print_i()
"""