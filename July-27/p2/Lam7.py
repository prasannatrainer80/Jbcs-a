numbers = [12,5,22,66,20,11,13,98,21,13,90,15,189,222,62,41,23,100]
sortedList = lambda x : (sorted(i) for i in numbers)
print(sortedList(numbers))

for i in sortedList(numbers):
    print(i)