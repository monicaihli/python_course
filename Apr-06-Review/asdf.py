def validate(num_input):
  if num_input.isnumeric():
    return(True)
  else:
    return(False)

demo_list = ["1", "2", "apples", "3"]
for item in demo_list:
  outcome = validate(item)
  print("Is {} a valid number? {}".format(item,outcome))


