num = input("please enter a number")
run = "yes"
while run == "yes":

  if num.isnumeric():
    run = "no"
  if not num.isnumeric():
    num = input("please enter another number")