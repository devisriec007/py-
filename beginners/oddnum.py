lower=int(input("Enter the first interval for the range:"))
upper=int(input("Enter the last interval for the range:"))
for n in range(lower,upper+1):
    if(n%2!=0):
        print(n)
