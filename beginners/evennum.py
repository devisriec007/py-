lower = int(input("Enter the first interval : "))
upper = int(input("Enter the last interval : "))
for number in range(lower,upper+1):
  if(number%2 == 0):
    print(number)
