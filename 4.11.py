#Armstrong Number
n = int(input("Enter number: "))
temp = n
digits = len(str(n))
sum = 0

while temp > 0:
    d = temp % 10
    sum = sum + d**digits
    temp = temp // 10

if sum == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")