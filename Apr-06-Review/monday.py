class Student:

  def __init__ (self, name, major, gradyear):
    self.name = name
    self.major = major
    self.gradyear = gradyear
  def give_name(self):
    print("The student's name is {}.".format(self.name))

new_student1 = Student('Joe', 'Cat Psychology', 2021)
new_student2 = Student('Mary', 'Mermaid Studies', 2022)
new_student3 = Student('June', 'I HAVE NO IDEA', 2021)

students = [new_student1,new_student2,new_student3]

for student in students:
  student.give_name()