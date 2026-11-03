# Alexandra Cujba - Future CS Student
# Westminster Applicant - Sept 2027 Intake

class FutureStudent:
  def ___init___(self, name, city, dream):
       self.name = name
       self.city = city
       self.dream = dream

  def introduce(self):
       return f"I am {self.name} from {self.city}. Dream:{self.dream}"

  me = FutureStudent("Alexandra", "Botosani", "CS at Westminster")

print(me.introduce())
print("Skills: Python, Java, HTML - learning daily")
print("Ready for London 2027!")
