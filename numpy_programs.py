import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
type(a)
dir(a)
a.shape=2,2,2
a.sum(axis=1)
a[0,0,0]

a.size
a.shape=2,4
a
a.shape
a.reshape(2,2,2)
a.shape=2,2,2
a[0,:,:]
data=np.array(range(1,101)).reshape(2,10,5)
data[1,5:8:2,:]
a=data[1,:,1:2]
a.shape
b=data[1,:,1]
b.shape

np.linspace(1,100,4)
np.zeros((2,6))
np.ones((2,6))+7
np.eye(5)
np.arange(1,100,3)
np.random.rand(7)
np.random.randn(1,100)
np.random.randint(1,100,4)


#create an array of 10 zeros
np.zeros(10)

#create an array of 10 ones
np.ones(10)


#create an array of 10 fives
np.ones(10)+4
np.ones(10)*5

#create an array of 10 to 50 integers
np.array(range(10,51))
np.arange(10,51)

#create an array of all even integers from 10 to 50 
np.array(range(10,51,2))
np.arange(10,51,2)

#create a 3*3 matrix with values ranging from 0 to 8
a=np.arange(0,9).reshape(3,3)
a

#create a 3*3 identity matrix
np.eye(3)

#use numpy to generate a random number between 0 to 1
np.random.rand()


# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
np.random.rand(25)


x=np.arange(0.01,1.01,0.01).reshape(10,10)
x

# Create an array of 20 linearly spaced points between 0 and 1:
np.linspace(0,1,20)


mat=np.arange(1,26).reshape(5,5)
mat[2:5,1:5]
mat[3,4]
mat[0:3,1:2]
mat[4,:]
mat[3:5,:]
mat.sum()
mat.std()
mat.sum(axis=0)


#Create a NumPy array of 10 zeros and then replace the fifth element with 1.
a=np.zeros(10)
a[4]=1
a


#Create a 6x6 matrix and fill the border with 1s, and the rest with 0s.
b=np.ones((6,6),dtype=int)
b[1:-1,1:-1]=0
b

#Given a 1D array, replace all values greater than 10 with 10.
c=np.array([25,1,5,34,56,23,45,2,9])
c[c>10]=10
c

#Create a 3x3 matrix with values from 1 to 9 and flatten it to a 1D array.
d=np.arange(1,10).reshape(3,3)
d
d.flatten()


#Generate a 3x3 random matrix and compute the sum of each row and column.
x=np.random.rand(3,3)
x
x.sum(axis=0)
x.sum(axis=1)


#Normalize a random 1D array (scale values between 0 and 1).
x=np.random.rand(10)
x


#Sort a NumPy matrix along the columns.
d=np.random.randint(1,100,9).reshape(3,3)
d
d.sort(axis=0)
d


# 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
np.__version__

# 3. Create a null vector of size 10 (★☆☆)
np.zeros(10)

# 4. How to find the memory size of any array (★☆☆)
null_vector=np.zeros(10)
null_vector.size


# 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
np.add.__doc__


# 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
nullVector=np.zeros(10)
nullVector[4]=1
nullVector

# 7. Create a vector with values ranging from 10 to 49 (★☆☆)
np.arange(10,50)

# 8. Reverse a vector (first element becomes last) (★☆☆)
vector=np.array([10, 11, 12, 13, 14])
vector[::-1]

# 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
np.arange(0,9).reshape(3,3)

# 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
arr=np.array([1,2,0,0,4,0]) 
arr.nonzero()

# 11. Create a 3x3 identity matrix (★☆☆)
np.eye(3,3)

# 12. Create a 3x3x3 array with random values (★☆☆)
np.random.randint(1,100,27).reshape(3,3,3)

# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
arr=np.random.randint(0,100,100).reshape(10,10)
arr.max()
arr.min()

# 14. Create a random vector of size 30 and find the mean value (★☆☆)
np.random.randint(1,100,30).mean()

# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
arr=np.ones((10,10))
arr[1:9,1:9]=0
arr

# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
arr=np.random.randint(0,100,100).reshape(10,10)
arr[0:10:9,:]=0
arr[:,0:10:9]=0
arr

#### 17. What is the result of the following expression? (★☆☆)
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
arr=np.arange(0,25).reshape(5,5)
length=arr.shape[1]
for i in range(length-1):
    arr[i+1,i]=i+1
arr

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
matrix=np.zeros((8,8))
matrix[1::2,::2]=1
matrix[::2,1::2]=1
matrix


matrix=np.zeros((8,8))
row=matrix.shape[0]
col=matrix.shape[1]
for i in range(row):
    for j in range(col):
        if i%2==0 and j%2==1:
            matrix[i,j]=1
        elif i%2==1 and j%2==0:
            matrix[i,j]=1
matrix
# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)

# 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
arr=np.array([[0,1],[1,0]])
np.tile(arr,(4,4))
# 22. Normalize a 5x5 random matrix (★☆☆)
np.random.rand(5,5)
# 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)

# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
matrix1=np.arange(15).reshape(5,3)
matrix2=np.arange(6).reshape(3,2)
matrix1 @ matrix2

# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
matrix=np.arange(10)
for i in range(10):
    if matrix[i]>=3 and matrix[i]<=8:
        matrix[i]=-matrix[i]
matrix
#### 26. What is the output of the following script? (★☆☆)
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
Z=np.arange(1,10).reshape(3,3)
Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z
# 28. What are the result of the following expressions? (★☆☆)
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float)
# 29. How to round away from zero a float array ? (★☆☆)
arr=np.array([2.1,3.4,5.6,7.5,8.6,9.6]).round()
arr
# 30. How to find common values between two arrays? (★☆☆)
arr1=np.array([2,4,6,7,10,8,9])
arr2=np.array([1,3,6,7,9])
np.intersect1d(arr1,arr2)
# 31. How to ignore all numpy warnings (not recommended)? (★☆☆)

# 32. Is the following expressions true? (★☆☆)
np.sqrt(-1) == np.emath.sqrt(-1)
# 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)

# 34. How to get all the dates corresponding to the month of July 2016? (★★☆)

# 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)

# 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)

# 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
arr=np.array([0,1,2,3,4])
np.tile(arr,(5,1))
#### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)

#### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
np.random.rand(10)
#### 40. Create a random vector of size 10 and sort it (★★☆)
vector=np.random.randint(1,50,10)
np.sort(vector)
# 41. How to sum a small array faster than np.sum? (★★☆)
from functools import reduce
arr=np.array([2,4,3,7,6,8])
reduce(lambda a,b:a+b,arr)
# 42. Consider two random arrays A and B, check if they are equal (★★☆)
arr1=np.array([2,4,6,7,10,8,9])
arr2=np.array([1,3,6,7,9])
np.array_equal(arr1,arr2)
# 43. Make an array immutable (read-only) (★★☆)
tuple(np.array([2,4,6,7,10,8,9]))
# 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)

# 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
vector=np.random.randint(1,50,10)
maximum=vector.max()
for i in range(10):
    if vector[i]==maximum:
        vector[i]=0
vector
#### 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)

#### 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)

#### 48. Print the minimum and maximum representable values for each numpy scalar type (★★☆)

# 49. How to print all the values of an array? (★★☆)
arr=np.array([2,4,6,7,10,8,9])
for i in  arr:
    print(i)
#### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)

#### 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)

#### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)

#### 53. How to convert a float (32 bits) array into an integer (32 bits) array in place?
np.int32(np.float32(np.array([2.3,3.4,5.6,7.8,1.1])))
#### 54. How to read the following file? (★★☆)
'''1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11'''
#### 55. What is the equivalent of enumerate for numpy arrays? (★★☆)

#### 56. Generate a generic 2D Gaussian-like array (★★☆)

#### 57. How to randomly place p elements in a 2D array? (★★☆)

#### 58. Subtract the mean of each row of a matrix (★★☆)