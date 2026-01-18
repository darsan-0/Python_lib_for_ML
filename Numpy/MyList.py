import time 
start = time.time()
a = [i for i in range(100000)]
for j in range(len(a)):
    print(f"{j}")
print(time.time()-start)