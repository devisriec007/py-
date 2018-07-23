number = int(input("Enter any number: "))
if number > 0:
    for i in range(1000, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")
