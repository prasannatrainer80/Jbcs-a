import numpy as np

x=1
arr =np.array([12,5,23,21,66,22,19])
for i in arr:
    x = x * i
print("Sum is  ", np.sum(arr))
print("MUltiplied Value ", x)
print("Maximum Value is  ", np.max(arr))
print("Minimum Value is ", np.min(arr))
print("Sorted Data of numpy ", np.sort(arr))