class Demo:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return (f"A value {self.a}  "
                f"B value {self.b}")

obj1=Demo(12,5)
print(obj1)
obj2=Demo(523,111)
print(obj2)