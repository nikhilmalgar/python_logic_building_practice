n = int(input("Enter a number to compute the factorial: "))


def non_resursive(num):
    fact = 1
    for i in range(1,n+1):
        fact *=i
        return fact
    
def recursive(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num * recursive(num -1)