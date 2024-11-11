class Student:
 def __init__(self,name,marks):
        self.name = name
        self.marks = marks
       
 def avg(self):
       sum = 0
       for i in self.marks:
         sum+=i
       print(" The avg of the marks is " + str(sum/3))


s1 = Student("Aakshat",[20,40,60])
s1.avg()