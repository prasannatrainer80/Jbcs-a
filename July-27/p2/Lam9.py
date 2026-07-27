a = [12,5,2,132,66,-2,42,88,323,66,-3,-44,22,6,-23]
neg_nos=list(filter(lambda x : (x < 0),a))
for i in neg_nos:
    print(i)

ages =[13, 90, 17, 59, 21,60,5]
voters = list(filter(lambda  age : age >= 18, ages))
print("Voters Details are \n\n")
for v in voters:
    print(v)