# basic number types
# 1 for int, 1.0 for float (decimal attached to it)
# for each of those we can do arithmetic actions (+, -, *, /).
# use parenthesis for math order.
# modolu -> 4 % 2 -> 0; 4 % 3 however, 1 with a reminder of 1. So 1.
# var assignments:
# x = 6. We can do x = x + x in case x has a value already
# variables can't have special symbols, usually lower case letter
# for python, proper syntax is using underscore
# strings: Two ways of using strings -
#1. single quote / double quote (depends in the value inside - I can't see him for examle)
# Printing is by: x = "hello"
# print(x)
# print formatting:
# num = 10
# name = "Daniel"
# print ('My number is {} and my name is {}'.format(num, name))
# second way:
# num = 10
# name = "Daniel"
# print ('My number is {one} and my name is {two}. more {one}'.format(one=num, two=name))
# string indexing - starts in 0...n - n size of string for example
# s = 'hello'
#indexing example
# print(s[:3])
# lists:
# my_list = ['a','b','c']
# my_list.append('d')
# print(my_list)
# my_list[1] = '15'
# print(my_list)
# nest = [1,2,3,[4,5,['target']]]
# print(nest[3][2][0])
#dictionary: Key - value structure:
# d = {'key1':[1,2,3],'key2':123}
# call it by key!
# print(d['key1'][0])
#tuple
# t = (1,2,3)
# t[0] = 'New' #can't be done since tuple are immutable - user can't change the items in it
# in list, however, you can do it
# sets - a set is a collection of unique elements. In case you add same values to it, it will remain the same
# set1 = {1,2,3}
# print(set1)
# set2 = {1,2,3,4,5,1,1,1,1,1,1,2,2,2,2,2,3,4,3,3,3,3,3}
# print(set2)
# when to use? list - team member names (dynamic);  Dictionary - phone book (less dynamic, different use case);
# tuple -they are like lists but can't be changed. Example: name of months in a year
