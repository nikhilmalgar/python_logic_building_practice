## An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

n = int(input())
num = n
total = 0
nod = len(str(n))
while num>0:
    ld = num%10
    total = total+(ld**nod)
    num //=10

print(n==total)