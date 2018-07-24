first = int(input("Enter first interval: "))  
last = int(input("Enter last interval: "))  
for number in range(first,last + 1):  
   sum = 0  
   temp = number  
   while temp > 0:  
       digit = temp%10  
       sum+= digit**3  
       temp //= 10  
       if number == sum:  
            print(number)  
