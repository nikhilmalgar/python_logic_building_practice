##  program to count the number of digits in a integer.
num=int(input("Enter the number:"))
count = 0
if(num==0):
    count=1
else:
    while(num>0):
        num //=10
        count+=1
    
print(count)

