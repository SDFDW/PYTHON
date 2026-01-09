#Check Triangle Valid using Angles
a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if a+b+c == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")