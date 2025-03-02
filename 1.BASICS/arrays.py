import array
import numpy as np

arr = array.array('i', [10, 20, 30, 40])  # 'i' means integer type
arr.append(50)
print(arr)  # Output: array('i', [10, 20, 30, 40, 50])

arr2 = np.array([10, 20, 30, 40])  # Creating a NumPy array
arr2 = arr2 * 2  # Element-wise operation
print(arr2)  # Output: [20 40 60 80]