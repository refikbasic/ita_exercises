year=int(input("Please enter year: "))
if year%4 == 0:
    print("It is leap year!") 
elif year%100 == 0 and year%400 == 0:
    print("It is leap year!")
else:
    print("That is not leap year.")