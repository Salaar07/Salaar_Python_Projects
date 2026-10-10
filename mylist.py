mylist = ["M.Salaar",'895','Active','95.5%',"Python",'JDC']
print(mylist)
print('===========================')
user = (input("Enter item to remove: "))

if user in mylist:
    val = mylist.index(user)
    mylist.pop(val)
    print(mylist)
else:
    print('Item not found')