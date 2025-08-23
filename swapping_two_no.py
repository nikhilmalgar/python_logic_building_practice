## swapping of two numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("First number before swapping:",num1)
print("Second number before the swapping:",num2)

temp = num1
num1=num2
num2=temp

print(f"Numbers after Swapping \n num1:{num1} \n num2:{num2} ")
