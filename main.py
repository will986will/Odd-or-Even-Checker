run = "1"
while run == "1":
  num = int(input("Enter your number: "))
  if num % 2 == 0:
    print (num,"is even")
  else:
    print (num,"is odd")
  run = str(input("Would you like to go again? press 1. If not press Enter"))
