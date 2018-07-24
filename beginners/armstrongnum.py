number=int(input("Enter a number: "))  
sum=0  
temp=number  
  
while temp > 0:  
   value=temp%10  
   sum +=value**3  
   temp//=10  
   if number==sum:  
       print(number,"is an Armstrong number")  
else:  
    print(number,"is not an Armstrong number") 
