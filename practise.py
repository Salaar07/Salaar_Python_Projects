class Students():
    def __init__(self):
        try:    
            self.rollno = input('Enter Roll Number: ')
            self.name = input('Enter Name: ')
            self.marks = int(input('Enter marks:'))
            self.tot_marks = int(input('Enter total marks:'))
        except ValueError:
            print('Invalid values')
    def print_std(self):
        print(print(f"Roll no: {self.rollno},",f"Name:{self.name},",f"Marks:{self.marks},",f"Total Marks:{self.tot_marks}"))

allstudents = {}
def add_students():
    std = Students()
    allstudents[std.rollno] = std
    return std
def find_std():
    search = input('Enter Roll Number')
    if search in allstudents.keys():
        allstudents[search].print_std()
    else:
        print('Student not found')
def update_std():
   search = input('Enter Roll Number')
   if search in allstudents.keys():
       del allstudents[search]
       add_students()
   else:
       print('Student not found')
def remove_std():
    search = input('Enter Roll Number')
    if search in allstudents.keys():
        del allstudents[search]
    else:
        print('Student not found')
def print_all():
    if not allstudents:
        print('No Students found')
    for std in allstudents.values():
        print(std.print_std())
        
while True:
   print('Press 1 for Add student ')
   print('Press 2 for Find student')
   print('Press 3 for Update student')
   print('Press 4 for Remove Student')
   print('Press 5 for Print all Students')
   print('Press 6 for Exit')
   choice = int(input('ENter your choice: '))
   if choice == 1:
      add_students()
   elif choice == 2:
      find_std()
   elif choice == 3:
      update_std()
   elif choice == 4:
      remove_std()
   elif choice == 5:
      if not allstudents:
         print('No student found')
      for std in allstudents.values():
            std.print_std()
   elif choice == 6:
      break
else:
       print('Enter valid choice')