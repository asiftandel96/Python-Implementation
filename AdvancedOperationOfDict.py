# Advanced Operation of Dictionary,List,Set
'''person = {'name': 'Jenn', 'age': 23}

# First Approach Of String formatting
sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)
# Second Approach of String Formatting
sentence_second = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
print(sentence_second)
# Third Approach of String Formatting
sentence_three = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence_three)
# This Look Like a Html tag when we see the output
tag_h1 = 'h1'
tag_h2 = 'h2'
text_h1 = 'This is a First headline'
text_h2 = 'This is second headline'
sentence_firsthead = '<{0}>{1}</{0}>'.format(tag_h1, text_h1)
sentence_secondhead = '<{0}>{1}</{0}>'.format(tag_h2, text_h2)
print(sentence_firsthead + ' ' + '\n' + sentence_secondhead)


class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = person('John', 33)
sentence_fir = 'My name is {0.name} and I am {0.age}'.format(p1)
print(sentence_fir)

#fourth approach of String formatting
sentence_fourth='My name is {name} and I am {age} years old'.format(name='Asif',age=23)
print(sentence_fourth)

# Using Keyword variable length arguments
sentence_fifth = 'My name is {name} and I am {age} years old'.format(**person)
print(sentence_fifth)

# Using for Loops
for i in range(1, 11):
    sentence_for = 'The value is {:02}'.format(i)
    print(sentence_for)

pi = 3.145292
sentence_maths='pi value is equal to {:.3f}'.format(pi)
print(sentence_maths)

# Working With DateTime

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)
# March 01 2016-This Format to be acheived
my_date1 = datetime.datetime(2018, 9, 5)
print(my_date1)
sentence_u = '{:%B,%d,%Y}'.format(my_date1)
print(sentence_u)
# Some Sentence formation of The Date
Sentence_i = '{0:%B,%d,%Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date1)
print(Sentence_i)
'''




