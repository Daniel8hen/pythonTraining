# numpy array - 1D / 2D
# casting a numpy array from python object
# my_list = [1,2,3]
import numpy as np
# arr = np.array(my_list)
# my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(np.array(my_matrix)) --> #2 dimensional array
# arr = np.arange(0, 11, 5) #start, #end (excluding), #step - for quickly generating array using numpy
#print(arr)
#print(np.zeros((6,6))) #pass 1 value / tuple(!)
#print(np.ones(1))
#print(np.linspace(0,5,100)) #generating an array with "number of points" (3rd element)
#print(np.eye(5))

# print(np.random.rand(5,5)) - #no need for tuple!
# print(np.random.randn(2)) - #from standard normal distribution
#np.random.randint(1,100,10) - #10 random numbers between 1 and 99
# arr.reshape(5,5) - #reshape existing array
#argmax for index of max, max of max value, same for min...
#from numpy.random import randint
# print(randint(2,10))

#indexing and selection
# arr = np.arange(0,11)
# print(arr[6]) #indexing
# print(arr[1:10:3]) #from, up to, in jumps of
# print(arr[:6]) #up to 6
# print(arr[5:]) #from 5th index and everything beyond
# print(arr[-1:]) #start from the last element and beyond (result: 1 element)
# arr[0:5] = 100
# print(arr)
# arr = np.arange(0,11) #reset array
# if doing something like:
# slice_of_arr = arr[0:6]
# slice_of_arr[:] = 99
# print(slice_of_arr)
# print(arr)
# the arr has been changed. This means that this is not a copy of a data (slice_of_arr), but a reference!
# this is due to the fact that python would like to avoid memory issues
# if we do want a copy...
# arr_copy = arr.copy()
# arr_copy[:] = 100
# print("Original Array NOT CHANGED: " + str(arr))
# print("Copy:" + str(arr_copy))


### 2D ARRAY ###
# arr_2d = np.array([[5,10,15],
#                    [20,25,30],
#                    [30,40,45],
#                    [100,200,300]])
# print(arr_2d[2][1]) # for specific element
# print(arr_2d[2]) # for specific row
# print("New convention: " + str(arr_2d[1,2])) #another convention
# print(arr_2d[:2,:1])
# print(arr_2d[3:, -1:])

# arr = np.arange(1,11)
# bool_array = arr > 5
# print(bool_array) # "casting" an array to a boolean array
# print(arr[bool_array]) #conditionly select elements where bool condition = true
# condition example: arr[arr > 3]
# 2d can be created by (as well):
# arr_2d = np.arange(50).reshape(5,10)
# print(arr_2d)


# ***NumPy Operations ***
arr = np.arange(0,11)
big_arr = arr + arr # works same for substraction, multiplication, arithmetic operations as well
# print(big_arr) - works with arrays and scalars
# print(arr ** 2)
# # universal functions
# print(np.sqrt(arr))
# print(np.exp(arr))
# print(arr.max())
# # print(np.log(arr))
# print(np.sin(arr))
# For more: https://docs.scipy.org/doc/numpy/reference/ufuncs.html
