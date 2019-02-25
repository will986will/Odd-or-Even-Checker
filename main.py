run = 1
even = ["0","2","4","6","8"]
while run == 1:
  num = str(input("Enter your number: "))
  numLen = len(num)
  number = []
  number.append(num[numLen-1])
  if number[0] in even:
    print (num,"is even")
  else:
    print (num,"is odd")
  run = input("Would you like to go again? press 1. If not press Enter")
