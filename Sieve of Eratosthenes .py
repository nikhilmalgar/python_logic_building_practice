## program to find the prime number using the Sieve of Eratosthenes.

def sieve_of_eratosthenes(n):
    prime = [True]*(n+1)
    prime[0]=prime[1]=False

    p=2
    while p*p<=n:
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    
    return[i for i in range(n+1) if prime[i]]
    
print(sieve_of_eratosthenes(50))