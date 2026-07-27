import numpy as np

list = []
n = int(input("Enter N value  "))
for i in range(n):
    x = int(input("Enter Value  "))
    list.append(x)

new = np.array(list)
print(new)

x=int(input("Enter the element to Search  "))
print(np.where(new==x))
