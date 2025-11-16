a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def hcf_simple(a,b):
    smaller = min(a,b)
    for i in range(1, smaller+1):
        if(a%i==0) and (b%i==0):
            hcf = i
    return hcf

def hcf_euclidean(a,b):
    while b!=0:
        a,b = b,a%b
    return a
print("HCF using simple method:", hcf_simple(a,b))
print("HCF using Euclidean algorithm:", hcf_euclidean(a,b))
