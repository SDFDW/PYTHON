#Convert the time entered in hh,min and sec into seconds.
h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))

seconds = h*3600 + m*60 + s

print("seconds:", seconds)
