import re
number = input('Enter Phone Number: ').strip()
pattern = "^\+?([1-9]?)(\.|-|\s|\()?[0-9]{3}(\.|-|\s|\))*[0-9]{3}(\.|-|/s)?"
if re.findall(pattern, number):
  print("Valid phone number")
else:
  print("Invalid phone number")