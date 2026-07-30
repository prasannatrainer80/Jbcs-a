def max(a,b):
    if a > b:
        return a
    else:
        return b

Max = lambda a,b : a if a > b else b
Min = lambda a,b : a if a < b else b
print("Max  ", Max(12,5))
print("Min  ", Min(12,5))