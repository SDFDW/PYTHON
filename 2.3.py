#Convert feet & inches into meter & centimeter
feet = int(input("Enter feet: "))
inch = int(input("Enter inches: "))

inches = feet*12 + inch
cm = inches * 2.54
meter = cm / 100

print("Meter:", meter)
print("Centimeter:", cm)

