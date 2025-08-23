## It extracts each digit (not “integer”) from a single number and stores them in a list.

num = int(input("enter the number:"))
digit=[]

while num>0:
    digit.append(num%10)
    num //=10

digit.reverse()
print(digit)