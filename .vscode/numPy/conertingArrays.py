import numpy as np

#CONVERTING BETWEEN DATA TYPES
#creting an array of integers 
arr=np.array([1,2,3,4,5])

arr_folat=arr.astype(float)

#1converting to list
arr.tolist() #[1,2,3,4,5]
#converting from list
list=[4,5,56]
arr=np.array(list)
print(arr)

#2converting to Another Shape
arr=np.array([1,2,3,4,5,6])
#reshaping the array to 2X3
arr_reshaped=arr.reshape((2,3))
#outpuy  2 rows three columns

#3Flattening an Array 
#flatten() method , ravel() method

#4converting to different order -> copy() , order() method

arr=np.array([[1,2,3],[4,5,6]])
arr_fortan=arr.copy(order='F')
print(arr_fortan)

#5converting between arrays and pandas Data Frames
import numpy as np
import pandas as pd
#crrate an aarray
arr=np.array([[1,2,3],[4,5,6]])
#inside pd.DataFrame pass arr, and columns as paramters
df=pd.DataFrame(arr, columns=['a','b','c'])
