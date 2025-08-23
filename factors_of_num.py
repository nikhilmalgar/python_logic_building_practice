##  This program finds all the factors of a given number.
## It checks numbers from 1 up to sqrt(n) to find divisors.
## For each divisor i, both i and (n // i) are added to the list of factors.
## Finally, the list is sorted and printed.

from math import sqrt
n = int(input())
num = n
result = []
for i in range(1,int(sqrt(num))+1):
    if num %i==0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
result.sort()
print(result)
