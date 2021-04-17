""" How to add two noA"""
from cmath import pi
from math import sqrt

'''def num_add():
    num1, num2 = input("Enter two no:").split()
    c = int(num1) + int(num2)
    print(c)


num_add() '''

# How to find the square root of a no

'''num_sqr = input('Enter the no:')
num_result = sqrt(int(num_sqr))
print(num_result)'''

'''numbers = [1, 5, 9, 18, 27, 36]

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)'''

'''def intica_integers():
    num = int(input('Enter the no:'))
    if num > 0:
        print('Positive No')
    elif num < 0:
        print('Negative')
    else:
        print('Zero')


intica_integers() '''

'''a, b, c = input('Enter the no:').split()
if int(a > b and a > c):
    print('The largest no is {}'.format(a))
elif b > a and b > c:
    print('The largest no is {}'.format(b))
elif a == b == c:
    print('The no is invisible')
else:
    print('The largest no is {}'.format(c))
'''
'''List_min1 = [1, 2, 3, 4, 5, 6, 7]
print(min(List_min1)) '''
'''# How to find the area of the circle
r = 4
area = pi * r * r
print(area)
'''
# How to subs two no

'''def func_subs():
    num_sub1, num_sub2 = input("Enter the two no:").split()
    result = int(num_sub1) - int(num_sub2)
    print(result)


func_subs()'''
# How to Calculate the area of the Triangle
'''
breadth = 12
height = 13
Area1 = 0.5 * breadth * height
print(Area1)
# Python Program to Sort word in Alphabetic order

List_alp = ['Asif', 'Bina', 'Fina', 'Eiffel', 'Cibel', 'Geet']
print(List_alp)
List_alp.sort()
print(List_alp)
List_alp.pop(2)
print(List_alp)

var = 'James Bond'
print(var[2::-1])
print(len(var))
var = "James" * 2 * 3
print(var)
'''
'''def calculate(num1, num2=4):
    res = num1 * num2
    print(res)


x = 36 / 4 * (3 + 2) * 4 + 2
print(x)
'''

# Keyword variable length arguments
'''def person_name(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)

# List Comprehension
person_name('asif', age=25, mobile_no=9899999)'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
'''my_list = []
for n in nums:
    my_list.append(n)
print(my_list)
'''
'''my_list = []
print([n for n in nums])
print(my_list)
'''
# I want 'n*n' for each 'n' in nums
'''
my_list = []
for n in nums:
    my_list.append(n*n)
    print(my_list)

my_list= [n*n for n in nums]
print(my_list)
# Using a map + lambda
# my_list = map(lambda n: n*n, nums)
# print my_list
'''
# I want 'n' for each 'n' in nums if 'n' is even
'''my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
        print(my_list)

my_list = [n for n in nums if n % 2 == 0]
print(my_list)
'''
# Using a filter + lambda
# my_list = filter(lambda n: n%2 == 0, nums)
# print my_list

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
'''my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)
my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)
'''

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(zip(names, hero))'''
# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
'''my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict = {name: heros for name, heros in zip(names, heros)}
print(my_dict)
'''
# If name not equal to Peter

# Set Comprehensions
'''num_set = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

my_set = set()
for n in num_set:
    my_set.add(n)
print(my_set)

my_set = {n for n in num_set}
print(my_set)

List_top10naturalnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_List = [i for i in List_top10naturalnum if i % 2 == 0 and i % 4 == 0]
print(my_List)

'''
New_dict = {'name': 'Asif', 'age': 25}

'''for k, v in New_dict.items():
    print(New_dict) '''
my_dict = {k: v for (k, v) in New_dict.items()}
print(my_dict)




