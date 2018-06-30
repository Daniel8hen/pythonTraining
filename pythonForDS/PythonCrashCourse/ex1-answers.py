# power of 7 by 4
#print(7**4)
# string split
#s = "Hi there Sam!"
#lst = s.split()
#print(lst)
#string format
#planet = "Earth"
#diameter = 12742
#print("The diameter of {} is {} kilometers".format(planet, diameter))
# find a specific node in a nested list ('hello')
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# print(list(lst[3][1][2]))[0]
# find a specific node in a Dictionary ('hello')
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# print(d['k1'][3]['tricky'][3]['target'][3])
# ** What is the main difference between a tuple and a list? **
# tuple - static values (immutable) - month list; list - dynamic values (mutable) - team members list
# a function that grabs email and returns the domain
# def get_domain(email=None):
#    """
#    This function gets an email and returns the domain after the "@"
#    """
#    if (not email) or (email is None) or ("@" not in email):
#        return
#    return email.split("@")[1]
# print(get_domain("abc.com"))

# def findDog(str):
#    """
#    This method gets a string and returns true if "dog" is part of it, false otherwise.
#    """
#    strDog = "dog"
#    if (strDog in str) or (strDog in str.lower()) or (strDog in str.upper()):
#        return True
#    return False
# print(findDog("No dog here"))
# def countDog(str):
#    """
#    This method returns number of occurneces of the word "dog" in a given string
#    """
#    return str.count("dog")
#print(countDog("dog in here dog in there three dogs in the air"))

#lambda expression to filter string that does not start with an 's'
# print(list(filter(lambda str: str[0] == 's', ['soup','dog','salad','cat','great'])))
# if elif else method
#def caught_speeding(speed, is_birthday):
#    if (speed <= 60):
#        return "No Ticket"
#    elif ((speed >= 61) and (speed <= 80) and is_birthday == False):
#        return "Small Ticket"
#    elif ((speed - 5 >= 61) and (speed <= 80) and is_birthday == True):
#        return "Small Ticket"
#    elif (speed > 80 and is_birthday == False):
#        return "Big Ticket"
#    elif (speed - 5 < 80 and is_birthday == True):
#        return "Small Ticket"
#    elif  (speed > 85 and is_birthday == True):
#        return "Big Ticket"
#print(caught_speeding(40,True))
