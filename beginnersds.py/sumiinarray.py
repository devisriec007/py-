lst = []
number = int(input("How many numbers:"))
for m in range(number):
    numbers = int(input("Enter the number"))
    lst.append(numbers)
print("Sum of elements in a given list is :", sum(lst))
