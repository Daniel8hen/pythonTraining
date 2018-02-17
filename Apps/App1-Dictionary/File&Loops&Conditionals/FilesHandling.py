# Opening and reading a file
#relevant for bianry (e.g. .dll) or .txt file
# file = open("FileHandlingExample.txt", 'r')
# content = file.read()
# # print(type(content))
# file.seek(0)
# # file.seek(0) - get pointer back to start of file, otherwise a print will print nothing
# # since the pointer get back to start
# content = file.readlines()
# print(content)
# content2 = []
# # note this syntax. it's a list where a loop is running inside it, nice
# content2 = [s.rstrip('\n') for s in content]
# print(content2)
# # for i in content:
# #     print(i)
# #     i = i.rstrip("\n")
# # print(content)
# file.close()
# # For the exercise, logic as below
# fileFruits = open('fruits.txt', 'r')
# content = fileFruits.readlines()
# content = [r.strip('\n') for r in content]
# for i in content:
#     print(len(i))
#
# fileFruits.close()
#open creates a file when it is not exists
# file = open('write_example.txt', 'w')
# file.write('Line 1\n')
# file.write('Line 2\n')
# file.close()
# Ex. 1 - Files:
# file = open('ex1.txt', 'r+')
# numbers = [1,2,3]
# for i in numbers:
#     file.write(str(i)+'\n')
# file.seek(0)
# content = file.readlines()
# content = [s.rstrip('\n') for s in content]
# for i in content:
#     print(i)
# # file.close
# Summary:
# r - opens a file for reading only. Pointer is at the begining of the file, default mode.
# r+ - opens a file for both reading + writing. Pointer is at the begining of the file.
# w - opens a file for writing only. OVERRIDES FILE (if file not exist- will create a file!)
# w+ - writing + reading. OVERRIDES FILE (if file not exist- will create a file!)
# a - opens a file for appending. Pointer - end of exists file, otherwise - creates a file
# a+ - appending + reading. Pointer - end of exists file, otherwise - creates a file
with open("example.txt","a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\nLine 6")
