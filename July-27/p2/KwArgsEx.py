def show(**kwargs):
    """Function document information to define about Key-Args Concept  """
    for key,value in kwargs.items():
        print(key, "  ", value, end=" ")
    print()

print(show.__doc__)
show(empno=1,name="Prasanna",salary=88234)
show(empno=1,name="Arjit",gender="Male",salary=88233,status="Yes")
