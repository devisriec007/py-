def Median(a, n):
    sorted(a)
    if n % 2 != 0:
        return float(a[n/2])
    return float((a[int((n-1)/2)] +
                  a[int(n/2)])/2.0)
a = [ 2451, 5283, 0.454, 2462, 7524, 5542, 845, 6412 ]
n = len(a)
print("Median =", Median(a, n))
