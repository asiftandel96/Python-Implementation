# Decorators
# First Class Objects

"""
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


greet_bob(say_hello)

"""

# This function arguments is not executed because it is take reference of the function and not arguments
# Inner function
"""
def parent():
    print('Printing the parent function')

    def first_child():
        print('Printing the first child function')

        def second_child():
            print('Printing the second child function')

        return second_child()

    return first_child()


parent()

"""

# Returning Function From Functions
"""
def parent_1(num):
    def first_child():
        return "Hi I am Asif"

    def second_child():
        return "Hi I am Yogesh"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent_1(1)
second = parent_1(2)
# print(first)
# print(second)
print(first())
print(second())

"""

# Simple Decorators
"""
def my_decorators(func):
    def wrapper():
        print('Something is happening before the function is called')

        func()
        print('Something is happening after the function is called')

    return wrapper


def say_whee():
    print('Whee!')


say_whee = my_decorators(say_whee)

say_whee()
"""
# Taking another example of decorators
"""
from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush,the neigbours are sleepy

    return wrapper


def say_whee():
    print('Whee!')


say_whee = not_during_the_night(say_whee)
say_whee()

"""


# In this two example we have used say_whee three times to simplya and make the code more Pythonic we will use
# @decorator-symbol in this
"""
def decorators(func):
    def wrapper_function():
        print('Something is happening before the function is called')

        func()
        print('Something is happening after the function is called')

    return wrapper_function


@decorators
def say_whee():
    print('Whee')


print(say_whee())
"""
# ReUsing Decorators:
"""
def do_twice(func):
        def wrapper_do_twice():

            func()
            func()

        return wrapper_do_twice
"""
"""
from Decorators import do_twice


@do_twice
def say_whee():
    print("Whee!")


say_whee()
"""


# Now Using Decorator With Arguments

def do_twice(func):
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, *kwargs)

    return wrapper_func
