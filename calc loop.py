
print('Welcome to my program')

while True:
 print('=====================')
 print('1 = Add Number')
 print('2 = Subtract Number')
 print('3 = Multiply Number')
 print('4 = Divide Number')
 print('5 = Exit')

 num1 = float(input("Enter first number : "))
 num2 = float(input("Enter second number : "))
 opt = input('Enter your choice : ')
 if opt == '1':
    print('Result:', num1 + num2)
 
 elif opt == '2':
   print('Result:', num1 - num2)
 
 elif opt == '3':
   print('Result:', num1 * num2)
 
 elif opt == '4':
        if num2 == 0:
           print("Can't Divide by zero")
        else:
         print('Result:', num1 / num2)
 
 elif opt == '5':
    print('Exiting program.')
    exit()
 else:
  print('Invalid option. Please try again.')

