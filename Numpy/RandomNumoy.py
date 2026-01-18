import numpy as np
import matplotlib 
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

arr_rg = gen(pcg(seed = 100))
random_gen = arr_rg.normal(size=(3,3))
print(random_gen)

arr_rg1 = gen(pcg(seed = 200))
random_gen1 = arr_rg.integers(low = 10 ,high = 100 ,size=(3,3))
print(random_gen1)