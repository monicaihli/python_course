grades = [88,60,100,70] # a list of grades. Lists are iterable. We'll learn more soon!

print("Here are your grades:")
for grade in grades:
  if grade >= 70:
    print("{} is acceptable. Keep up the good work".format(grade))
  else:
    print("{} is not okay. No ipad for a month".format(grade))
print("Done listing Grades")