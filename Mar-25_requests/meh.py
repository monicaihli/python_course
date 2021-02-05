import requests

r = requests.get("http://kitty.ninja/a")
if r.status_code == 200:
  print("Success!")
elif r.status_code == 503:
  print('Too much server traffic, wait 20 minutes and try again.')
elif r.status_code == 404:
  print("Resource not found")
else:
  print("Unknown problem.")