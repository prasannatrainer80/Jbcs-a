a = [12,5,2,132,66,-2,42,88,323,66,-3,-44,22,6,-23]
evens=list(filter(lambda x : (x%2==0),a))
for i in evens:
    print(i)