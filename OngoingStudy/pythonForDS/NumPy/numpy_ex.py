#import NumPy as np
import numpy as np

#create array of 10 zeros
# zeros_arr = np.zeros(10)
# print(zeros_arr)
# ones_arr = np.ones(10)
# print(ones_arr)
# create arr of 10 fives
# fives_arr = np.ones(10) * 5
# print(fives_arr)
# # create arr with elements from 10 - 50
# ten_to_fifty_arr = np.arange(10,51)
# print(ten_to_fifty_arr)
# # create arr of only even values from the above array
# print(ten_to_fifty_arr[ten_to_fifty_arr % 2 == 0])
# 3x3 matrix
# three_mat = np.arange(0,9).reshape(3,3)
# print(three_mat)
# identity 3x3 matrix - one argument for rows, columns
# print(np.identity(3))
# random number between 0 and 1 using NumPy
# print(np.random.rand(1))
# 25 random numbers sampled from a standard normal distribution
# print(np.random.randn(25))
# 10x10 mat of values between 0.01 and 1
# print(np.arange(0.01,1.01,0.01).reshape(10,10))
# array of 20 linearly spaced points
# print(np.linspace(0,1,20))

# NumPy Indexing and selection
mat = np.arange(1,26).reshape(5,5)
# print(mat)
# print specific subset of this matrix (12 till the end...)
#print(mat[2:,1:])
# get 1 value - 20
#print(mat[3:4,4:])
# get 2,7,12
# print(mat[:3,1:2])
# get last line
# print(mat[4:])
# get two last lines
# print(mat[3:])
# sum of mat
# print(mat.sum())
# std of mat
# print(mat.std())
# sum of all columns
# print(mat.sum(axis=0))
# sum of all rows
# print(mat.sum(axis=1))
