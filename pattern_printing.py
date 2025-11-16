def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=' ')
        print()

def increasing_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end = ' ')
        print()

def decreasing_trianlge(n):
    for i in range(n):
        for j in range(i,n):
            print("*", end = ' ')
        print()

def right_side_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print(" ", end = ' ')
        for j in range(i+1):
            print("*", end = ' ')
        print()

def left_sided_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(' ',end=" ")
        for j in range(i,n):
            print("*",end = ' ')
        print()

def hill_pattern(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end = ' ')
        for j in range(i):
            print("*",end=' ')
        for j in range(i+1):
            print("*",end=' ')
        print()

def reverse_hill_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(' ',end=' ')
        for j in range(i,n-1):
            print("*",end= ' ')
        for j in range(i,n):
            print("*",end=' ')
        print()





n = int(input("Enter the number number of wors:\n"))
print(" 1.square_pattern \n 2. increasing_triangle \n 3. decreasing_triangle \n " \
"4. right_side_triangle \n 5. left_side_trianlge \n 6. hill_pattern \n 7. reverse_hill_pattern \n")
pattern = int(input("Enter the number of pattern which you want to print: \n"))

match pattern:
    case 1:
        square_pattern(n)
    case 2:
        increasing_triangle(n)
    case 3:
        decreasing_trianlge(n)
    case 4:
        right_side_triangle(n)
    case 5:
        left_sided_triangle(n)
    case 6:
        hill_pattern(n)
    case 7:
        reverse_hill_pattern(n)
    case _ :
        print("Invalid input ! please enter the number between 1-7.")
