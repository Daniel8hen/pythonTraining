# basic number types
# 1 for int, 1.0 for float (decimal attached to it)
# for each of those we can do arithmetic actions (+, -, *, /).
# use parenthesis for math order.
# modolu -> 4 % 2 -> 0; 4 % 3 however, 1 with a reminder of 1. So 1.
# power - x**y
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
#few relevant functions:
# range(0,5) / range(10) - gives you a range of numbers by desired value - 1 or 2 values.
#for i in range(10):
#    print(i)
# list comprehension (kind of for loops backwards)
# x = [num**2 for num in [1,2,3,4]] is like for num in [1,2,3,4]: \t out.append(num**2)
# print(x)
# functions
# convention: lower case value. E.g.
# the name = 'XYZ' is a default name
# def my_func(name='XYZ'):
#    """
#    This is documentation
#    """
#    print('hello ' + name)
#help(my_func)

# map
# seq = [1,2,3,4,5]

# def times2(var):
#    return var*2
# x = list(map(times2,seq))
# print x
# lambda expression:
# say we have a function (e.g. times2)
# def times2(var):return var*2 --> works fine
# the lambda expression version is: lambda var:var*2
# t = lambda var:var*2
# this is a re-writing way for function to one single line of code
# x = t(5)
# print(x)
# then in map we can use:
# list(map(lambda num: num*3, seq)) // for the sequence above
# filter function
# print(list(filter(lambda num: num%2 == 0, [1,2,3,4,5])))
# map will run the func / lambda among all of the values, filter will filter those who "answers" the logic term
# important string methods:
# s.lower() -> lower case a string
# s.upper() -> upper case a string
# s.split() -> split words into a list based on whitespace.
# s.split('string') -> split words into a list based on a specific given string
# dictionary methods
# d.keys() / d.items() - returns the keys / items accordingly
# d.values() - returns the values without the keys
# list methods:
# l.pop() - pops out the last item in the list (we can assign it to another value)
# l.pop(specific index)
# l.append('new item') -> to the end of the list
# 'x' in [1,2,3] // "in" operator false because no string x in this list
# 'x' in ['x',2,3] // true
# tuple unpacking - unpack and "get" only individual item in that tuple
# x = [(1,2),(3,4),(5,6)]
# for a,b in x:
#    print a
