## A palindrome is a word, phrase, or number that reads the same forwards and backwards.

n = int(input())
num = n
result = 0

while(num>0):
    ld = num%10
    result = (result*10)+ld
    num //=10

print(n==result)