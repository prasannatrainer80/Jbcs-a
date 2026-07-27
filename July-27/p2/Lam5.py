numbers = [12,5,22,66,20,11,13,98,21,13,90,15,189,222,62,41,23,100]
# next i need to print all the number by using lambda funciton

list1=[lambda arg=x: arg+1 for x in numbers]
for v in list1:
    print(v())