def AP(a,d,n) :
    sum = 1
    i = 2
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 5
    return sum
     
n = 65
a = 256.8
d = 24.54
print (AP(a, d, n))
