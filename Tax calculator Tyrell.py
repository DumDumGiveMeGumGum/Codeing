item1=input("Item 1 price: ")
bool(int(item1))
item2=input("Item 2 price: ")
bool(int(item2))
item3=input("Item 3 price: ")
bool(int(item3))
Tax1= int(item1)*0.12
Tax2= int(item2)*0.12
Tax3= int(item3)*0.12
Total1= int(item1)+ Tax1
Total2= int(item2)+ Tax2
Total3= int(item3)+ Tax3
TotalC= int(item1)+int(item2)+int(item3)
TotalC1=int(TotalC)*0.12
TotalC2= TotalC+ TotalC1
print("The cost of item 1 is ${0:.2f}".format(Total1))
print("The cost of item 1 is ${0:.2f}".format(Total2))
print("The cost of item 1 is ${0:.2f}".format(Total3))
print("The cost of all items is ${0:.2f}".format(TotalC2))
