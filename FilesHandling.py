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
# For the exercise, logic as below
fileFruits = open('fruits.txt', 'r')
content = fileFruits.readlines()
content = [r.strip('\n') for r in content]
for i in content:
    print(len(i))

fileFruits.close()
