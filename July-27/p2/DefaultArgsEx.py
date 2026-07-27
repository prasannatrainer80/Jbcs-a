def show(empno,name,salary,city="Hyderabad"):
    """This Show Function is About Default Arguments  """
    print("Employ No ", empno)
    print("Employ Name  ", name)
    print("Salary  ", salary)
    print("City  ", city)

print(show.__doc__)
show(1, "Arjit",88323)
show(3, "Sravanthi",98823,"Delhi")