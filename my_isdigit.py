def my_isdigit():
    user = input("Enter: ") 

    if user == "":  
        return False

    for i in range(0,len(user),1):
        code = ord(user[i])
        if code < 48 or code > 57:  
            return False

    return True
my_isdigit()
#If we want to print result we can simply use
#if my_isdigit:
#   print('it is a digit')
#else:
#   print('not a digit')
  