def orderDetails(customerName,*orderItems):
    print("Customer Name ", customerName, end="  ")
    for i in orderItems:
        print(i, end="  ")
    print()

orderDetails("Sanjay Purchaed Items Are  ", "Books","Laptop","Watch")
orderDetails("Utkarsh Purchased Items Are  ", "Books","Mobile","Watch","Laptop")
orderDetails("Sravanthi Purchased Items Are  ","Books","Watch")
orderDetails("Mithun Purchased Items Are  ")