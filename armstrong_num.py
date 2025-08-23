n = int(input())
num = n
total = 0
nod = len(str(n))
while num>0:
    ld = num%10
    total = total+(ld**nod)
    num //=10

print(n==total)