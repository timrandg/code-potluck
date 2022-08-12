'''
Regex is a syntax for describing text. It is very handy 
for various code situations--like searching for occurances
of text, breaking compound strings into components, extracting
information. 

\d represents a digit
{} represents the number of required characters (can also be {min,max})
-  some characters like hyphen, represent itself
In python r'' is a regular expression string. 
Make a regular expression string for a phone number and use it with:
re.search -- find first occurance 
re.match -- find starting at beginning of string
re.findall -- picks up all matches throught the string 
to find phone numbers in the following three sentences s1, s2, s3. 

>>> s1 = "This sentence contains a phone number (415-630-2001)."
>>> s2  = "This sentence contains a phone number (415-630-2001)."
>>> s3 = "415-630-2119 This sentence contains a two phone numbers (cell: 415-630-2001)." 

>>> phone_num =  r'\d{3}-\d{3}-\d{4}'
>>> assert re.search(phone_num, s1)[0] == '415-630-2001'
>>> assert re.match(phone_num, s1) == None
>>> assert re.findall(phone_num, s1) == ['415-630-2001']
>>> assert re.match(phone_num, s3)[0] == '415-630-2119' 
>>> assert re.findall(phone_num, s3) == ['415-630-2119', '415-630-2001']

'''
import regex as re
# Write your code here:
#re.search(regular_expression, string)
phone_num =  r'\d{3}-\d{3}-\d{4}'
s1 = "This sentence contains a phone number (415-630-2001)."
assert re.search(phone_num, s1)[0] == '415-630-2001'

assert re.match(phone_num, s1) == None
## This regular expression does not match s1 because s1 does not BEGIN with a phone number

assert re.findall(phone_num, s1) == ['415-630-2001']
## re.findall() will find all cases in a string that match the regular expression

s3 = "415-630-2119 This sentence contains a two phone numbers (cell: 415-630-2001)."
assert re.search(phone_num, s3)[0] == '415-630-2119'

assert re.match(phone_num, s3)[0] == '415-630-2119'

assert re.findall(phone_num, s3) == ['415-630-2119', '415-630-2001']

##What about for dates?
date_re = r'\d{3}-\d{3}-\d{4}' ##What is the regular expression for this?

date = '2022-08-12'

assert re.match(date_re,date)

#Do not edit any code below this line!
if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nWOOT! You know some regex syntax!')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.

