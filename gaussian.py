import math

import numpy as np

matrix_size = 3
filter = np.zeros((matrix_size,matrix_size), np.float32)
sigma = 1.5


for x in range((-matrix_size//2),matrix_size//2+1):
    for y in range(-matrix_size//2,matrix_size//2+1):
        # gaussian calculation 
        filter[x+matrix_size//2][y+matrix_size//2] = (1/(2*math.pi*sigma**2))*math.exp(-(x**2+y**2)/(2*sigma**2))

# The corner of the filter should equal 1
magnitude = 1 / filter[0][0] 
filter = filter * magnitude
filter = filter.round(2)

print(filter)


