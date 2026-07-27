a=int(input("Enter First Number  "))
b=int(input("Enter Second Number  "))
def add():
    return a+b

def sub():
    return a-b

def mult():
    return a*b

print("Sum is ", add())
print(id(a))
print(id(b))
print("SUb is ", sub())
print("Mult is  ", mult())