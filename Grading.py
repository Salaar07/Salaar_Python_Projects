#Take input
print("Enter Marks")
val1 = int(input("English:"))
val2 = int(input("Urdu:"))
val3 = int(input("Computer:"))
val4 = int(input("Maths:"))
val5 = int(input("Physics:"))
val6 = int(input("Pak std:"))
val7 = int(input("Islamiat:"))
val8 = int(input("Practical:"))
#Add input
tot = val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8
if (val1<=100 and val2<=100 and val3<=100 and val4<=100 and val5<=100 and val6<=100 and val7<=100 and val8<=100):
 perc = float(tot / 800)* 100
 perc = round(perc,2)
 print("Total Marks =",tot)
 print("Percentage = ",perc)
#Calculate Pass or Fail
 if perc>=40:
    print("Result = Pass")
 else:
       print("Result = Fail")
#Calculate grade
 if perc>=40 and perc<50:
        print("Grade:E")
 elif perc>=50 and perc<60:
        print("Grade:D")
 elif perc>=60 and perc<70:
        print("Grade:C")
 elif perc>=70 and perc<80:
        print("Grade:B")
 elif perc>=80 and perc<90:
         print("Grade:A")
 elif perc>=90 and perc<100:
        print("Grade:A+")
else:
      print("Invalid marks entered, Each subject has 100 total marks")
