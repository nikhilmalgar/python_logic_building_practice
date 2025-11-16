import time 

a = input("Enter a Number: \n")

def big(): 
    if "." in a:
        integral, fractional = a.split(".")
        fractional = "." + fractional

    else:
        integral = a
        fractional = ".0"

    print("Integral part:", integral)
    print("Fractional part:", fractional)


## Small and eficient code
def small():
    i = a.find(".")
    print("Integral part:",a[:i])
    print("fractional_part:",a[i:])

start_big = time.time()
big()
end_big = time.time()
print("Big function time:", end_big - start_big)

start_small = time.time()
small()
end_small = time.time()
print("Small function time:", end_small - start_small)