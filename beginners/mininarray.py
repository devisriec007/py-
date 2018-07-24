array = []
num = int(input('How many numbers: '))
 
for n in range(num):
    numbers = int(input('Enter number: '))
    array.append(numbers)
print("Minimum element in the array is :", min(array))
