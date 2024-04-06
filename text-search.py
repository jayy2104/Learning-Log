# this prompt is used to find all of the occurence of 'Mr' and 'Mrs' in chapter 1 of Harry Potter 1

with open('J. K. Rowling - Harry Potter 1 - Sorcerer\'s Stone.txt') as file:
    text = file.read()

import re

# create a search system
def ctrlf(string):
    occurence = {}
    for i in string:
        occurence += 1
    return occurence

string = input('enter your search: ')
object = re.compile(string)

print(ctrlf(object.findall(text)))

# find all occurrences of Mr and Mrs
def ctrlf(string):
    occurence = {}
    for i in string:
        occurence[i] = string.count(i)
    return occurence

mo = re.compile(r'Mrs?\.\s?\w+')
print(ctrlf(mo.findall(text)))
