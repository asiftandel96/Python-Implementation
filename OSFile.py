# Understanding the functionality of the OS module
"""
import os
from datetime import datetime
# Checking all the methods and Function available in our os module
# print(dir(os))
# Get the current directory
# print(os.getcwd())
# Change the working directory
# os.chdir('E:/PyCharm Program/')
# print(os.getcwd())
# print(os.getcwd())
# Show the contents of the directory
# print(os.listdir())
# How to make Directory
# os.mkdir('OS-Demo-2/')
# os.makedirs('OS-Demo/Sub-Dir1/')
# Removing the directory
# os.removedirs('OS-Demo/Sub-Dir1/')
# print(os.listdir())
# Showing the contents of the file
# print(os.stat('E:/PyCharm Program/OS-Demo-2/test.txt').st_mtime)
# Changing the data into  human readable format
# mod_time = os.stat('E:/PyCharm Program/OS-Demo-2/test.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))
#Show how to access home directory and join files with it
print(os.environ.get('USERPROFILE'))
# print(os.getcwd())
fil_c = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
print(fil_c)
#Make a temporary file,directory and check if it exist or not
print(os.path.basename('tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))

# Working with Date,DateTimes,TimeDelta & TimeZones
# knive,aware datatime
import datetime
import pytz

# Working with year,month,day
# d = datetime.date(2016, 9, 24)
# print(d)
# Today Date
# The major difference b/w weekday and isoweekday is
# that weekday start with 0 and isoweekday start with 1
tday = datetime.date.today()
'''print(tday.year)
print(tday.weekday())
print(tday.isoweekday()) '''
# Working with Timedelta- Python timedelta() function is present under datetime library which is generally used for
# calculating differences in dates and also can be used for date manipulations in Python. It is one of the easiest
# ways to perform date manipulations.
tdelta = datetime.timedelta(days=10)
print('The today date is {} and timedelta day is after {} days'.format(tday, tdelta))
print(tday + tdelta)
# timedelta=date1+date2
# date2=date1+timedelta
bday = datetime.date(2020, 8, 22)
till_day = bday - tday
print(till_day.days)
# Working with hours,minutes and seconds
# t = datetime.time(9, 30, 45, 100)
# print(t)
# date - years,month,day
# time=hours,minutes,seconds,milliseconds
# datetime-will give everything
dt = datetime.datetime.today()
print(dt)
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

dt1 = datetime.datetime(2018, 9, 24, 12, 30, 45, tzinfo=pytz.utc)
print(dt1)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
print(dt_utcnow)

dt_now1 = datetime.datetime.now(tz=pytz.UTC)
print(dt_now1)
# Converting UTC TimeZones to our timezones
# for tz in pytz.all_timezones:
# print(tz)

dt_cal = dt_now1.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_cal)
dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)
# Strftime-Datetime to String
# Strptime-String to DateTime
dt_mtn1 = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn1.strftime('%B %d %Y'))
# Converting String to Datetime
dt_str = 'July 03, 2020'
dt_i = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt_i)
# Working with File
# f = open('test.txt', 'r')
# f.close()
# Reading File  with Context Manager
# Working with Small Files
# with open('test.txt', 'r') as f1:
#    f_contents = f1.read()
#    print(f_contents)
# Big Files:
# with open('test.txt', 'r') as f_r:
#   f_contents = f_r.readlines()
#   print(f_contents)

# With the extra lines:

with open('test.txt', 'r') as f_rl:
    f_contents = f_rl.readline()
    print(f_contents)
    f_contents = f_rl.readline()
    print(f_contents)
    f_contents = f_rl.readline()
    print(f_contents)

# Without the extra lines

with open('test.txt', 'r') as f_extra:
    f_contents = f_extra.readline()
    print(f_contents, end='')
    f_contents = f_extra.readline()
    print(f_contents, end='')
    f_contents = f_extra.readline()
    print(f_contents, end='')

# Iterating through the file

# for line in f1:
#    print(line, end='')

###Going Back....
# f_contents = f1.read()
# print(f_contents, end='')
# Printing by characters:
with open('test.txt','r') as f_re:
    f_contents = f_re.read(100)
    print(f_contents, end='')
    f_contents = f_re.read(100)
    print(f_contents, end='')
# f_contents = f_re.read(100)
# print(f_contents, end = '')

###Iterating through small chunks:
with open('test.txt','r') as f_re:
    size_to_read = 100
    f_contents = f_re.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents)
        f_contents = f_re.read(size_to_read)


###Iterating through small chunks, with 10 characters:

with open('test.txt', 'r') as f_resm:
    size_to_read = 10
    f_contents = f_resm.read(size_to_read)
    print(f_contents, end='')
    f_resm.seek(0)
    f_contents = f_resm.read(size_to_read)
    print(f_contents, end='')
    print(f_resm.tell())

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f_resm.read(size_to_read)
# print(f.mode)
# print(f.closed)
# print(f.read())


##Writing Files:
###The Error:
# with open("test.txt", "r") as f:
#    f.write("Test")

# Writing Starts:

with open("test2.txt", "w") as f:
    f.write("Test")
    f.seek(0)
    f.write("Test")
    #f.seek("R")

##Copying Files:

with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)

# Copying the/your image:
###The Error
# with open("bronx.jpg", "r") as rf:
# with open("bronx_copy.jpg", "w") as wf:
# for line in rf:
# wf.write(line)

###Copying the image starts, without chunks:

with open("asifij.png", "rb") as rf:
    with open("asifij_copy.png", "wb") as wf:
        for line in rf:
            wf.write(line)
###Copying the image with chunks:
# with open("bronx.jpg", "rb") as rf:
# with open("bronx_copy.jpg", "wb") as wf:
# chunk_size = 4096
# rf_chunk = rf.read(chunk_size)
# while len(rf_chunk) > 0:
# wf.write(rf_chunk)
# rf_chunk = rf.read(chunk_size)
# Automating and rename the names of the files
import os

# print(os.getcwd())
os.chdir('C:/Users/asif/OneDrive/Pictures/Screenshots')
print(os.getcwd())
for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    f_year, f_day, f_num = file_name.split('-')

    f_year = f_year.strip()
    f_day = f_day.strip()
    f_num = f_num.strip()
    print('{}-{}-{}{}'.format(f_num, f_year, f_day, file_ext))
 '''
# Generating random numbers and data using random module This random module is used to generate dummy datasets so
# that we can used it because we don't have the real datasets in hand.
import random

# The main difference b/w random function cannot take arguments but uniform can take arguments
'''a_random = random.random()
print(a_random)
aj = random.randint(1, 10)
print(aj) 
'''
# The main difference b/w choice and choices is that  choice take one arguments but choices can take multiple
# arguments one at a time .
'''List_aj = ['Red', 'Green', 'Black']
hand_oi = random.choice(List_aj)
print(hand_oi)

hand_i = random.choices(List_aj, weights=(3, 3, 2), k=8)
print(hand_i)

Deck = list(range(1, 53))
print(Deck)
random.shuffle(Deck)
print(Deck)
d = random.uniform(0, 1)
print(d)
#sample function take unique value but choices can take repetitive value
#k is the number of  value that we want in our List s
e = random.sample(Deck, k=10)
print(e)
'''
# Seed Function
# This is used in the generation of a pseudo-random encryption key. Encryption keys are an important part of computer
# security. These are the kind of secret keys which used to protect data from unauthorized access over the internet.
# It makes optimization of codes easy where random numbers are used for testing. The output of the code sometime
# depends on input. So the use of random numbers for testing algorithms can be complex. Also seed function is used to
# generate same random numbers again and again and simplifies algorithm testing process
'''random.seed(5)
List_o = random.randint(1, 100)
print(List_o) '''
# How to Read,Parse and Write CSV Files

import csv

# this is used to read the file
with open('names.csv', 'r') as csv_file:
    Csv_Reader = csv.reader(csv_file)
    with open('new_names1.csv', 'w') as new_file:
        # next(Csv_reader)- It is used to remove the headers from the data
        # This is used to write file
        Csv_Writer = csv.writer(new_file, delimiter='\t')
        for line in Csv_Reader:
            Csv_Writer.writerow(line)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
"""
