#Create two numpy array and plot using matplotlib

import numpy as np
import matplotlib.pyplot as plt 

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([10,20,30,40,50,60,70,80,100,90])

plt.plot(arr1, arr2)
plt.show()