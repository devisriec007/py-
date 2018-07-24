array = []
num = int(input('How many numbers: '))
 
for n in range(num):
    numbers = int(input('Enter number '))
    array.append(numbers)
 
print("Maximum element in the list is :", max(array))
