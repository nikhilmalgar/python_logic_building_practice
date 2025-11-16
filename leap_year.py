year = input("Enter the year\n")

if year.isdigit() and len(year)==4:
    year = int(year)

    if(year % 400==0) or (year % 100 !=0 and year % 4==0):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
else:
    print("Invalid input ! please enter 4 digit year.")