#Motive - it's not a good practice to have all functions, but only those needed.
# therefore, we need to import some code before starting usage
# we can import modules and os's, module are more likely libraries
# library - .py files
# import sqlite3;
# dir(sqlite3)
# print(dir(sqlite3))
# print(os.__file__
# we can use pip from the terminal and install other modules / libraries
# package, module, library - all are actually the same (bunch of code from an external service)
# import glob2
# print(glob2.glob("*.txt"))
# """
# This script creates an empty file
# """
# print(__doc__) # will print the above example of the documentation
# python is able to give you the current date and time, alongside playing with numbers & strings
# date and time objects are special objects in python
# can be able to generate graphs.
# relevant modules: dateTime (manipulate, find, etc.), time (control the time when a script runs)
import datetime
# print(datetime.datetime.now()) # now's time with micro of sec.
# yesterday = datetime.datetime(2017, 11, 3)
# now = datetime.datetime.now()
# print((now - yesterday).days)
def create_file_curr_date():
    """ a method that creates a file with current date """
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"+".txt")
    method = "w+"
    with open(str(filename), method) as file:
        file.write("")
# function call
# create_file_curr_date()
# now = datetime.datetime.now()
# after = now + datetime.timedelta(days=2, seconds=10000)
# print(after)
# time module
# import time
# lst = []
# for i in range(5):
#     lst.append(datetime.datetime.now())
#     time.sleep(2)
filelist = ['Ex.2_MergeTextFiles/file1.txt', 'Ex.2_MergeTextFiles/file2.txt', 'Ex.2_MergeTextFiles/file3.txt']
def create_file_curr_date():
    """ a method that creates a file with current date """
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"+".txt")
    method = "a+"
    with open(str(filename), method) as file:
        file.write("")
    return filename

def mergeTxtFiles():
    """This method merge txt files based on a whatever variable"""
    with open(mergedfile, "w") as outfile:
        for fname in filelist:
            with open(fname, "r") as infile:
                outfile.write(infile.read() + "\n")
mergedfile = create_file_curr_date()
mergeTxtFiles()
