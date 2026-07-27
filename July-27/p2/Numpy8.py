import numpy as np

ages =np.array([12,55,88,22,19,4,22,18,17,82])
filter_array = ages >= 18
newarr = ages[filter_array]
result = np.array(newarr)
print(newarr)
print(result)