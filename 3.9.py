#
m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
m3 = int(input("Enter mark3: "))
m4 = int(input("Enter mark4: "))
m5 = int(input("Enter mark5: "))

per = (m1+m2+m3+m4+m5)/5

if per >= 60:
    print("First class")
elif per >= 50:
    print("Second class")
elif per >= 40:
    print("Pass class")
else:
    print("Fail")
