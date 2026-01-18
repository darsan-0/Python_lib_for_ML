import numpy as np
import time 
start = time.time()
arr = np.arange(100000)
for j in range(len(arr)):
    print(arr[j])
print(time.time()-start)