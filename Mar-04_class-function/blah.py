#
#  Date:  March 04, 2020
#  File:  class-demo-1.py
#  Auth:  monica@utk.edu
#  Desc:  Demonstrates a simple implementation of a class
#  #.


from _datetime import datetime

def main():
    name = input("Student name: ")
    major = input("Major: ")
    gradyear = input("Graduation Year: ")
    new_student = Student(name, major, gradyear)
    new_student.give_name()


class Student:

  # use a constructor method to initialize an instance of the class
  def __init__(self, name, major, gradyear):
    self.name = name
    self.major = major
    self.gradyear = gradyear

  def give_name(self):
    print("The student's name is {}.".format(self.name))

  def timetograd(self, current_year):
    timetograd = self.gradyear - current_year
    return(timetograd)


if __name__ == "__main__":
  main()