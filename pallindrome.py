n = int(input())
num = n
result = 0

while(num>0):
    ld = num%10
    result = (result*10)+ld
    num //=10

print(n==result)