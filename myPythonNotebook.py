
#age = input("Enter your age: ")
#new_age = float(age) + 50
#print(new_age)
#10 / 5
#x = 2 * 3 ** 2 ** 5
#print(x)
#c = "Here"
#x = c.replace("e","a")
#print(x)
#print(c.upper)
#c = "Hi There!"
#in Python you have two index systems (0...size -1 or -1, -2, etc)
#print(c[-1]);
#in Python you can print a part of a string,
#and the upper bound is always exclusively. e.g.:
#print(c[0:5]);
#print(c[-3:-1]);
#print(c[3:]);
#Lists - variety of data types (mutable)
#Remember - item != index
#l1 = ["Hello", 2, 3];
#print(l1);
#print(l1[1]);
#print(dir(list));
#l1.append(4);
#(l1.remove(4));
#print(l1);
#Tuples - not mutable - can't be changed - ()
#t = ("Hello", 3, 4)
#print(t[-1])
# print(dir(tuple))
#Dictionaries - the curly brackets
#d = {"Name":"John", "Surname":"Smith", "Cities": ("Porto", "Tel Aviv", "Madrid")}
#print(d);
#-----------#
#errors are divided by two - SyntaxErorrs (which are caused by syntax issues)
#and Exceptions
#First, the code is being checked for SyntaxErrors, then the code is being run, after running it
#Exception example: NameError - name is not defined...
#another one - ZeroDivisionError
#Handling Exception / Errors:
#The goal is to let the the code flow continue
# try:
#     z = 3 / 0
# except ZeroDivisionError:
#     z = 0
# print("printing z is " + str(z))
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         #can use only except: (for all types of errors),
#         #but can be specifically
#         return "You are dividing by zero"
#
# print(divide(6,6))
# print("End of Program")


#--------------#
#Functions and conditionals
#Functions - when writing the func itself, first use *def*, then write the name,
# then write a parameter
# inside, no need for its type (as JAVA for example), then use semicolon
def seconds_and_minutes_to_hours(minutes, seconds=3600):
    return minutes / 60 + seconds / 3600
# def seconds_to_hours(seconds):
#     return seconds / 3600

# default arg is passed only after the non default arg!
# NoneType is the actual type in the memory of a function
minutes = 120
seconds = 7200
print(seconds_and_minutes_to_hours(60))
# print("Number of hours for " + str(minutes_to_test) + " minutes in float is " + str(minutes_to_hours(minutes_to_test)))
# print("Number of hours for " + str(seconds_to_test) + " seconds in float is " + str(seconds_to_hours(seconds_to_test)))
