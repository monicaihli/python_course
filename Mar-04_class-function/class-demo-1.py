#
#  Date:  March 04, 2020
#  File:  class-demo-1.py
#  Auth:  monica@utk.edu
#  Desc:  Demonstrates a simple implementation of a class
#  #.


from _datetime import datetime

def main():
  new_student = Student("Joann", "Fishstick Studies", 2022)
  print(new_student.name)
  print(new_student.gradyear)
  yearstillgrad = new_student.timetograd(datetime.today().year) # accessing a function associated w/ class
  print("This student has {} more years till graduation.".format(yearstillgrad))

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