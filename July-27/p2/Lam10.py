class Employ:
    def __init__(self, empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employ No {self.empno}  Employ Name {self.name}  Salary {self.salary}"

e1 = Employ(1, "Raj",88888)
e2 = Employ(2, "Mahesh",99999)
e3 = Employ(3,"Kishore",88882)
e4 = Employ(4,"Rajani",88823)
e5 = Employ(5, "Srikar",99823)

employs=[e1, e2, e3, e4, e5]

emp_sal_list=list(filter(lambda  x : x.salary > 90000, employs))
for x in emp_sal_list:
    print(x)