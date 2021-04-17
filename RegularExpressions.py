# Regular Expression
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'
# . is a special charcaters in regular expressions
# pattern = re.compile(r'abc')
# pattern=re.compile(r'\.')
'''
pattern=re.compile(r'\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#Important Note for Regular Expression
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
'''
# Matching the Phone Numbers
# Matching the Numbers which is 800 and 900
""""
pattern_numbers = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches_num = pattern_numbers.finditer(text_to_search)

for match_n in matches_num:
    print(match_n)
'''
# Filter out some way
# a-z is the range of character from a to z
# ^ in this meaning outside of this block all characters
'''
pattern_alphabets = re.compile(r'[^bm]at')
matches_alphabets = pattern_alphabets.finditer(text_to_search)
for matches_alp in matches_alphabets:
    print(matches_alp, end='\t')
'''
# Handling Multiple Characters
'''
pattern_multiple = re.compile(r'\d{3}\-\d{3}\-\d{4}')
matches_multiple = pattern_multiple.finditer(text_to_search)

for matches_mu in matches_multiple:
    print(matches_mu)
'''
# Handling Multiple Character and Condition-Very Important Concept
'''
pattern_multi = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches_multi = pattern_multi.finditer(text_to_search)
for matches_multi in matches_multi:
    print(matches_multi)
    
'''
# Write A Regular Expression for email
'''
email = '''
asiftandel22@gmail.com
asif-tandel89@my-edu.net
CoreySchafer-189@my-work.edu
'''
pattern_com = re.compile(r'[a-zA-z0-9-]+@[a-zA-z-]+\.(com|net|edu)')
matches_com = pattern_com.finditer(email)
for matches_c in matches_com:
    print(matches_c)

#Managing Groups

email_id='''
http://www.google.com
https://coreyms.com
http://yahoo.com
http://naso.gov.in
'''
pattern_id=re.compile(r'https?://(www\.)?(\w+)+(\.\w+)')
matches_id=pattern_id.finditer(email_id)
for match_ie in matches_id:
    print(match_ie.group(2))
"""
# Managing URL By sub-URL
"""
url = '''
http://www.google.com
http://www.yahoo.com
https://nasa.gov.in
'''

pattern_url = re.compile('https?://(www\.)?(\w+)+(\.\w+)')
sub_url = pattern_url.sub(r'\2\3', url)
print(sub_url)
"""

# Other Function or method associated with Regular Expressions
"""
url = '''
http://www.google.com
http://www.yahoo.com
https://nasa.gov.in
'''
sentence_ai='Start with a sentence with a literal'
#pattern_url = re.compile('https?://(www\.)?(\w+)+(\.\w+)')
#match_iu=pattern_url.findall(url)
pattern_ic=re.compile(r'sentence')
matches=pattern_ic.search(sentence_ai)
print(matches)
"""
# Some Exercise that is needed to be solved for regular expression Write a Python program to check that a string
# contains only a certain set of characters (in this case a-z, A-Z and 0-9)
"""
Alphabets='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123456789
'''
pattern=re.compile(r'\w')
matches=pattern.finditer(Alphabets)
for mat in matches:
    print(mat)
"""
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
# Write a Python program that matches a word at the beginning of a string.
"""
beg='Start with a sentence'
pattern=re.compile(r'Sentence')
matches=pattern.finditer(beg)
for match in matches:
    print(match)
"""
# Write a Python program that matches a word containing 'z', not at the start or end of the word.
"""
Sentence_z='Start with a sez score'
pattern=re.compile(r'z')
matches=pattern.search(Sentence_z)
print(matches)
"""
# Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores
"""
Sentences='This is a ASIF_tandel which is true awesome'
pattern=re.compile(r'[A-Z]+\_[a-z]+')
matches=pattern.finditer(Sentences)
for matche in matches:
    print(matche)
"""
# Write a Python program where a string will start with a specific number.
'''
Sentence_num='800 is a concert that is specified by 800 and then start with  a noise sense'
pattern=re.compile(r'[^800][a-z]')
matches_i=pattern.finditer(Sentence_num)
for matr in matches_i:
    print(matr)
'''
# Write a Python program to remove leading zeros from an IP address
"""
IP_Address='''
125.125.125.0
126.126.0.0
124.0.0.0
0.0.0.0
'''
pattern=re.compile(r'[^0]')
matches=pattern.finditer(IP_Address)
for matc in matches:
    print(matc)
"""
# Write a Python Program to read email from a file using Regular Expression
with open('names.csv', 'r') as f:
    f_contents = f.read()
    pattern = re.compile(r'[a-z-]+@[a-z]+\.com')
    matches = pattern.finditer(f_contents)
    for match in matches:
        print(match)
