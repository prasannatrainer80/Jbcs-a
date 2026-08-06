from abc import abstractmethod

class Vehicle:
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def type(self):
        pass

class Bike(Vehicle):
    def name(self):
        print("Vehicle is Bike Pulsor")

    def type(self):
        print("Its Two-Wheeler")

class Car(Vehicle):
    def name(self):
        print("Name is Car...")
    def type(self):
        print("Its Four Wheeler")

obj1=Car()
obj2=Bike()
list=[obj1,obj2]
for ob in list:
    ob.name()
    ob.type()
    print("==================")