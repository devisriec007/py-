number = [3, 5]
max = 100
result = 0
for num in number:
    for i in range(1,max):
        if num*i < max:
       result += num*i
  print result
        result = 0
         for i in range(0,max):
           if i%3 == 0 or i%5 == 0:
     result += i
print(result)
