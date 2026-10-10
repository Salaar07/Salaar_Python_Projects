user  =  input("Enter :")
dig = True
for i in range(0, len(user), 1):
  code =  (ord(user[i]))
  if code >= 48 and code<=57:
    dig = True
  else:
     dig =False
     break
if dig ==True:
  print("It is a digit")
else:
  print('not a digit')
  

