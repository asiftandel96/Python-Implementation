""" Python Lambda Functions/Anonymous Functions.Anonymous function are those function which are without name."""


# Defining a Normal functions.
def addition_num(a, b):
    c = a * b
    print(c)


addition_num(2, 42)
# Using A Lambda
# Syntax lambda arguments:expression
# Note-(Lambda Function can take single expression one at a time) (x+y-This is a expression)
s = lambda x, y: x + y
print(s(2, 3))
# Now Using lambda function with Filter() method
# Filter method filter out the list and give the output
List_li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
g = list(filter(lambda x: (x % 2 == 0), List_li))
print(g)
# Now Using Lambda function with map() method
c_2 = list(map(lambda x1, x2: x1 * 2 + x2 * 2, [2, 4, 6, 8, 10], [4, 2, 5, 7, 8]))
# Using Lambda Functions with reduce() method
from functools import reduce

c_3 = reduce(lambda x3, x4: x3 + x4, [1, 2, 4, 6, 7] + [1, 6, 7, 8, 9])
print(c_3)
# This is very Important Code
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

# Python Program to find Linear Equation using Lambda Functions
Linear_eq = lambda a, b: 3 * a + 4 * b
print(Linear_eq(3, 4))
# Python Program to find Quadratic Equations
Quadratic_eq = lambda a, b: (a + b) ** 2
print((Quadratic_eq(3, 4)))

Unknown_number = lambda x: x * x
print(Unknown_number(5))
# Write a Python program to sort a list of tuples using Lambda.
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)
# Python Program to sort List Of Dictionaries using lambda
models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key=lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)
# Write a Python program to filter a list of integers using Lambda
List_Integers = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
g_e = list(filter(lambda x: (x > 0), List_Integers))
print(g_e)
# Write a Python program to find if a given string starts with a given character using Lambda.
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java'))
