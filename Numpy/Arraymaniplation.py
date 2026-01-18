import numpy as np
arr = np.array([i+1 for i in range(12)])
print(arr)
print()
arr1 = arr.reshape(3,4)
print(arr1)
# Use case of flatten() ---> it couldn't Effect acutula one.
print(f"\n\n")
flatted = arr1.flatten()
flatted[0] = 10
print(flatted)
print(arr1)
print(f"\n\n")
# ravel() ---> if we modifie any changes in raveld array the
# changes are effected on actual array aslo

ravled = arr1.ravel()
ravled[0] = 10
print(ravled)
print(arr1)

