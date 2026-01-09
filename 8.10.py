def leap_year(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

y = int(input("Enter year: "))
if leap_year(y):
    print("Leap Year")
else:
    print("Not Leap Year")
