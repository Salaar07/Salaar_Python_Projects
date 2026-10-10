class Students:
    def __init__(self,rollno,name,marks,totmarks) :
     self.rollno = rollno 
     self.name = name
     self.marks = marks
     self.totmarks = totmarks
    
    def calc(self):
       perc = (self.marks/self.totmarks)*100
       return perc
    def printstd(self,rollno):
       print(rollno)

std1 = Students(895,'M.Salaar',522,560)
v = std1.calc()
print(v)
std2 = Students(895,'M.Atabak',500,560)
print(std2.calc())

