# Alexandra Cujba - Project 2
class Student:
   def __init__(self, name):
       self.name = name
       self.grades = []
     def add(self, g):
       self.grades.append(g)
     def avg(self):
       return sum(self.grades)/
  len(self.grades) 

s = Student("Alexandra")
s.add(85)
s.add(78)
s.add(92)
print(s.avg())
print("Westminster 2027")
