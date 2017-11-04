# a = 5
# if (a < 5):
#     print("less than 5")
# elif a == 5:
#     print("Super Equal!")
# else:
#     print("NOT LESS")
# def age_foo(age):
#     new_age = float(age) + 50
#     return new_age
#
# age = float(input("What's your age?"))
#
# if age < 150:
#     print(age_foo(age))
# else:
#     print("No possible!")

# -- Loops --
# myList = [1,2,3,4,5]
# for i in myList:
#     if i > 2:
#         print(i)
# input - user input based functions, commands, etc.
# iterate on multiple lists - for loop
# names = ['james', 'john', 'jack']
# emails_domains = ['gmail', 'hotmail', 'yahoo']
#
# for i,j in zip(names, emails_domains):
#     print(i,j)
#
# def currency_converter(rate, euros):
#     dollars = euros*rate
#     return dollars
# r = input("Enter the *rate* please: ")
# e = input("Enter the *euros* please: ")
# print(currency_converter(float(r),float(e)))
# While loops
# password = ''
# while password != 'python123':
#     password = input("Enter a password: ")
#     if password == 'python123':
#         print("logged in!")
#     else:
#         print("sorry, try again")
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

tempratrues = [10,-20, -289, 100]
for i in tempratrues:
    with open("example2.txt","a+") as file:
        file.write(str(c_to_f(i)) + "\n")
        file.seek(0)
        print(file.readlines())
