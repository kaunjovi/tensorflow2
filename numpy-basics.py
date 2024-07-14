import numpy as np 

print(f"NumPy version is {np.__version__}")

myList = [1,4,6,8]
array = np.array(myList)
print(f"Array is {array}")
print(f"The array is of type : {type(array)}")
print(f"The list was of type : {type(myList)}")


# Array can have many dimensions, starting from zero
# Python will make a guess depending upon the initiation 

zero_dim_array = np.array(1)
print(f"The number of dimensions of this array is {zero_dim_array.ndim}")

one_dim_array = np.array([1, 2,3,4,5,6,7,8])
print(f"The number of dimensions of this array is {one_dim_array.ndim}")

two_dim_array = np.array([[1,2,5,6,7],[3,4,5,6,7]])
print(f"The number of dimensions of this array is {two_dim_array.ndim}")

# Array can have many dimensions, starting from zero
# Python will make a guess depending upon the initiation 
# Or you can be explicit about it. 

explicit_dim_array = np.array(2, ndmin=5)
print(f"The number of dimensions of this array is {explicit_dim_array.ndim}")

# Array indexing - get to a specific element in the array 
print(f"The first element of the first element is {two_dim_array[1,0]}")
print(f"Or we could go for the last elements {two_dim_array[1,-1]}")

# You could index it, or you could slice it. start : end : step 
# print(f"The array {one_dim_array}")
# print(f"Get a slice of that array {one_dim_array[1:]}")
# print(f"Get a slice of that array {one_dim_array[:4]}")
# print(f"Get a slice of that array {one_dim_array[:4]}")
# print(f"Get a slice of that array {one_dim_array[-3:-1]}")
# print(f"Get a slice of that array {one_dim_array[1:4:2]}")

# Whoa. Now we are mixing this up.
# print(f"The array {two_dim_array}")
# print(f"Get a slice of that array {two_dim_array[0:2,1]}")
# print(f"Get a slice of that array {two_dim_array[1,:5]}")

# print(f"Data type of the array is {one_dim_array.dtype}")
# 
# one_more_array = np.array(['check', 'once', 'more'])
# print(f"Data type of the array is { one_more_array.dtype}")
# 
# arr = np.array([1, 2, 3, 4], dtype='S4')
# print(f"Data type of the array is { arr.dtype}")

# int64
arr_of_int = np.array([1, 2, 3])  
print(f"Data type of the array is { arr_of_int.dtype}")

# float64
arr_of_float = arr_of_int.astype(float)
print(f"Data type of the array is { arr_of_float.dtype}")
