class Students:
    def __init__(self) :
     try :
        self.rollno = input('enter rollno: ') 
        self.name = input('enter name: ')
        self.marks = int(input('enter marks: '))
        self.totmarks = int(input('enter total marks:' ))
     except ValueError:
        print("Wrong Values")
    
    def calc(self):
       perc = (self.marks/self.totmarks)*100
       return perc
    def printstd(self):
       print(f"Roll no: {self.rollno},",f"Name:{self.name},",f"Marks:{self.marks},",f"Total Marks:{self.totmarks},")

allstudents = {}
def add_student():
   std = Students()
   allstudents[std.rollno] = std
   return std

def find_std():
   search = input('Enter student roll no: ')
   if search in allstudents.keys():
      allstudents[search].printstd()
   else:
      print("Student not found.")

def update_student():
   search = input('Enter roll no: ')
   if search in allstudents.keys():
      del allstudents[search]
      add_student()
   else:
      print('Student not found')

def remove_student():
   search = input('Enter roll no: ')
   if search in allstudents.keys():
      del allstudents[search]
   else:
      print('Student not found')
   
while True:
   print('Press 1 for Add student ')
   print('Press 2 for Find student')
   print('Press 3 for Update student')
   print('Press 4 for Remove Student')
   print('Press 5 for Print all Students')
   print('Press 6 for Exit')
   choice = int(input('ENter your choice: '))
   if choice == 1:
      add_student()
   elif choice == 2:
      find_std()
   elif choice == 3:
      update_student()
   elif choice == 4:
      remove_student()
   elif choice == 5:
      if not allstudents:
         print('No student found')
      for std in allstudents.values():
            std.printstd()

   elif choice == 6:
      exit()